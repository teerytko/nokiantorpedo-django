(function() {
require(['jquery', 'bootstrap', 'jeditable', 'dataTables', 'jutils'], 
	function($, bootstrap, editable, dataTables, jutils) {
	var oTable
	var playerquery = '/statistics/0/rest/player?format=dict&key=id&value=number,name'		
	var sid = getQueryVariable("sId");
	var editMode = false;
	var playerDlg = $('#myModal');
	$(document).ready(function() {
		oTable = $('#players').dataTable( {
			bProcessing: true,
			bServerSide: true,
			bPaginate: false,
			bInfo: false,
			bFilter: false,
			sAjaxSource: SOURCEROOT+"player?format=dlist&sQuery=team=="+sid,
			aaSorting: [[2,'asc']],
			aoColumns: [{ sName: "id", bVisible: false}, // the first column is invisible
			            { bVisible: false , sName: "team_id"},
			            { sClass: "text", sName: "number"},
			            { sClass: "text", sName: "name"},
			            { sClass: "text", sName: "role"},
			            ],
			fnDrawCallback: function () {
				if (editMode == true) {
					$('td.text').create_edit({'oTable' : oTable, 
						'sUpdateUrl': SOURCEROOT+'player'});
				}
			}
		});
		/* Add a click handler to the rows - this could be used as a callback */
		$("#players tbody").click(function(event) {
			$(oTable.fnSettings().aoData).each(function (){
				$(this.nTr).removeClass('row_selected');
			});
			$(event.target.parentNode).addClass('row_selected');
		});

		/* Add a click handler for the delete row */
		$('#delete').click( function() {
			var anSelected = fnGetSelected( oTable );
			var sId = oTable.fnGetData(oTable.fnGetPosition(anSelected[0]))[0]
			delete_datarow(oTable, 'player', sId);
		});
		/* Add a click handler for the delete row */
		$('#add').click( function() {
			$.getJSON(playerquery, function(data) {
				$('#addPlayerModal').modal('show');
				$('#selectable-players').empty();
				for (key in data) {
					var player = data[key];
					var pli = $('<li>');
					var pa = $('<a class="drp-btn">');
					pa.attr('data-player', key);
					pa.text(player);
					pli.append(pa)
					$('#selectable-players').append(pli);
				}
				$('.drp-btn').click( function(e) {
					var target = e.currentTarget;
					$('#selected-player').text(target.textContent);
					$('#selected-player').attr('data-selected', target.data-player);
				});
			});
		});
		$('#dlg-add-player').click(function(e) {
			var selected = $('#selected-player').attr('data-selected');
			if (selected === 'new') {
				var number = '1';
				var name = '-';
			}
			else {
				var nn = $('#selected-player').text();
				var number = nn.split(' ')[0];
				var name = nn.replace(number+' ', '');
			}
			add_datarow(oTable, 'player', {team: sid,
				number: number,
				name: name,
				role: ''});
			$('#addPlayerModal').modal('hide');
		});
		/* Add a click handler for the delete row */
		$('#edit').click( function() {
			if (editMode == false) {
				$('#edit').html('Lopeta muokkaus')
				editMode = true
				oTable.fnDraw();
			}
			else {
				$('#edit').html('Muokkaa');
				editMode = false;
				oTable.fnDraw();    
			}
		});
	});


});
}).call(this);

