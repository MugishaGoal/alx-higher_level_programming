$(document).ready(function(){
    // Handle click event on DIV#toggle_header
    $('#toggle_header').click(function(){
        // Toggle class between red and green on <header> element
        $('header').toggleClass('red green');
    });
});
