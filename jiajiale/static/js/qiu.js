$(function() {
    var index = 0;
    $.extend({
        showEachPic: function() {
            $('#content li').each( function (i) {
                var $this = $(this);
                switch(i){
                    case 0:
                        eachAnimate($this,0,0);
                        break;
                    case 1:
                        eachAnimate($this,0,'320px');
                        break;
                    case 2:
                        eachAnimate($this,0,'640px');
                        break;
                    case 3:
                        eachAnimate($this,0,'960px');
                        break;
                    case 4:
                        eachAnimate($this,'320px',0);
                        break;
                    case 5:
                        eachAnimate($this,'320px','320px');
                        break;
                    case 6:
                        eachAnimate($this,'320px','640px');
                        break;
                    case 7:
                        eachAnimate($this,'320px','960px');
                        break;
                    case 8:
                        eachAnimate($this,'640px','0');
                        break;
                    case 9:
                        eachAnimate($this,'640px','320px');
                        break;
                    case 10:
                        eachAnimate($this,'640px','640px');
                        break;
                    case 11:
                        eachAnimate($this,'640px','960px');
                        break;
                };
            });
        },
        showEachWord: function() {
            $('.coverCon li').each( function (i) {
                var $this = $(this);
                switch(i){
                    case 0:
                        eachAnimate($this,0,'27%');
                        break;
                    case 1:
                        eachAnimate($this,0,'54%');
                        break;
                    case 2:
                        eachAnimate($this,'30%','70%');
                        break;
                    case 3:
                        eachAnimate($this,'60%','53%');
                        break;
                    case 4:
                        eachAnimate($this,'60%','25%');
                        break;
                    case 5:
                        eachAnimate($this,'30%','10%');
                        break;
                };
            });
        },

        hideEachPic: function() {
            $('#content li').each( function (i) {
                var $this = $(this);
                eachAnimate($this,'25%','40%');
            });
        },

        hideEachWord: function() {
            $('.coverCon li').each( function (i) {
                var $this = $(this);
                eachAnimate($this,'25%','40%');
            });
        },

        showClickB: function() {
            $('.showEachPic').html('还有惊喜!').parent().show();
        },
        
        showClick: function() {
            $('.coverCon').hide();
            $('.content').show();
            $('.showEachPic').html('揭盖有惊喜!').parent().show();
        },

        /*
        hideStartPic: function() {
            $('.coverImg').animate({
                'top':'-1200px',
                'left':'-1920px'
            },2000);
        },
        showStartPic: function() {
            $('.coverImg').animate({
                'top':'0',
                'left':'0'
            },2000);
        }
        */
    });

    // setTimeout('$.hideStartPic()',2000);

    $(document).on('click','.showEachPic' ,function() {
        index += 1;
        var check = index % 2;
        
        var $this = $(this),
            $parent = $(this).parent();

        if ( check == 1 ) {
            $parent.hide();
            $.showEachPic();
            setTimeout('$.hideEachPic()',6000);
            setTimeout('$.showClickB()',8000);
        } else if ( check == 0 ){
            $('.content').hide();
            $('.coverCon').show();
            $.showEachWord();
            setTimeout('$.hideEachWord()',6000);
            setTimeout('$.showClick()',8000);
        };
    });

    function eachAnimate($this,eachTop,eachLeft){
        $this.animate({
            'top':eachTop,
            'left':eachLeft
        },2000);
    }
});
