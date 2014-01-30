(function() {
require(['jquery', 'bootstrap', 'dataTables'], function($, bootstrap, datatables) {
	var rowCb = function( nRow, aData, iDisplayIndex ) {
		var timeformat = dateFormat(new Date(aData[0]));
		var firsttd = $('td:eq(0)', nRow)
		firsttd.html('<span class="label label-default">'+timeformat+'</span>');
		return nRow;
	};
	var dateFormat = function(d) {
		var time = d.toTimeString().split(' ')[0];
		return d.toLocaleDateString()+" "+time;
	};

	$(document).ready(function() {
		oTable = $('#eventtable').dataTable({
			bProcessing: true,
			bServerSide: true,
			fnRowCallback: rowCb,
			sAjaxSource: SOURCEROOT+"?format=dlist",
			aoColumns: [{ sClass: "date", sName: "start_date"}, // the first column is invisible
			            { sClass: "text", sName: "duration"},
			            { sClass: "text", sName: "title"}
			           ],
		});
		$('#eventtable_length').addClass('pull-left');
		$('#eventtable_filter').addClass('pull-right');
		$('#eventtable_info').addClass('pull-left');
		$('#eventtable_paginate').addClass('pull-right');
		$('.paginate_disabled_previous').html('<button><span class="glyphicon glyphicon-arrow-left" disabled="disabled" /></button>');
		$('.paginate_enabled_previous').html('<button><span class="glyphicon glyphicon-arrow-left"/></button>');
		$('.paginate_disabled_next').html('<button><span class="glyphicon glyphicon-arrow-right" disabled="disabled"/></button>');
		$('.paginate_enabled_next').html('<button><span class="glyphicon glyphicon-arrow-right"/></button>');
	});
});
}).call(this);