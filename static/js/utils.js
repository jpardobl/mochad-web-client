function doload_dom_script(url, id){
	var d = document;
	var s = d.createElement('script');
	s.src = url;
	s.type="text/javascript";
	s.id = id
	d.getElementsByTagName('head')[0].appendChild(s);
	delete d, s;
}

function doload_dom_css(url, id){
	var d = document
	var c = d.createElement('link')
	c.href = url
	c.rel = "stylesheet"
	c.type="text/css"
	c.id = id
	d.getElementsByTagName('head')[0].appendChild(c)
	delete d, c;
}


function load_dom_script_once(url, css){


	if( css == undefined){
		id = 'js_'+url.replace(/\//g,"").replace(/_/g,"").replace(/\./g, "")
		if(window.console)console.log("script "+id+"found: " + $("#"+id).length)
		if($("#"+id).length) return;
		if(window.console)console.log("Cargamos el script/css " + url)
		doload_dom_script(url, id);
		return
	}
	id = 'css_'+url.replace(/\//g,"").replace(/_/g,"").replace(/\./g, "")
	if($("#"+id).length) return;
	if(window.console)console.log("Cargamos el script/css " + url)
	doload_dom_css(url, id)
}
