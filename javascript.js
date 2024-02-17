function getValue() {
    // Get the value from the input field
  var location = document.getElementById("location").value;
  var destination = document.getElementById("destination").value;
  var mileage = document.getElementById("mileage").value;

    // Now 'userInput' contains the value entered by the user
    // You can perform actions or logic with this variable
  console.log("location: ", location);
  console.log("destination: ", destination);
  console.log("mileage:", mileage);
}