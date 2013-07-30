(function() {
require(['jquery', 'jfeed'], function($, jfeed) {
	var maxitems=6;
	var get_datetime = function(dstr) {
		// replace possible ending Z
		dstr = dstr.replace(/Z$/, '');
		var dtime = new Date(Date.parse(dstr, 'yyyy-MM-ddTHH:mm:ss'));
		return dtime.toString();
	}
	var get_title = function(item) {
		var title = item.title.split('::');
		return title[title.length-1].trim()
	}
	var feeds = function($div, titleurl, feedurl) {
		jQuery.getFeed({
			url:  feedurl,
			success: function(feed) {
				var $title = $('<a>' + feed.title + '</a>');
				$title.attr('href', titleurl)
				$div.append($title);
				for (i=0; i<feed.items.length && i<maxitems; i++)
				{
					var post_id = 'newsfeed_post_'+i
					var $feednode = $('<blockquote/>', {
						id: post_id,
					});
					var item = feed.items[i];
					var dstr = item.updated.split('+')[0]
					var updated = ' '+get_datetime(dstr);
					var title = get_title(item);
					var link = '<a href="'+item.link+'" title="'+updated+' '+item.title+'">'+item.title+'</a></br>';
					var description = ''+item.description.substring(0, 80)+'</br>';
					$feednode.append(link);
					$feednode.append('<p>'+description+'</p>');
					$div.append($feednode)
				}
			}
		});
	}

	$(document).ready(function() {
		if (typeof(leftfeed) !== 'undefined')
			feeds($("#leftfeeds"), leftfeed.titleurl, leftfeed.feedurl);
		if (typeof(rightfeed) !== 'undefined')
			feeds($("#rightfeeds"), rightfeed.titleurl, rightfeed.feedurl);
	});
});
}).call(this);