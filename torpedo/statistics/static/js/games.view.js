(function() {
require(['jquery', 'bootstrap', 'jeditable', 'dataTables', 'jutils'], 
  function($, bootstrap, editable, dataTables, jutils) {
	var oTable;
	var rowcb = function( nRow, aData, iDisplayIndex ) {
		var alink = '<a href="game?sId=' + aData[0] + '"';
		alink += '>'+aData[1]+'</a>';
		$('td:eq(0)', nRow).html( alink );
		return nRow;
	};
	var addGame = function() {
		var now = new Date;
		add_datarow(oTable, 'game',{'date': format_date(now)});
	};

	$(document).ready(function() {
		$('#example tbody tr').each( function() {
			var sTitle;
			var nTds = $('td', this);
			var gid = $(nTds[0]).text();
			var ddate = $(nTds[1]).text();
			var sTitle = gid + " " + ddate 
			this.setAttribute( 'title', sTitle );
		});
		oTable = $('#pelit').dataTable({
			"bPaginate": false,
			"bProcessing": true,
			"bServerSide": true,
			"sAjaxSource": SOURCEROOT+"game?format=dlist",
			"fnRowCallback": rowcb,
			"aaSorting": [[1,'asc']],
			"aoColumnDefs" : [{ 'bVisible' : false, 'sName' : 'id', "aTargets" : [0] },
			                  { 'sName' : 'date', "aTargets" : [1] },
			                  { 'sName' : 'location', "aTargets" : [2] },
			                  { 'sName' : 'home__name', "aTargets" : [3] },
			                  { 'sName' : 'guest__name', "aTargets" : [4] },
			                  { 'sName' : 'home_goals', "aTargets" : [5] },
			                  { 'sName' : 'guest_goals', "aTargets" : [6] }]
		});
		$('#add-game-btn').click(addGame);
	});
  });
}).call(this);

