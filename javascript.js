window.onload = function() {
    // Create a new XMLHttpRequest object
    var xhttp = new XMLHttpRequest();
  
    // Define the function to handle the response
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        // Get the dropdown menu element
        var dropdown = document.getElementById('clubs');
        
        // Set the fetched content as the innerHTML of the dropdown
        dropdown.innerHTML = this.responseText;
      }
    };
  
    // Open the file and send the request
    xhttp.open('GET', 'menu_options.html', true);
    xhttp.send();
  }