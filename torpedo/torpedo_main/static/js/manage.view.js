(function() {
require(['jquery', 'bootstrap', 'modaleditor'], function($, bootstrap, modaleditor) {
	$(document).ready(function() {
		$('.memberrow').hover(modaleditor.show_editors, modaleditor.hide_editors);
		$('.editors').click(modaleditor.edit);
		$('#editModalSave').click(modaleditor.edit_save);
	});
});
}).call(this);