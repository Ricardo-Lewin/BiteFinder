let slider = document.getElementById("myRange");
let output = document.getElementById("output");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
// slider.onload = function() {
//   output.innerHTML = this.value + " " + "miles";
// }
slider.oninput = function() {
  output.innerHTML = this.value + " " + "miles";
}


$(document).ready(function() {
  $('form').submit(function (e) {
      let url = '/api/get-restaurant'; // send the form data here.
      $.ajax({
          type: "POST",
          url: url,
          data: $('form').serialize(), // serializes the form's elements.
          success: function (data) {
              console.log(data)  // display the returned data in the console.
          }
      });
      e.preventDefault(); // block the traditional submission of the form.
  });

  // Inject our CSRF token into our AJAX request.
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
          }
      }
  })
});