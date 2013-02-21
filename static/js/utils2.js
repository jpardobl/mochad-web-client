function init_progress(){
    var z = $("#menu")
    $("#prog").remove()
    $("#avisos").remove()
    z.append("<div id='prog' class=\"progress\"><div id=\"progress\" class=\"bar\" data-percentage=\"0%\" style=\"width: 0%;\"></div></div>")
    delete z;
}

function progress(p){


    $("#progress").css( "width", p + "%")
}

function drop_progress(){

    setTimeout("$('#prog').fadeOut('slow')", 800)

}

function show_msg(msg, type){
    if(type == undefined) type = "error"
    var z = $("#menu")

    $("#avisos").remove()
    z.append("<div style='display:none' class='alert alert-"+type+"' id='avisos'><button type='button' class='close' data-dismiss='alert'>&times;</button>" + msg + "</div>")
    $("#avisos").fadeToggle('slow')
    $('#avisos').bind('closed', function () {
            $("#avisos").remove()
        })
    delete z
}

function load_url(selector, url, data){
    init_progress();
    $.ajax({
        url: url,
        data: data,
        beforeSend: function(){progress(30)},
        success: function(data){progress(60);$(selector).html(data);progress(90)},
        complete: function(){$("[title!=undefined]").tooltip({"animation": "true"});progress(100)},
        error: function(ob){show_msg(ob.responseText)}
        });
   drop_progress();

}

function send_url(url, fun, data){
   init_progress();
   $.ajax({
    url: url,
    data: data,
    beforeSend: function(){progress(30)},
    success: fun,
    complete: function(){$("[title!=undefined]").tooltip({"animation": "true"});progress(100)},
    error: function(ob){show_msg(ob.responseText)}
   });

   drop_progress();
}



