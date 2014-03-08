(function() {
require(['jquery', 'bootstrap', 'jeditable', 'dataTables', 'jutils'], 
	function($, bootstrap, editable, dataTables, jutils) {
		var sid = getQueryVariable("sId");
		var hometeam;
		var hometeam_id=0;
		var guestteam;
		var guestteam_id=0;
		var gameTable;
		
		var guestPlayer;
		var homeGoal;
		var editHomeGoal = false;
		var guestGoal;
		var editGuestGoal = false;
		var homePenalty;
		var editHomePenalty = false;
		var guestPenalty;
		var editGuestPenalty = false;
		var playerquery = SOURCEROOT+'player?format=dict&key=id&value=number,name&sQuery=team__id=='
		var goalquery = SOURCEROOT+"goal?format=dlist&sQuery=game__id=="+sid+" and team__id==";
		var penaltyquery = SOURCEROOT+"penalty?format=dlist&sQuery=game__id=="+sid+" and team__id==";
		function update_data(data)
		{
			var gamedate = format_date(new Date(data[0][1]));
			var gamelocation = data[0][2];
			hometeam = data[0][3];
			if (data[0][4] != '-') { hometeam_id = data[0][4]; }
			guestteam = data[0][5];
			if (data[0][6] != '-') { guestteam_id = data[0][6]; }
			$('#game-info').html(gamedate+' '+gamelocation);
			$('#home-team-info').html('Koti: <a href="team?sId='+hometeam_id+'">'+hometeam+'</a>');
			$('#guest-team-info').html('Vieras: <a href="team?sId='+guestteam_id+'">'+guestteam+'</a>');
		};
		var gameRowCb = function (nRow, aData, iDisplayIndex) {
			var date = format_date(new Date(aData[1]));
			$('td:eq(0)', nRow).html( date );
			return nRow;
		};
		var gameDrawCb = function () {
			$('#salibandy_game td.text').create_edit({
				oTable : gameTable, 
				sUpdateUrl: SOURCEROOT+'game'});
			$('#salibandy_game td.select').create_select_edit({
				oTable : gameTable, 
				sUpdateUrl: SOURCEROOT+'game',
				sUpdateFieldReplace: {from: '__name', to: '_id'}, 
				sLoadUrl: SOURCEROOT+'team?format=dict&key=id&value=name',
			})
			data = gameTable.fnGetData()
			update_data(data);
			homeGoal.fnSettings().sAjaxSource = goalquery+hometeam_id;
			guestGoal.fnSettings().sAjaxSource = goalquery+guestteam_id;
			homePenalty.fnSettings().sAjaxSource = penaltyquery+hometeam_id;
			guestPenalty.fnSettings().sAjaxSource = penaltyquery+guestteam_id;
			homeGoal.fnDraw();
			guestGoal.fnDraw();
			homePenalty.fnDraw();
			guestPenalty.fnDraw();
		};
		var goalDrawCb = function() {
			add_static_data(homeGoal, []);
			if (editHomeGoal == true) {
				$('#homegoal td.text').create_edit({
					oTable : homeGoal, 
					sUpdateUrl: SOURCEROOT+'goal'})
				$('#homegoal td.select').create_select_edit({
					oTable : homeGoal, 
					sUpdateUrl: SOURCEROOT+'goal',
					sUpdateFieldReplace: {from: '__name', to: '_id'}, 
					sLoadUrl: playerquery+hometeam_id})
			}
		};
		var selectRow = function(event) {
			$(homeGoal.fnSettings().aoData).each(function (){
				$(this.nTr).removeClass('row_selected');
			});
			$(event.target.parentNode).addClass('row_selected');
		};
		var deleteRow = function() {
			var anSelected = fnGetSelected( homeGoal );
			var sId = homeGoal.fnGetData(homeGoal.fnGetPosition(anSelected[0]))[0]
			delete_datarow(homeGoal, 'goal', sId);
		}; 
		var addRow = function() {
			add_datarow(homeGoal, 'goal', {
				team : hometeam_id,
				game : sid,
				time : '00:00:00'});
		};
		var editRow = function() {
			if (editHomeGoal == false) {
				editHomeGoal = true
				$('#edit-homeGoal').html('Lopeta muokkaus')
				homeGoal.fnDraw();    
			}
			else {
				editHomeGoal = false;
				$('#edit-homeGoal').html('Muokkaa');
				homeGoal.fnDraw();
			}
		}
		$(document).ready(function() {
			var gameid = getQueryVariable('sId');
			var defaults = {
					"bServerSide": true,
					"bPaginate": false,
					"bInfo": false,
					"bFilter": false,
			};
		    gameTable = $('#salibandy_game').dataTable( 
		        $.extend(defaults, {
		        sAjaxSource: SOURCEROOT+"game?format=dlist&sQuery=id=="+gameid,
		        aoColumns: [ { sName: "id", bVisible: false }, // the first column is invisible
		                     { sClass: "text", sName: "date"},
		                     { sClass: "text", sName: "location"},
		                     { sClass: "select", sName: "home__name" },
		                     { bVisible: false , sName: "home__id" },
		                     { sClass: "select", sName: "guest__name"},
		                     { bVisible: false , sName: "guest__id" },
		                     { sName: "home_goals"},
		                     { sName: "guest_goals"},
		                     ],
		        fnRowCallback: gameRowCb,
		        fnDrawCallback: gameDrawCb
		        }) );
		    homeGoal = $('#homegoal').dataTable( {
		        bServerSide: true,
		        bPaginate: false,
		        bInfo: false,
		        bFilter: false,
		        sAjaxSource: goalquery+hometeam_id,
		        aaSorting: [[1,'asc']],
		        aoColumns: [ { sName: "id", bVisible: false }, // the first column is invisible
		                     { sClass: "text", sName: "time"},
		                     { sClass: "select", sName: "player__name"},
		                     { sClass: "select", sName: "assisting__name"},
		                     { sClass: "text", sName: "note"},
		                     ],
		        fnDrawCallback: goalDrawCb
		    });
		    /* Add a click handler to the rows - this could be used as a callback */
		    $("#homegoal tbody").click(selectRow);
		    /* Add a click handler for the delete row */
		    $('#delete-homeGoal').click(deleteRow);
		    /* Add a click handler for the delete row */
		    $('#add-homeGoal').click(addRow);
		    /* Add a click handler for the delete row */
		    $('#edit-homeGoal').click(editRow);
		    guestGoal = $('#guestgoal').dataTable( {
		        bServerSide: true,
		        bPaginate: false,
		        bInfo: false,
		        bFilter: false,
		        sAjaxSource: goalquery+guestteam_id,
		        aaSorting: [[1,'asc']],
		        aoColumns: [ { sName: "id", bVisible: false }, // the first column is invisible
		                     { sClass: "text", sName: "time"},
		                     { sClass: "select", sName: "player__name"},
		                     { sClass: "select", sName: "assisting__name"},
		                     { sClass: "text", sName: "note"},
		                     ],
		        fnDrawCallback: function() {
		            add_static_data(guestGoal, []);
		            if (editGuestGoal == true) {
		                $('#guestgoal td.text').create_edit(
		                      { 'oTable' : guestGoal, 
		                        'sUpdateUrl': SOURCEROOT+'goal'})
		                $('#guestgoal td.select').create_select_edit(
		                    { oTable : guestGoal, 
		                      sUpdateUrl: SOURCEROOT+'goal',
		                      sUpdateFieldReplace: {from: '__name', to: '_id'}, 
		                      sLoadUrl: playerquery+guestteam_id})
		            }
		        }
		    });
		    /* Add a click handler to the rows - this could be used as a callback */
		    $("#guestgoal tbody").click(function(event) {
		        $(guestGoal.fnSettings().aoData).each(function (){
		            $(this.nTr).removeClass('row_selected');
		        });
		        $(event.target.parentNode).addClass('row_selected');
		    });
		    /* Add a click handler for the delete row */
		    $('#delete-guestGoal').click( function() {
		        var anSelected = fnGetSelected( guestGoal );
		        var sId = guestGoal.fnGetData(guestGoal.fnGetPosition(anSelected[0]))[0]
		        delete_datarow(guestGoal, 'goal', sId);
		    } );
		    /* Add a click handler for the delete row */
		    $('#add-guestGoal').click( function() {
		        add_datarow(guestGoal, 'goal', 
		                              {'team' : guestteam_id, 
		                               'game' : sid,
		                               'time' : '00:00:00'});
		    } );
		    /* Add a click handler for the delete row */
		    $('#edit-guestGoal').click( function() {
		        if (editGuestGoal == false) {
		            editGuestGoal = true
		            $('#edit-guestGoal').html('Lopeta muokkaus')
		            guestGoal.fnDraw();    
		        }
		        else {
		            editGuestGoal = false;
		            $('#edit-guestGoal').html('Muokkaa');
		            guestGoal.fnDraw();
		        }    
		    });
		    homePenalty = $('#homepenalty').dataTable( {
		        bServerSide: true,
		        bPaginate: false,
		        bInfo: false,
		        bFilter: false,
		        sAjaxSource: penaltyquery+hometeam_id,
		        aaSorting: [[1,'asc']],
		        aoColumns: [ { sName: 'id', bVisible: false }, // the first column is invisible
		                     { sClass: "text", sName: "time"},
		                     { sClass: "text", sName: "length"},
		                     { sClass: "select", sName: "player__name"},
		                     { sClass: "text", sName: "reason"},
		                     ],
		        fnDrawCallback: function() {
		            add_static_data(homePenalty, []);
		            if (editHomePenalty == true) {
		                $('#homepenalty td.text').create_edit(
		                      { oTable : homePenalty, 
		                        sUpdateUrl: SOURCEROOT+'penalty'})
		                $('#homepenalty td.select').create_select_edit(
		                    { oTable : homePenalty, 
		                      sUpdateUrl: SOURCEROOT+'penalty',
		                      sUpdateFieldReplace: {from: '__name', to: '_id'}, 
		                      sLoadUrl: playerquery+hometeam_id})
		            }
		        }
		    });
		    /* Add a click handler to the rows - this could be used as a callback */
		    $("#homepenalty tbody").click(function(event) {
		        $(homePenalty.fnSettings().aoData).each(function (){
		            $(this.nTr).removeClass('row_selected');
		        });
		        $(event.target.parentNode).addClass('row_selected');
		    });
		    /* Add a click handler for the delete row */
		    $('#delete-homePenalty').click( function() {
		        var anSelected = fnGetSelected( homePenalty );
		        var sId = homePenalty.fnGetData(homePenalty.fnGetPosition(anSelected[0]))[0]
		        delete_datarow(homePenalty, 'penalty', sId);
		    } );
		    /* Add a click handler for the delete row */
		    $('#add-homePenalty').click( function() {
		        add_datarow(homePenalty, 'penalty', {'team' : hometeam_id,
		                                             'game' : sid,
		                                             'time' : '00:00:00',
		                                             'length' : '00:02:00'});
		    } );
		    /* Add a click handler for the delete row */
		    $('#edit-homePenalty').click( function() {
		        if (editHomePenalty == false) {
		            editHomePenalty = true
		            $('#edit-homePenalty').html('Lopeta muokkaus')
		            homePenalty.fnDraw();    
		        }
		        else {
		            editHomePenalty = false;
		            $('#edit-homePenalty').html('Muokkaa');
		            homePenalty.fnDraw();
		        }    
		    });
		
		    guestPenalty = $('#guestpenalty').dataTable( {
		        bServerSide: true,
		        bPaginate: false,
		        bInfo: false,
		        bFilter: false,
		        sAjaxSource: penaltyquery+guestteam_id,
		        aaSorting: [[1,'asc']],
		        aoColumns: [ { sName: 'id', bVisible: false }, // the first column is invisible
		                     { sClass: "text", "sName": "time"},
		                     { sClass: "text", "sName": "length"},
		                     { sClass: "select", "sName": "player__name"},
		                     { sClass: "text", "sName": "reason"},
		                     ],
		        fnDrawCallback: function() {
		            add_static_data(guestPenalty, []);
		            if (editHomePenalty == true) {
		                $('#guestpenalty td.text').create_edit(
		                      { 'oTable' : guestPenalty, 
		                        'sUpdateUrl': SOURCEROOT+'penalty',
		                        'sUpdateMethod': 'PUT'})
		                $('#guestpenalty td.select').create_select_edit(
		                    { 'oTable' : guestPenalty, 
		                      'sUpdateUrl': SOURCEROOT+'penalty',
		                      sUpdateFieldReplace: {from: '__name', to: '_id'}, 
		                      'sLoadUrl': playerquery+guestteam_id})
		            }
		        }
		    });
		    /* Add a click handler to the rows - this could be used as a callback */
		    $("#guestpenalty tbody").click(function(event) {
		        $(guestPenalty.fnSettings().aoData).each(function (){
		            $(this.nTr).removeClass('row_selected');
		        });
		        $(event.target.parentNode).addClass('row_selected');
		    });
		    /* Add a click handler for the delete row */
		    $('#delete-guestPenalty').click( function() {
		        var anSelected = fnGetSelected( guestPenalty );
		        var sId = guestPenalty.fnGetData(guestPenalty.fnGetPosition(anSelected[0]))[0]
		        delete_datarow(guestPenalty, 'penalty', sId);
		    } );
		    /* Add a click handler for the delete row */
		    $('#add-guestPenalty').click( function() {
		        add_datarow(guestPenalty, 'penalty', {'team' : guestteam_id, 
		                                              'game' : sid,
		                                              'time' : '00:00:00',
		                                              'length' : '00:02:00'});
		    } );
		    /* Add a click handler for the delete row */
		    $('#edit-guestPenalty').click( function() {
		        if (editHomePenalty == false) {
		            editHomePenalty = true
		            $('#edit-guestPenalty').html('Lopeta muokkaus')
		            guestPenalty.fnDraw();
		        }
		        else {
		            editHomePenalty = false;
		            $('#edit-guestPenalty').html('Muokkaa');
		            guestPenalty.fnDraw();
		        }    
		    });
		
		});
	
});
}).call(this);

