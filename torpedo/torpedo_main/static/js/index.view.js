(function() {
require(['jquery', 'bootstrap', 'feeds'], function($, bootstrap, feeds) {
	leftfeed = {'titleurl': '/forum/2/',
				'feedurl': '/forum/feeds/posts/'};

	var facebook = function(d, s, id) {
		  var js, fjs = d.getElementsByTagName(s)[0];
		  if (d.getElementById(id)) return;
		  js = d.createElement(s); js.id = id;
		  js.src = "//connect.facebook.net/fi_FI/all.js#xfbml=1&appId=205098582998927";
		  fjs.parentNode.insertBefore(js, fjs);
	};
	$(document).ready(function() {
		facebook(document, 'script', 'facebook-jssdk');
	});
});
}).call(this);