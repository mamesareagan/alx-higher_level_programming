$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            $.each(data.results, function(i, title) {
                $('#list_movies').append('<li>' + title.title + '</li>');
            });
        }
    });
})