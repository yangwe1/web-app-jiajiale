requirejs.config({
    baseUrl: 'static/js/lib',
    paths: {
        jquery: 'jquery',
        plugins: '../plugins'
    },
    'shim': {
        'cycle2':['jquery']
    }
});

require( ['jquery','plugins/cycle2'],function( $ , cycle ) {
});
