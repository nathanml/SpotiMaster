$(document).ready(function(){
	
	$("#submit").click(function(){
		var city = document.getElementById('city').value;

<<<<<<< HEAD
		const link = "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&city=" + city + "&apikey=" ticketmaster_key;
		alert(link);
		
=======
		const link = "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&city=" + city + "&apikey=zPVq2ttl6VGJAZoAMB4y9ZsNlVsvjXCH";


>>>>>>> e72ae6a8a9e6d94d369a0068a26c7027f2590ddd
		$.ajax({
			console: "suceess",
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
              	 	"<b> " + results[i]['name'] + ":  </b>" +
              	 	"<a href=" + results[i]['url'] + ">See Event Here!</a><br>" + "</div>"
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


	
	

