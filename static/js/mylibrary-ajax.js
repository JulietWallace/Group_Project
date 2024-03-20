$(document).ready(function() { 
    $('#like_btn').click(function() {
    var catecategoryIdVar;
    catecategoryIdVar = $(this).attr('data-categoryid');
    
    $.get('/mylibrary/like_category/', 
    {'category_id': catecategoryIdVar}, 
    function(data) {
        $('#like_count').html(data);
        $('#like_btn').hide();
    })
}); 
});

$(document).ready(function() { 
    $('#readButton').click(function() {
    var bookISBN;
    bookISBN = $(this).attr('data-bookISBN');
    userID=$(this).attr(data-userID);
    
    $.get('/mylibrary/read_book/', 
    {'book_ISBN': bookISBN, 'userID':userID}, 
    function() {
        $('#readButton').html("Stop Reading")
    })
}); 
});