(function() {
  requirejs.config({
    baseUrl: STATIC_URL + 'js',
    paths: {
      'jquery':     'jquery-ui-1.9.2.custom/js/jquery-1.8.3',
      'jqui':       'jquery-ui-1.9.2.custom/js/jquery-ui-1.9.2.custom',
      'scalendar':   '../events/js/scalendar',
      'eventCalendar':  '../events/js/vendor/jquery.eventCalendar',
    },
    shim: {
      eventCalendar: {
          deps: ['jquery']
      },
      jqui: {
          deps: ['jquery']
      },
    }
  });
}).call(this);
