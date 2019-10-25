$(document).ready(function(){
	
	$("#submit").click(function(){
		var city = document.getElementById('city').value;

		const link = "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&city=" + city + "&apikey=" ticketmaster_key;
		alert(link);
		
		$.ajax({
  			type:"GET",
  			url: link,
  			async:true,
  			dataType: "json",
        alert('here');
  			success: function(json) {
            	console.log(json);
            	alert("in success");
            	var results = json["_embedded"]["events"];
            	var html = "";
            	for (i=0; i<results.length; i++){
              		html += "<div class='searching-res'>" +
              		"<h3> " + results[i]['name'] + "</h3>" +
              		"<p> " + results[i]['url'] + "</p>" + "</div>"
            	}
            	document.getElementById("results").innerHTML = html;
        	},
  			error: function(xhr, status, err) {
            	// This time, we do not end up here!
            	alert("unsuccessful"); 
            	console.log(xhr);
            	console.log(status);
            	console.log(err);
    		}
		});
	});
});


	
	

