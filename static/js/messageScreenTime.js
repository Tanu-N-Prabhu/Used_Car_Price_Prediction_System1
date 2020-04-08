// The name of the file is messageScreenTime.js which contains the javascript code.
// The original nav bar code was found fron the website Djangoproject.com
// Basically this file keeps the message on the screen based on the given time in this case its 2 seconds (2000)
// Source: https://docs.djangoproject.com/en/3.0/ref/contrib/messages/

setTimeout(function()
{
    if ($('#msg').length > 0) 
    {
        $('#msg').remove();
    }
}, 1000)
