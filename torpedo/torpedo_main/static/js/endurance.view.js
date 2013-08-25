(function() {
require(['jquery', 'bootstrap'], function($, bootstrap) {
	leftfeed = {'titleurl': '/forum/2/',
				'feedurl': '/forum/feeds/forum/2/'};
	$(document).ready(function() {
		var loc = window.location;
		$('#endurancetabs a').click(function (e) {
			e.preventDefault();
			$(this).tab('show');
			loc.hash = $(this).attr('href');
			if ($(this).attr('href') == '#events') {
				$('#events-nav').show();
				$('body').scrollspy({target: "#events-nav",
						offset: 2});
			}
			else {
				$('#events-nav').hide();
			}
		})
		if (loc.hash) {
			tab = $(loc.hash + '-link');
			tab.trigger('click');
		}

	});
});
}).call(this);