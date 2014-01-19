(function() {
  define(['jquery', 'jfeed'], function($, jfeed) {
	var MAXEVENTS=5;
	var update_events = function(maxevents, eventsfeed) {
		$.getFeed({
			url: eventsfeed,
			success: function(feed) {
				var title = '<div class="panel-heading"><h3>' + feed.title + '</h3></div>';
				var feedsbody = $('<div><table class="table"></table></div>');
				feedsbody.addClass("panel-body");
				$('#eventsfeed').append(title);
				$('#eventsfeed').append(feedsbody);
				var table = $('#eventsfeed').find('table');
				for (i=0; i<feed.items.length && i<maxevents; i++)
				{
					var post_id = 'eventsfeed_post_'+i;
					var post = $('<tr/>', {id: post_id});
					var item = feed.items[i];
					var description = ''+item.description;
					var datetime = item.title.split(' ').slice(0, 2);
					var datestr = datetime.join(' ')
					var title = item.title.replace(datestr, '');
					var link = '<a href="'+item.link+'" title="'+datestr+title+' '+description+'">'+datetime[0]+title+'</a></br>';
					post.append('<td>'+link+'</td>');
					table.append(post);
					
				}
			}
		});
	};
	return {
		update_events: update_events
	};
  })
}).call(this);