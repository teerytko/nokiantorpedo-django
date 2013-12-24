(function() {
  requirejs.config({
    baseUrl: STATIC_URL + 'js',
    paths: {
      'jeditable':  'vendor/jquery.jeditable',
      'dataTables':  'vendor/jquery.dataTables',
    },
    shim: {
      jutils: {
          deps: ['jquery']
      },
      jeditable: {
          deps: ['jquery']
      },
      dataTables: {
          deps: ['jquery']
      },
    }
  });
}).call(this);
