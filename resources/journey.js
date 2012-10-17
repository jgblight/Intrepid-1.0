var majorArr = [];
var minorArr = [];
var pathArr = [];
//var minorShow = false;
var titleDiv = document.createElement('div');
var contentDiv = document.createElement('div');
var imageDiv = document.createElement('div');
var imageElement = document.createElement('img');

	function createControl() {
		var headerText = document.createElement('div');
		headerText.id = 'header';
		headerText.innerHTML = "<img class='imagebox' src='resources/title.png' alt='Image Here' width='250'/>";
		map.controls[google.maps.ControlPosition.TOP_LEFT].push(headerText);
	  
		var controlDiv = document.createElement('div');
		controlDiv.id = 'databox';
		

		titleDiv.id = 'datatitle';
		titleDiv.innerHTML = 'Oh, Hello!';
		controlDiv.appendChild(titleDiv);
		
		contentDiv.id = 'datatext';
		contentDiv.innerHTML = "You're here early. There's nothing to see yet. <br/><br/> Check back later";
		controlDiv.appendChild(contentDiv);
		
		imageDiv.id = 'imagewrapper';
		controlDiv.appendChild(imageDiv);
		
		imageElement.setAttribute('class','imagebox');
		imageElement.setAttribute('src','resources/compass.png');
		imageElement.setAttribute('alt','Image');
		imageElement.setAttribute('rel','lightbox');
		imageDiv.appendChild(imageElement);
		
		map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(controlDiv);
		
		};

	function addMarker(lat,lng,info){
		loc = new google.maps.LatLng(lat,lng)
		
		var marker = new google.maps.Marker({	
			position: loc,
		});
		
		if (info.major == "True") {
			marker.setIcon("resources/markerrose.png");
			marker.setMap(map);
			majorArr.push(marker);
			pathArr.push(loc);
		}
		else {
			marker.setIcon("resources/markerbrown.png");
			marker.setMap(map);
			minorArr.push(marker);
		}
		addInfo(marker,info);
		
	  };
	  
	function addInfo(marker,info) {
		var infowindow = new google.maps.InfoWindow({ 
			content: info.title,
			size: new google.maps.Size(50,50)
		});
		
		google.maps.event.addListener(marker, 'click', function() {
			//infowindow.open(map,marker);
			fillDiv(info);
		});
		
		google.maps.event.addListener(marker, 'dblclick', function() {
			map.setCenter(marker.getPosition());
			map.setZoom(10);
		});
		
	  };
	  
	function fillDiv(info) {
		titleDiv.innerHTML = info.title;
		contentDiv.innerHTML = "<p class='date'> Visited: " + info.date + "</p>" + info.content;
		imageElement.setAttribute('src','img?img_id=' + info.img_id + '&tile=true');
	};
	
	function changeLastMarker() {
		if (majorArr.length > 0) {
			var last = majorArr[majorArr.length - 1];
			last.setIcon("resources/markerred.png");
			map.setCenter(last.getPosition());
			google.maps.event.trigger(last,'click')
		}
	}
	
	function drawPath() {
		poly = new google.maps.Polyline({
			path: pathArr,
			strokeColor: "#594c25",
			strokeOpacity: 1.0,
			strokeWeight: 2
		});
		poly.setMap(map);
	};
	
	//function checkZoom() {
	//	zoom = map.getZoom();
	//	if (zoom > 8 && !minorShow){
	//		minorShow = true;
	//		for (var i = 0; i < minorArr.length; i++){
	//			minorArr[i].setMap(map);
	//		}
	//	}
	//	else if (zoom <= 8 && minorShow){
	//		minorShow = false;
	//		for (var i = 0; i < minorArr.length; i++){
	//			minorArr[i].setMap(null);
	//		}
	//	}
	//};
	  

		
	 