var DEVELOPMENT_URL = "http://localhost:8000/proteil/";
var PRODUCTION_URL = "";
var BASE_URL = DEVELOPMENT_URL;

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

function addProteinByPdbId(btn) {
	
	var card = $(btn).parents('.card');
	var protein_id = card.attr('data-id')
	var progress = $(card.find('.progress'));

	progress.removeClass('hide');
	var progressBar = $(progress).find('.progress-bar');
	var alert = $(card.find('.alert'));

	var intervalID = window.setInterval(function () {
		var currentValue = parseInt(progressBar.attr('aria-valuenow'));
		var inc = Math.floor( (100 - currentValue) / 2);
		var newValue = currentValue + inc;

		progressBar.attr('aria-valuenow', newValue);
		progressBar.attr('style', "width: "+newValue+"%");

		if (newValue >= 99) {
			clearInterval(intervalID);
		}
	}, 1000);

	$.ajax({
        type: "POST",
        url: BASE_URL + "api/proteins/add/" + protein_id,
        dataType: "json",
        success: function(response){
        	console.log(response);

        	progressBar.attr('aria-valuenow', 100);
			progressBar.attr('style', "width: " + 100 + "%");
			clearInterval(intervalID);
			
            if(response['status'] == "success") {
        		progress.addClass('hide')
        		alert.html("Protein added to DB");
        		alert.removeClass('hide');
        		card.find('button').remove();
            } else {
             	progressBar.attr('aria-valuenow', 0);
        		progressBar.attr('style', 'width: ' + 0 + "%");
        		progress.addClass('hide');
        		alert.removeClass('alert-success').addClass('alert-danger');
        		alert.html("Error: ").append(response['error_msg']);
        		alert.removeClass('hide');
            }
        }
    }).fail(function(){
        progressBar.attr('aria-valuenow', 0);
		progressBar.attr('style', 'width: ' + 0 + "%");
		progress.addClass('hide');
		alert.removeClass('alert-success').addClass('alert-danger');
		alert.html("Error: ").append("Request failed.");
		alert.removeClass('hide');
    });
}

function addAllProteinsByPdbId() {
	$('.card').each(function(index, elem){
		var card = $(elem);
		var exists = card.attr('data-exists');
		var req_out = $("#request_output");
		var res_out = $("#response_output");

		$('#pre-blocks').removeClass("hide");
		$("#list-ids").remove();

		if (exists == "false") {
			var protein_id = card.attr('data-id');

			$.ajax({
		        type: "POST",
		        url: BASE_URL + "api/proteins/add/" + protein_id,
		        dataType: "json",
		        success: function(response) {
		        	console.log(response);

		            if(response['status'] === "success") {
		            	res_out.prepend("<p>"+(new Date()).toTimeString()+" - ADDED " + protein_id + " TO DB</p>")
		            } else {
		            	res_out.prepend('<p class="has-error"> -- Error message: '+response['error_msg']+"</p>");
		                res_out.prepend('<p class="has-error">'+(new Date()).toTimeString()+' - FAILED TO ADD '+protein_id+' TO DB</p>');
		            }
		        },
		        complete: function(response) {
		        	req_out.prepend('<p>'+(new Date()).toTimeString()+' - REQUESTED ' + protein_id + "</p>");
		        }
		    }).fail(function(){
		        res_out.prepend('<p class="has-error">'+(new Date()).toTimeString()+' - REQUEST FAILED FOR '+protein_id+'</p>');
		    });

		}
	});
}