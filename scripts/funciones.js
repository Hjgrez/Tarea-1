function mostrarusuario(usuario,map,color,colors,inicio,fin) {

	var i;

	f_ini = new Date(inicio)
	f_fin = new Date(fin)
	var ruta = [];

	for (i = 0; i < usuario.checkins.length; i++) {
		date_i= new Date(usuario.checkins[i].time)
		
		if (f_ini<=date_i && f_fin>=date_i) {
		var marker;
		var lat = usuario.checkins[i].latitude
		var lon = usuario.checkins[i].longitude
		ruta[ruta.length] = new google.maps.LatLng(lat, lon)

		marker = new google.maps.Marker({
		        position: new google.maps.LatLng(lat, lon),
		        map: map,
		        icon: "icons/" + colors[color] + ".png"
		      });
		marker.setMap(map);
		i += 1	      
		};
	};
	var movimiento = new google.maps.Polyline({
    	path: ruta,
   		geodesic: true,
    	strokeColor: "#"+colors[color],
    	strokeOpacity: 1.0,
    	strokeWeight: 2
  });

 movimiento.setMap(map);

return map
}
function mostraramigos(usuario,map,colors,amigos,inicio,fin) {
	var color = 0
	mostrarusuario(usuario,map,color,colors,inicio,fin)
	if (amigos=='true') {
		for (var i = 0; i < usuario.amigos.length; i++) {
		mostrarusuario(usuario.amigos[i],map,i+1,colors,inicio,fin)
	};
	}
	
}