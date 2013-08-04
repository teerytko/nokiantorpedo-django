(function() {
require(['jquery', 'bootstrap'], function($, bootstrap) {
	leftfeed = {'titleurl': '/forum/2/',
				'feedurl': '/forum/feeds/forum/2/'};
	$(document).ready(function() {
		$('#endurancetabs a').click(function (e) {
			e.preventDefault();
			$(this).tab('show');
			if ($(this).attr('href') == '#events') {
				$('#events-nav').show();
				$('body').scrollspy({target: "#events-nav",
						offset: 0});
			}
			else {
				$('#events-nav').hide();
			}
		})

	});
});
}).call(this);