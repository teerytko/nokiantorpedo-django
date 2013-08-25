(function() {
require(['jquery', 'bootstrap'], function($, bootstrap) {
	$(document).ready(function() {
		var loc = window.location;
		$('#torpedotabs a').click(function (e) {
			loc.hash = $(this).attr('href');
			e.preventDefault();
			$(this).tab('show');
		})
		if (loc.hash) {
			tab = $(loc.hash + '-link');
			tab.trigger('click');
		}

	});
});
}).call(this);