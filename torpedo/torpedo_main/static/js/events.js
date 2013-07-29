(function() {
require(['jquery', 'jfeed'], function($, jfeed) {
	var MAXEVENTS=5;
	var update_events = function(maxevents) {
		$.getFeed({
			url: '/events/feed/',
			success: function(feed) {
				var title = '<h3>' + feed.title + '</h3>';
				$('#eventsfeed').append(title);
				for (i=0; i<feed.items.length && i<maxevents; i++)
				{
					var post_id = 'eventsfeed_post_'+i
					$('<div/>', {
						id: post_id,
					}).appendTo('#eventsfeed');
					var item = feed.items[i];
					var description = ''+item.description;
					var link = '<a href="'+item.link+'" title="'+item.title+' '+description+'">'+item.title+'</a></br>';
					$('#'+post_id).append(link);
					// $('#'+post_id).append('<p/>');
					//$('#'+post_id+' p').append(description);
				}
			}
		});
	}
	
	$(document).ready(update_events(MAXEVENTS));

});
}).call(this);