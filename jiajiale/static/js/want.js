
requirejs.config({
    baseUrl: '/static/js/lib',
    paths: {
        'jquery': 'jquery',
        'sizzle': 'sizzle',
        'modules':'../modules',
        'plugins':'../plugins'
    },
    'shim': {
        'EventUtil.min': {
            exports:'EventUtil'
        },
        'validator.min': {
            exports: 'Validate'
        },
        'zepto': {
            exports: 'Zepto'
        }
    }
});

require( ['plugins/validator.min','EventUtil.min'],function( Validate,EventUtil ) {
    var $btn = document.getElementById( 'eachSubmitValidate' ),
        //$eachInput = document.getElementsByTagName( 'input' ),
        //$u_btn = $( '#eachSubmitValidate' ),
        $warn = document.getElementById( 'warn' );
    /*
    EventUtil.addHandler( $eachInput, 'focus', function() {
        console.log( 'test' );
    });
    */
    /*
    $( '#eachSubmitValidate' ).find( 'input[type="text"]' ).on( 'focus', function() {
        console.log( 'test' );
        var $this = $( this );
        $this.next().html( '' );
    });
    */
    var validator = new FormValidator( 'eachValidation' , [{
        name:'name',
        rules: 'required'
    },{
        name: 'cardID',
        rules: 'required|callback_check_cardID'
    },{
        name: 'address',
        rules: 'required'
    },{
    },{
        name: 'districtName',
        rules: 'required'
    },{
        name: 'floorName',
        rules: 'required'
    },{
    },{
        name: 'floorNum',
        rules: 'required'
    },{
        name: 'houseNum',
        rules: 'required'
    },{
        name: 'houseStyle',
        rules: 'required'
    },{
        name: 'houseSqure',
        rules: 'required'
    },{
        name: 'useSqure',
        rules: 'required'
    },{
        name: 'time',
        rules: 'required'
    },{
        name: 'phone',
        rules: 'required|callback_check_mobile'
    }], function( errors, event) {
            if( errors.length > 0 ) {
                event = EventUtil.getEvent( event );
                event.preventDefault();
                for( var i = 0,errorLen = errors.length; i < errorLen; i++ ) {
                    var $this = document.getElementsByName( errors[i].name ),
                        $next = sibling( $this[0] );
                    $next[1].innerHTML =  errors[i].message;
                }
            };
        }
    );

    validator.registerCallback( 'check_mobile', function( value ) {
        var regexp = /^1[3|4|5|7|8][0-9]\d{8}$/;
        if( regexp.test( value ) ) {
            return true;
        };
        return false;
    })
    .setMessage( 'check_mobile', '好像手机号错了呢' );

    validator.registerCallback( 'check_cardID', function( value ) {
        var regexp = /(^\d{15}$)|(^\d{17}([0-9]|X)$)/;
        if( regexp.test( value ) ) {
            return true;
        };
        return false;
    })
    .setMessage( 'check_cardID', '好像身份证号错了呢' );

    function sibling( elem ) {
        var r = [];
        var n = elem.parentNode.firstChild;
        for( ; n ;n =n.nextSibling ) {
            if( n.nodeType === 1 && n !== elem ) {
                r.push( n );
            }
        }
        return r;
    };
    /*
    function oSibling( elem ) {
        var a = [];
        var b = elem.parentNode.children;
        for( var i = 0; i < b.length; i++ ) {
            if( b[i] !== elem ) a.push( b[i] );
        };
        return a;
    };
    */
    function focusInput() {
        var ele = document.getElementsByTagName( 'input' );
        for( var i = 0,len = ele.length; i < len; i++ ) {
            if( ele[i].type != 'button' && ele[i].type != 'submit' && ele[i] != 'reset' ) {
                ele[i].onfocus = function() {
                    //console.log( this.name );
                    $next = sibling( this );
                    //console.log( $next );
                    $next[1].innerHTML = '';
                };
            };
        }
    };
    focusInput();
});
