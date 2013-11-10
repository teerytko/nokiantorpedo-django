(function() {
define(['jquery'], function($) {
	var modal_id = '#editModal';
	var show_editors = function(event) {
		$editors = $(this).find('.editors');
		$editors.show(100);
	}
	var hide_editors = function(event) {
		$editors = $(this).find('.editors');
		$editors.hide(200);
	}
	var edit = function(event) {
		$.ajax($(this).attr('data-url')).
		done(function(data) {
			$('.modal-body').empty();
			$('.modal-body').append(data);
			// Show the footer close / save when there is now submit button 
			var submit = $('input[type="submit"]');
			console.log(submit);
			if ( submit.length > 0 ) {
				$('.modal-footer').hide();
			}
			else {
				$('.modal-footer').show();
			}
			$(modal_id).modal({show: true});
		});
	}
	var edit_save = function(event) {
		var action = $(modal_id).find('form').attr('action');
		var datas = {};
		$('input').each(function(index, value) {
			if (value.type != 'submit') {
				datas[value.name] = value.value;
			}
		});
		$('select').each(function(index, value) {
			opts = [];
			for (var i=0; i<value.length; i++) {
				if (value[i].selected)
					opts.push(value[i].value);
			}
			datas[value.name] =  opts;
		});
		console.log(datas);
		$.ajax({
			url: action,
			type: "POST",
			data: datas,
			traditional: true
		}).
		done(function(data) {
			retq = $(data);
			$('.modal-body').empty();
			if (retq.attr('id') == 'profile-form') {
				$('.modal-body').append(data);
			}
			else {
				$(modal_id).modal('hide')
				// reload the page to get the changes
				window.location.reload();
			}
		}).
		fail(function(data) {
			$('.modal-body').empty();
			$('.modal-body').append(data.responseText);
			
		});
		
	}

	return {
		show_editors: show_editors,
		hide_editors: hide_editors,
		edit: edit,
		edit_save: edit_save,
	}
});
}).call(this);