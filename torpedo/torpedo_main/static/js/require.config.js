(function() {
  requirejs.config({
    baseUrl: STATIC_URL + 'js',
    paths: {
      'jquery':     'jquery-ui-1.9.2.custom/js/jquery-1.8.3',
      'jqui':       'jquery-ui-1.9.2.custom/js/jquery-ui-1.9.2.custom',
      'bootstrap':  'bootstrap3/js/bootstrap',
      'backbone':   'vendor/backbone',
      'underscore': 'vendor/underscore',
      'date':       'vendor/date',
      'jatom':      'vendor/jatom',
      'jrss':       'vendor/jrss',
      'prefix-free':'vendor/prefix-free',
      'jfeed':      'vendor/jfeed',
      'jfeeditem':  'vendor/jfeeditem',
      'facebook':    '//connect.facebook.net/fi_FI/all',
    },
    shim: {
      jqui: {
          deps: ['jquery']
      },
      bootstrap: {
          deps: ['jquery']
      },
      backbone: {
          deps: ['underscore', 'jquery'],
          exports: 'Backbone'
      },
      underscore: {
          exports: '_'
      },
      jfeed: {
        deps: ['jquery', 'jfeeditem', 'jatom']
      },
      facebook: {
        exports: 'FB'
      }
    }
  });
}).call(this);
