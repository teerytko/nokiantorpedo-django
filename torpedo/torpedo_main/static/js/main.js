(function() {
require(['jquery', 'bootstrap', 'feeds', 'fb', 'htmlmixedmode'], 
	function($, bootstrap, events, feeds, fb, htmlmode) {
		leftfeed = {
				'feedurl': '/weblog/feeds/'};
		$(document).ready(function() {

			pageEditor = $('#id_content');
			if (pageEditor.length == 1) {
				var myCodeMirror = CodeMirror.fromTextArea(pageEditor[0], {
					mode: 'htmlmixed',
					lineNumbers: true,
					autofocus: true,
					coverGutterNextToScrollbar: true,
				});
			}
		});
	});
}).call(this);
