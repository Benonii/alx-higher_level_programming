$(function() {
	$('#toggle_header').on('click', function() {
		if ($('#toggle_header').hasClass("red")) {
		    $('#toggle_header').toggleClass("green");
		} else if ($('#toggle_header').hasClass("green")) {
		    $('#toggle_header').toggleClass("red");
		} else {
		    $('#toggle_header').addClass("red");
		}
	});
});
