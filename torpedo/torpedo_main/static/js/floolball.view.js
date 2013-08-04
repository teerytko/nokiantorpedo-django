(function() {
require(['jquery', 'bootstrap'], function($, bootstrap) {
	$(document).ready(function() {
		$(function () {
			$('#torpedotabs a:last').tab('show');
		})
		$('#torpedotabs a').click(function (e) {
			e.preventDefault();
			$(this).tab('show');
		})
	});
});
}).call(this);