$(document).ready(function() {
    // Make an AJAX request to the translation API
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      method: 'GET',
      dataType: 'json',
      success: function(data) {
        // Extract the translated hello from the response
        var translatedHello = data.hello;
  
        // Display the translated hello in the DIV#hello
        $('#hello').text(translatedHello);
      },
      error: function(error) {
        // Handle errors if any
        console.error('Error fetching translation:', error);
      }
    });
  });
  