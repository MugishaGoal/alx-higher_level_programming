$(document).ready(function(){
    // Fetch data from the URL using jQuery AJAX
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        success: function(data) {
            // Update the text of the <div> with id 'character'
            $('#character').text(data.name);
        },
        error: function(error) {
            // Handle errors, for example, display an error message
            $('#character').text('Error fetching character name');
        }
    });
});
