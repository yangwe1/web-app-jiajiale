#!/usr/bin/python
#coding=utf-8
#deploy nginx

from path import path
from sh import cp, rm, git
from os import system
from sys import argv

class AutoSetConf(object):
    ''' make a nginx conf file corresponding to specified project '''

    def __init__(self, _select):
        self.conf_d = path('/etc/nginx/conf.d')
        self.port_used = []
        # git.clone(unicode(argv[1]))
        # self.proj_d = unicode(argv[1]).split(':')[1]
        proj_d = unicode(argv[1])
        self.real_proj_d = proj_d.split('/')[-1]
        # print self.real_proj_d
        if _select == 'yw':
            self.current_dir = path('/home/yw/space/' + proj_d)
        if _select == 'gc':
            self.current_dir = path('/media/sf_work/' + proj_d)

    def load_static(self):
        for i in self.current_dir.walkdirs('static'):
            return unicode(i.abspath())

    def load_port(self):
        files = self.conf_d.files()

        for f in files:
            lines = f.lines()
            port = lines[1].strip(' ').strip('\n').strip(';').split(' ')[1]
            self.port_used.append(int(port))

    def load_sock(self):
        sh_file = self.current_dir.files('*.sh')[0]

        if not sh_file:
            print 'PLZ input the directory of .sh file :('
            exit(1)

        file_sh = open(sh_file, 'r')
        all_lines = file_sh.readlines()

        for line in all_lines:
            line_list = line.strip('\n').split(' ')
            for i in line_list:
                i = i.strip(' ').strip('\n\r')
            count = 0
            for x in line_list:
                count += 1
                if x == '-s' or x == '--socket':
                    file_sh.close()
                    # print line_list[count]
                    return line_list[count]
        #     file_sh.close()
        # return line_list[count]

    def setup(self, portno=8000):

        self.load_port()
        # print self.port_used
        some_no = portno
        conf_file = self.real_proj_d + '.conf'
        while 1:
            if some_no in self.port_used:
                some_no += 1
            else:
                print 'the port allocated is: ', some_no
                break

        conf = open(conf_file, 'w')
        conf.write('server {\n')
        conf.write('    listen' + ' ' + unicode(some_no) + ';\n')
        conf.write('    access_log /var/log/nginx/access.log;\n')
        conf.write('    error_log /var/log/nginx/error.log;\n')
        conf.write('    location / {\n')
        conf.write('        uwsgi_pass unix:' + self.load_sock() + ';\n')
        conf.write('        include uwsgi_params;\n')
        conf.write('    }\n')
        conf.write('    location ~ ^/static/ {\n')
        conf.write('        root ' + self.load_static() + ';\n')
        conf.write('    }\n')
        conf.write('}')
        conf.close()

        cp(conf_file, '/etc/nginx/conf.d')
        rm(conf_file)
        system("service nginx restart")

        return

if __name__ == '__main__':
    try:
        rock = AutoSetConf('yw')
    except:
        print 'sth wrong :( plz setup manually...'
        exit(1)
    port = raw_input('port: ')
    if port:
        rock.setup(portno=int(port))
    else:
        rock.setup(portno=8000)
    print 'Done!Check in your browser:)'
    # print argv
    # print argv[1], argv[2]
