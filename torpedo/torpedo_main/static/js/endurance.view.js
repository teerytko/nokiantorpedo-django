(function() {
require(['jquery', 'bootstrap', 'events'], function($, bootstrap, events) {
	leftfeed = {'titleurl': '/forum/2/',
				'feedurl': '/forum/feeds/forum/2/'};
	$(document).ready(function() {
		var loc = window.location;
		$('#endurancetabs a').click(function (e) {
			e.preventDefault();
			$(this).tab('show');
			loc.hash = $(this).attr('href');
			if ($(this).attr('href') == '#events') {
				$('body').scrollspy({target: "#events-nav",
						offset: 2});
			}
		})
		if (loc.hash) {
			tab = $(loc.hash + '-link');
			tab.trigger('click');
		}
		events.update_events(5, '/events/feed/Torpedo Endurance/');
	});
});
}).call(this);