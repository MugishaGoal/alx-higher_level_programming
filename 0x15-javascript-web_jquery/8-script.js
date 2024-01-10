$(document).ready(function(){
    // Fetch data from the URL using jQuery AJAX
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET',
        success: function(data) {
            // Loop through the movies and append titles to the <ul> with id 'list_movies'
            $.each(data.results, function(index, movie) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        },
        error: function(error) {
            // Handle errors, for example, display an error message
            $('#list_movies').append('<li>Error fetching movies</li>');
        }
    });
});
