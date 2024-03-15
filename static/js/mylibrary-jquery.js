$(document).ready(function() 
    { alert('Hello, world!');
});

$(document).ready(function() {
    $('#about-btn').click(function() {
    alert('You clicked the button using JQuery!');
    }); 
});

$("a").click(function() {
    $("p#text").css(
        {fontSize:36, color:"blue"});
});