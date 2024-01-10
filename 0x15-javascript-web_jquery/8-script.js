$(function() {
	$.ajax({
		url: "https://swapi-api.alx-tools.com/api/films/?format=json",
		method: "GET",
		dataType: "json",
		success: function(resonse) {
			const films = resonse.results;
			for (const film of films) {
				let item = $("<li></li>").text(film.title);
				$("#list_movies").append(item);
			};
		}
	});
});
