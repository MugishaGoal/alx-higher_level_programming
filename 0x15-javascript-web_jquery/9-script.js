$(document).ready(function(){
    // Fetch data from the URL using jQuery AJAX
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: function(data) {
            // Display the translation in the HTML tag with id 'hello'
            $('#hello').text(data.hello);
        },
        error: function(error) {
            // Handle errors, for example, display an error message
            $('#hello').text('Error fetching translation');
        }
    });
});
