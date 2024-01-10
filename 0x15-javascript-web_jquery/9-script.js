$(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (hi) {
      $('#hello').text(hi.hello);
    }
  });
});
