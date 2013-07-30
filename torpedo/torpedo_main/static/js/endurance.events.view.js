(function() {
require(['jquery', 'bootstrap'], function($, bootstrap) {
	$(document).ready(function() {
		$('body').scrollspy({target: "#scroll-nav", offset: 0});
	});
});
}).call(this);