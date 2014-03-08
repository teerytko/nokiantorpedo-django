/*
 * Jutils - generic utils for salibandy
 *
 * Copyright (c) 2011 Teemu Rytk�nen
 *
 *
 */

var STATIC_TABLE_LEN = 15;

function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
}

function two_decimal(number) {
    if (number < 10)
        return "0"+number;
    else
        return number;
}

function format_date(date) {
    var year = date.getFullYear();
    var month = date.getMonth()+1;
    var day = date.getDate();
    var hour = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    
	return year+"-"+two_decimal(month)+"-"+two_decimal(day)+
	" "+two_decimal(hour)+":"+two_decimal(minutes)+":"+two_decimal(seconds);
}

function add_datarow(oTable, resource, data) {
    $.post(SOURCEROOT+resource, data, function(ret, obj) {
        console.log(ret, obj);
    	oTable.fnDraw();
    });
}

function delete_datarow(oTable, resource, sId) {
	$.ajax({
		url: SOURCEROOT+resource+'/'+sId+'/', 
		type: 'delete',
		success: function() {
			oTable.fnDraw();
		},
	});
}

/* Get the rows which are currently selected */
function fnGetSelected( oTableLocal ) {
    var aReturn = new Array();
    var aTrs = oTableLocal.fnGetNodes();

    for ( var i=0 ; i<aTrs.length ; i++ ) {
        if ( $(aTrs[i]).hasClass('row_selected') ) {
            aReturn.push( aTrs[i] );
        }
    }
    return aReturn;
}

function add_static_data(oTable, aStaticData) {
    var datalength = oTable.fnGetData().length;
    var collength = oTable.fnSettings().aoColumns.length;
    if (datalength < STATIC_TABLE_LEN) {
        var dummyrow = [];
        for (j=0; j<collength; j++) {
            dummyrow.push('**');
        }
        for (i=datalength+aStaticData.length; i<STATIC_TABLE_LEN; i++) {
            aStaticData.push(dummyrow);
        }
        oTable.fnAddData(aStaticData);
    }
}

(function($) {
    var defaults = {
        height: "12px",
    };
    $.fn.create_edit = function(options) {
        var empty = {}
        var options = $.extend(true, empty, defaults, options);
        if (!options.sUpdateMethod) {
            options.sUpdateMethod = 'PUT';
        }
        this.each( function() {
            obj = $(this);
            poss = options.oTable.fnGetPosition(this)
            objid = options.oTable.fnGetData(poss[0])[0]
            var cols = options.oTable.fnSettings().aoColumns;
            var aPos = options.oTable.fnGetPosition( this );
            var colname = cols[aPos[2]].sName;
            obj.editable(options.sUpdateUrl+'/'+objid+'/', {
                tooltip: 'Click to edit..',
                method: options.sUpdateMethod,
                name: colname,
                id: '',
                ajaxoptions: {dataType: 'text'},
                callback: function( sValue, y ) {
                    var aPos = options.oTable.fnGetPosition( this );
                    options.oTable.fnUpdate( '-', aPos[0], aPos[1] );
                    callbackFnk = options.callback;
                    if(typeof callbackFnk == 'function') {
                        callbackFnk.call(this, options);
                    }
                },
                height: options.height,
                placeholder : "-",
                onerror: function (settings, original, xhr) {  
                    alert(xhr);
                    original.reset();
                },
            }
            );
        });
    }
    $.fn.create_select_edit = function(options) {
        var empty = {}
        var options = $.extend(true, empty, defaults, options);
        if (!options.sUpdateMethod) {
            options.sUpdateMethod = 'PUT';
        }
        this.each( function() {
            obj = $(this);
            objid = options.oTable.fnGetData(options.oTable.fnGetPosition(this)[0])[0]
            var colname = '';
            var cols = options.oTable.fnSettings().aoColumns;
            var aPos = options.oTable.fnGetPosition( this );
            colname = cols[aPos[2]].sName;
            if (options.sUpdateFieldReplace != null) 
            {
                colname = colname.replace(options.sUpdateFieldReplace.from,
                                          options.sUpdateFieldReplace.to);
            }
            obj.editable(options.sUpdateUrl+'/'+objid+'/', {
                callback: function( sValue, y ) {
                    var aPos = options.oTable.fnGetPosition( this );
                    options.oTable.fnUpdate( '-', aPos[0], aPos[1] );
                    callbackFnk = options.callback;
                    if(typeof callbackFnk == 'function') {
                        callbackFnk.call(this, options);
                    }
                },
                name: colname,
                id: '',
                ajaxoptions: {dataType: 'text'},
                loadurl : options.sLoadUrl,
                height: options.height,
                placeholder : "-",
                type   : "select",
                submit : "OK",
                style   : 'display: inline',
                method: options.sUpdateMethod,
                onerror: function (settings, original, xhr) {  
                    alert(xhr   );  
                    original.reset();  
                }
            });
        });
    }
})(jQuery);