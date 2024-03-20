//$(document).ready(function(){
    $("#readButton").click(function(){
        var value = $('#readButton').val()
        var stopMessage="Stop Reading"
        var startMessage="Start Reading"
        console.log(value);
            if (value == stopMessage){
                $('#readButton').html(startMessage);  //taken from stack overflow https://stackoverflow.com/questions/5580616/how-to-change-the-text-of-a-button-in-jquery
    }
            else{
                $('#readButton').html(stopMessage);
    }
            }
            
)
//})


function readBook() {
    var xhttp = new XMLHttpRequest(); 
        xhttp.onreadystatechange = readBook(); {

}}
