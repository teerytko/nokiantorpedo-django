(function() {
require(['jquery', 'bootstrap'], function($, bootstrap) {
	var show_editors = function(event) {
		$editors = $(this).find('.editors');
		$editors.show(100);
	}
	var hide_editors = function(event) {
		$editors = $(this).find('.editors');
		$editors.hide();
	}
	
	$(document).ready(function() {
		$('.memberrow').hover(show_editors, hide_editors);
		$('.editors').click(function(event) {
			console.log(this);
			$.ajax($(this).find('a').attr('data-url')).
			done(function(data) {
				$('.modal-body').empty();
				$('.modal-body').append(data);
				$('#editModal').modal({show: true});
			});
		});
		$('#editModalSave').click(function(event) {
			var action = $('#editModal').find('form').attr('action');
			var datas = {};
			$('input').each(function(index, value) {
				if (value.type != 'submit') {
					datas[value.name] = value.value;
				}
			})
			console.log(datas);
			$.post(action, datas).
			done(function(data) {
				retq = $(data);
				$('.modal-body').empty();
				if (retq.attr('id') == 'profile-form') {
					$('.modal-body').append(data);
				}
				else {
					$('#editModal').modal('hide')
					// reload the page to get the changes
					window.location.reload();
				}
			}).
			fail(function(data) {
				$('.modal-body').empty();
				$('.modal-body').append(data.responseText);
				
			});
			
		});
	});
});
}).call(this);