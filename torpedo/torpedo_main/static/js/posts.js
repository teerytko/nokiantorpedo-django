(function() {
require(['jquery', 'jfeed'], function($, jfeed) {
	var maxitems=6;

	var get_datetime = function(dstr) {
		// replace possible ending Z
		dstr = dstr.replace(/Z$/, '');
		var dtime = new Date(Date.parse(dstr, 'yyyy-MM-ddTHH:mm:ss'));
		return dtime.toString();
	}
	var forumposts = function () {
		jQuery.getFeed({
			url:  '/forum/feeds/posts/',
			success: function(feed) {
				var title = '<h3>' + feed.title + '</h3>';
				$('#forumfeed').append(title);
				for (i=0; i<feed.items.length && i<maxitems; i++)
				{
					var post_id = 'forumfeed_post_'+i
					jQuery('<blockquote/>', {
						id: post_id,
					}).appendTo('#forumfeed');
					var dstr = feed.updated.split('+')[0]
					var updated = ' '+get_datetime(dstr);
					var item = feed.items[i];
					var title = item.title.split('::');
					title = title[title.length-1].trim()
					var link = '<a href="'+item.link+'" title="'+updated+' '+item.title+'">'+title+'</a></br>';
					var description = item.description.substring(0, 180)+'</br>';
					$('#'+post_id).append(link);
					$('#'+post_id).append('<p/>');
					$('#'+post_id+' p').append(description);
				}
			}
		});
	}
	var feeds = function() {
		jQuery.getFeed({
			url:  '/feeds/feed/atom/',
			success: function(feed) {
				var title = '<h3><a href="/feeds/">' + feed.title + '</a></h3>';
				$('#newsfeed').append(title);
				for (i=0; i<feed.items.length && i<maxitems; i++)
				{
					var post_id = 'newsfeed_post_'+i
					jQuery('<blockquote/>', {
						id: post_id,
					}).appendTo('#newsfeed');
					var item = feed.items[i];
					var dstr = item.updated.split('+')[0]
					var updated = ' '+get_datetime(dstr);
					var title = item.title;
					var link = '<a href="'+item.link+'" title="'+updated+' '+item.title+'">'+item.title+'</a></br>';
					var description = ''+item.description.substring(0, 80)+'</br>';
					$('#'+post_id).append(link);
					$('#'+post_id).append('<p/>');
					$('#'+post_id+' p').append(description);
				}
			}
		});
	}

	$(document).ready(function() {
		forumposts();
		feeds();
	});
});
}).call(this);