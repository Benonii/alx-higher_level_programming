$(function() {
	$('#add_item').on('click', function() {
		let item = $("<li></li>").text("Item");
		$('.my_list').append(item);
	});
});
