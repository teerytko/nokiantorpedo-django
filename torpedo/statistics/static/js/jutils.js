/*
 * Jutils - generic utils for salibandy
 *
 * Copyright (c) 2011 Teemu Rytk�nen
 *
 *
 */

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

function add_datarow(oTable, resource, data) {
    var datastr = ''
    if (data != null) {
        var columns = []
        var values = []

        for (var key in data) {
            columns.push(key)
            values.push(data[key])
        }
        datastr += '?fields='+columns.join()
        datastr += '&values='+values.join()
    }
    $.post('/torpedo/rest/'+resource+'/create'+datastr, function() {
        oTable.fnDraw();
    });
}

function add_data(oTable, resource, data) {
    var datastr = ''
    if (data != null) {
        var datas = []

        for (var key in data) {
            datas.push(key + '=' + data[key])
        }
        datastr = '?' + datas.join('&')
    }
    $.get('/torpedo/rest/'+resource+'/create'+datastr, function() {
        oTable.fnDraw();
    });
}

function delete_datarow(oTable, resource, sId) {
    $.post('/torpedo/rest/'+resource+'/delete/'+sId, function() {
        oTable.fnDraw();
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
            dummyrow.push('-');
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
        this.each( function() {
            obj = $(this);
            poss = options.oTable.fnGetPosition(this)
            objid = options.oTable.fnGetData(poss[0])[0]
            obj.editable(options.sPostUrl+'/'+objid, {
                tooltip   : 'Click to edit...',
                callback: function( sValue, y ) {
                    var aPos = options.oTable.fnGetPosition( this );
                    options.oTable.fnUpdate( sValue, aPos[0], aPos[1] );
                    callbackFnk = options.callback;
                    if(typeof callbackFnk == 'function') {
                        callbackFnk.call(this, options);
                    }
                },
                submitdata: function ( value, settings ) {
                    var cols = options.oTable.fnSettings().aoColumns;
                    var aPos = options.oTable.fnGetPosition( this );
                    var colname = cols[aPos[2]].sName;
                    return {
                        "field": colname,
                    };
                },
                height: options.height,
                placeholder : "-",
                onerror: function (settings, original, xhr) {  
                    var error = eval('(' + xhr.responseText + ')');
                    // This will be reverted by reset. 
                    // $('<span class="field-validation-error">' + error.Message + '</span>').appendTo($(this));  
                    alert(error.Message);  
                    original.reset();  
                },
            }
            );
        });
    }
    $.fn.create_select_edit = function(options) {
        var empty = {}
        var options = $.extend(true, empty, defaults, options);
        this.each( function() {
            obj = $(this);
            objid = options.oTable.fnGetData(options.oTable.fnGetPosition(this)[0])[0]
            obj.editable(options.sPostUrl+'/'+objid, {
                callback: function( sValue, y ) {
                    var aPos = options.oTable.fnGetPosition( this );
                    options.oTable.fnUpdate( sValue, aPos[0], aPos[1] );
                    callbackFnk = options.callback;
                    if(typeof callbackFnk == 'function') {
                        callbackFnk.call(this, options);
                    }
                },
                submitdata: function ( value, settings ) {
                    var cols = options.oTable.fnSettings().aoColumns;
                    var aPos = options.oTable.fnGetPosition( this );
                    var colname = cols[aPos[2]].sName;
                    return {
                        "field": colname,
                    };
                },
                loadurl : options.sLoadUrl,
                height: options.height,
                placeholder : "-",
                type   : "select",
                submit : "OK",
                style   : 'display: inline',
                onerror: function (settings, original, xhr) {  
                    var error = eval('(' + xhr.responseText + ')');
                    // This will be reverted by reset. 
                    // $('<span class="field-validation-error">' + error.Message + '</span>').appendTo($(this));  
                    alert(error.Message);  
                    original.reset();  
                },
            });
        });
    }
})(jQuery);