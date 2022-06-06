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

// helper function - used to generate random index for search 
function random(mn, mx) {
  return Math.random() * (mx - mn) + mn;
}

// makes call to backend API 
$(document).ready(function() {
  $('form').submit(function (e) {
      let url = '/api/get-restaurant'; // send the form data here.
      $.ajax({
          type: "POST",
          url: url,
          data: $('form').serialize(), // serializes the form's elements.
          success: function (data) {
              // console.log(data)  // display the returned data in the console.
              handleResponse(data)
          }
      });
      e.preventDefault(); // block the traditional submission of the form.
  });


// Handles object returned and accesses values
function handleResponse(data) {
  // console.log(data.businesses[1].name)
  business_array = Array(data.businesses)
  random_business = business_array[0][Math.floor(random(1, 20))-1]
  console.log(random_business)
  
  $('.card-title').text(random_business.name)
  $('.card-img-top').attr('src', random_business.image_url)
  $('#restaurant-phone').text(`Phone: ${random_business.display_phone}`)
  $('#restaurant-yelp').text('Visit on Yelp').attr('href', random_business.url)
  $('#card-container').removeClass('hidden')
  }
  


  // Inject our CSRF token into our AJAX request.
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
          }
      }
  })
});