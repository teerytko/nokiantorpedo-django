(function() {
require(['jquery', 'bootstrap', 'events'], function($, bootstrap, events) {
	leftfeed = {'titleurl': '/forum/2/',
				'feedurl': '/forum/feeds/forum/2/'};
	$(document).ready(function() {
		var loc = window.location;
		$('#endurancetabs a').click(function (e) {
			var href = $(this).attr('href');
			if (href[0] == '#') {
				loc.hash = $(this).attr('href');
				e.preventDefault();
				$(this).tab('show');
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