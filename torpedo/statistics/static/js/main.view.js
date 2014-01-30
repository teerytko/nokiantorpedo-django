(function() {
require(['jquery', 'bootstrap', 'jeditable', 'dataTables', 'jutils'], 
	function($, bootstrap, editable, dataTables, jutils) {
	var oTable;
	var fnRowCb = function( nRow, aData, iDisplayIndex ) {
		var alink = '<a href="player?sId=' + aData[0];
		alink += '">'+aData[1]+'</a>';
		$('td:eq(0)', nRow).html( alink );
		return nRow;
	};
	var fnServerParamCb = function ( aoData ) {
		var keep = ['sEcho', 'sSearch', 'sColumns', 
		            'iSortCol_0', 'sSortDir_0',
		            'iSortCol_1', 'sSortDir_1'];
		var i=0; 
		var dataLenght=aoData.length
		while (i<dataLenght)
		{
			var obj = aoData.shift()
			if ( keep.indexOf(obj.name) != -1 )
			{
				aoData.push( obj );
			}
			i++;
		}
	};
	$(document).ready(function() {
		oTable = $('#players').dataTable(
		{
		"bProcessing": true,
		"bServerSide": true,
		"sAjaxSource": SOURCEROOT+"/player?format=dlist",
		"fnRowCallback": fnRowCb,
		"iDisplayLength": 25,
		"aoColumnDefs" : [{ bVisible : false, "sName": "id", "aTargets": [0]},
		                  { "sName": "number", "aTargets": [1]},
		                  { "sName": "name", "aTargets": [2]},
		                  { "sName": "team_name", "aTargets": [3]},
		                  { "sName": "goals", "aTargets": [4]},
		                  { "sName": "assists", "aTargets": [5]},
		                  { "sName": "points", "aTargets": [6]},
		                  { "sName": "penalties", "aTargets": [7]},
		                  ],
		"aaSorting": [[6,'desc'],[4,'desc']],
		"oSearch": {"sSearch": "Torpedo"},
		"fnServerParams": fnServerParamCb
		});
		$('.paginate_disabled_previous').html('<span class="glyphicon glyphicon-previous" disabled="disabled">');
		$('.paginate_enabled_previous').html('<span class="glyphicon glyphicon-previous">');
		$('.paginate_disabled_next').html('<span class="glyphicon glyphicon-next" disabled="disabled">');
		$('.paginate_enabled_next').html('<span class="glyphicon glyphicon-next">');
	});
	
});
}).call(this);

