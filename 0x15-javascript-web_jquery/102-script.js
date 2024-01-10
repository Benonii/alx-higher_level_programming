$(function() {
	$('#btn_translate').on('click', function() {
		let lang_code = $('#language_code').val();
		$.ajax({
			url: `https://hellosalut.stefanbohacek.dev/?lang=${lang_code}`,
			method: "GET",
			dataType: "json",
			success: function(hi) {
				$("#hello").text(hi.hello);
			}
		});
	});
});
