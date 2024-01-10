$(document).ready(function(){
    // Handle click event on DIV#add_item
    $('#add_item').click(function(){
        // Create a new <li> element
        var newItem = $('<li></li>').text('Item');
        
        // Append the new <li> element to UL.my_list
        $('ul.my_list').append(newItem);
    });
});
