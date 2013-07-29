(function() {
	console.log('testig 1');
	require(['jquery'], function($) {
		console.log('TEST 2');
	});
}).call(this);