$(function () {
  $('#add_item').on('click', function () {
    const item = $('<li></li>').text('Item');
    $('.my_list').append(item);
  });
});
