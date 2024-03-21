$(document).ready(function() { 
    $('#readButton').click(function() {
    var value = $('#readButton').html()
    var stopMessage="Stop Reading"
    var startMessage="Start Reading"
    var bookISBN;
    var userID;
    bookISBN = $(this).attr('data-book');
    userID=$(this).attr('data-userID');
    if (value == stopMessage){
        $('#readButton').html(startMessage); 
    }
    else{
        $.get('/mylibrary/user_read_book/', {'user': userID, 'bookISBN':bookISBN}, function() {
            $('#readButton').html(stopMessage);
            $('#readHeader').hide();
            alert("Book has been added to your current books");
        })
    }
}); 
});

$(document).ready(function() { 
    $('#progress').load(function() {
        var pagesRead = $(this).attr('data-book');
        var totalPages = $(this).attr('data-userID');
        var percentage = (pagesRead/totalPages)*100
        $('progress').width(percentage+'%');
    })}); 


