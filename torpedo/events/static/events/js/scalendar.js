(function() {
  define(['jquery', 'jqui'], function($, jqui) {
	$.widget( "custom.slidingcalendar", {
		// default options
		options: {
			current: new Date
		},
		// the constructor
		_create: function() {
			this.element
			.addClass( "custom-slidingcalendar")
			.disableSelection();
			var $month = $('<ul class="slidingcalendar-month"/>');
			var mdays = this.getMonthDays(this.options.current.getFullYear(),
										this.options.current.getMonth());
			for (var i=1; i<=mdays; i++)
			{
				var $day = $('<li class="slidingcalendar-day"/>');
				$day.text(i);
				$month.append($day);
			}
			this.element.append($month)
		},
		getMonthDays: function(year, month) {
			var daysOnTheMonth = 32 - new Date(year, month, 32).getDate();
			return daysOnTheMonth;
		},		
		_destroy: function() {
		},
	 
		_setOptions: function() {
			this._superApply( arguments );
		},
		_setOption: function( key, value ) {
			this._super( key, value );
		}
	});
  })
}).call(this);