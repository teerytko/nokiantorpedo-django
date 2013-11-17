(function() {
require(['jquery', 'bootstrap', 'events', 'feeds', 'fb', 'htmlmixedmode'], 
	function($, bootstrap, events, feeds, fb, htmlmode) {
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
