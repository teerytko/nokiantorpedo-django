(function() {
require(['jquery', 'bootstrap', 'eventCalendar'], function($, bootstrap, ecalendar) {
	$(document).ready(function() {
		var ec = $('#eventcalendar');
		$.ajax({url: '/events/rest/event'
		}).done(function(data, textStatus, jqXHR) {
			// convert the data to eventCalendar format
			var eventdata = new Array();
			for (var d in data) {
				var event = data[d];
				if (event.start_date) {
					event.date = new Date(data[d].start_date).valueOf().toString();
					//event.url = event.link;
					eventdata.push(event);
				}
			}
			ec.eventCalendar({jsonData: eventdata});
		});
	});
});
}).call(this);