(function() {
require(['jquery', 'bootstrap', 'jeditable', 'dataTables', 'jutils'], 
	function($, bootstrap, editable, dataTables, jutils) {
		var oTable;
		var leagueid = null;
		var rowCb = function( nRow, aData, iDisplayIndex ) {
			var alink = '<a href="team?sId=' + aData[0];
			alink += '">'+ aData[0]+' '+aData[1]+'</a>';
			$('td:eq(0)', nRow).html( alink );
			return nRow;
		};
		var drawCb = function () {
			$('td.text').create_edit({oTable: oTable, sUpdateUrl: SOURCEROOT+'team'})
		};
		var addDatarow = function() {
			add_datarow(oTable, 'team', {name: 'Empty'});
		};
		$(document).ready(function() {
			oTable = $('#teams').dataTable({
				bProcessing: true,
				bServerSide: true,
				sAjaxSource: SOURCEROOT+"team?format=dlist",
				fnRowCallback: rowCb,
				aoColumns: [{ sName: "id"}, // the first column is invisible
				            { sClass: "text", sName: "name"}
				           ],
				fnDrawCallback: drawCb
			});
			$('#add-team-btn').click(addDatarow);
		});
});
}).call(this);

