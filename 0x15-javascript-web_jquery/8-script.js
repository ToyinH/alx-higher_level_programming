$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      const films = data.results;
      $.each(films, function(index, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>')
      })      
    }
  });
});
