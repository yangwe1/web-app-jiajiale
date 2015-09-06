#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
