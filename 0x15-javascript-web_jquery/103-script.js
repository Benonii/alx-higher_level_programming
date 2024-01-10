$(function () {
  $('#btn_translate').on('click', function () {
    const langCode = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`,
      method: 'GET',
      dataType: 'json',
      success: function (hi) {
        $('#hello').text(hi.hello);
      }
    });
  });

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      const langCode = $('#language_code').val();
      $.ajax({
        url: `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`,
        method: 'GET',
        dataType: 'json',
        success: function (hi) {
          $('#hello').text(hi.hello);
        }
      });
    }
  });
});
