let slider = document.getElementById("myRange");
let output = document.getElementById("output");
output.innerHTML = `within ${slider.value} miles`; // Display the default slider value



// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = `within ${this.value} miles`;
}

// helper function - used to generate random index for search 
function randomize(mn, mx) {
  return Math.random() * (mx - mn) + mn;
}

function showCard() {
  $('.card-title').text(random_business.name)
  $('.card-img-top').attr('src', random_business.image_url)
  $('#restaurant-address').text(`${random_business.location.display_address[0]}`)
  $('#restaurant-city').text(`${random_business.location.display_address[1]}`)
  $('#restaurant-phone').text(`Phone: ${random_business.display_phone}`)
  $('#restaurant-yelp').text('Visit on Yelp').attr('href', random_business.url)
  $('#card-container').removeClass('hidden')
  }

function failCard() {
  $('.card-title').text('Not a valid Zip Code!')
  $('.card-img-top').attr('src', './images/broken-1.png')
  $('#restaurant-address').text('Please check zip code and try again!')
  $('#restaurant-city').empty()
  $('#restaurant-phone').empty()
  $('#restaurant-yelp').empty()
  $('#card-container').removeClass('hidden')
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
              console.log('successful post')
          },
          error: function (error) {
            console.log(error)
          }
      });
      e.preventDefault(); // block the traditional submission of the form.
  });


// Handles object returned and accesses values
function handleResponse(data) {
  
  business_array = Array(data.businesses)
  try{
  random_business = business_array[0][Math.floor(randomize(1, 20))-1]
  showCard()
  console.log(random_business)
  } catch(e){
    if (e instanceof TypeError) {
      failCard()
    }
  }


  
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