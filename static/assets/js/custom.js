


// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

function toggleDropdown() {
    var dropdown = document.getElementById("ingredientsDropdown");
    dropdown.classList.toggle("show");
  }

function showMoreIngredients() {
    var additionalIngredients = document.getElementById("additionalIngredients");
    additionalIngredients.classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.nav-link dropdown-toggle')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
  
      var additionalIngredients = document.getElementById("additionalIngredients");
      if (additionalIngredients.classList.contains('show')) {
        additionalIngredients.classList.remove('show');
      }
    }
  }




// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
  loop: true,
  margin: 0,
  dots: false,
  nav: true,
  navText: [],
  autoplay: true,
  autoplayHoverPause: true,
  navText: [
      '<i class="fa fa-angle-left" aria-hidden="true"></i>',
      '<i class="fa fa-angle-right" aria-hidden="true"></i>'
  ],
  responsive: {
      0: {
          items: 1
      },
      768: {
          items: 2
      },
      1000: {
          items: 2
      }
  }
});

document.addEventListener('DOMContentLoaded', () => {
  const wishlistButtons = document.querySelectorAll('.wishlist-btn');

  wishlistButtons.forEach(button => {
      button.addEventListener('click', () => {
          const itemId = button.dataset.itemId;
          addToWishlist(itemId);
      });
  });

  function addToWishlist(itemId) {
      // Send a POST request to your Django view to handle wishlist functionality
      fetch(`/wishlist/add/${itemId}`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': '{{ csrf_token }}', // Include CSRF token for security
          },
          body: JSON.stringify({ item_id: itemId }),
      })
      .then(response => {
          if (response.ok) {
              console.log('Item added to wishlist successfully!');
              // Optionally update UI or display a success message
          } else {
              console.error('Error adding item to wishlist:', response.statusText);
              // Optionally display an error message
          }
      })
      .catch(error => {
          console.error('Error adding item to wishlist:', error);
          // Optionally display an error message
      });
  }
});

$(document).ready(function() {
    $('.user_link').on('click', function(event) {
        event.stopPropagation(); 
        $('.user_details').toggle(); // Toggle visibility of user details
    });

    // Close user details dropdown when clicking outside
    $(document).on('click', function(event) {
        if (!$(event.target).closest('.user_option').length) {
            $('.user_details').hide(); // Hide user details if clicked outside
        }
    });
});
/*
$(document).ready(function() {
    $('.view-recipe-btn').click(function() {
        var recipeId = $(this).data('recipeId');
        var pk = parseInt(recipeId);
        debugger
        if (!isNaN(pk) && pk > 0) {
            $.ajax({
                url: '/recipe/' + pk + '/', // Update the URL to your Django view for fetching recipe details
                type: 'GET',
                success: function(response) {
                    $('#recipe-details').html(response); // Update DOM with fetched recipe details
                },
                error: function(xhr, status, error) {
                    console.error('Error fetching recipe:', error);
                }
            });
        } else {
            console.error('Invalid recipe ID:', recipeId);
        }
    });
});
*/
document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.rating-stars i');
    const ratingInput = document.getElementById('review_rating');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            const ratingValue = parseInt(star.getAttribute('data-rating'));
            ratingInput.value = ratingValue;

            stars.forEach(s => {
                if (parseInt(s.getAttribute('data-rating')) <= ratingValue) {
                    s.classList.remove('far');
                    s.classList.add('fas');
                } else {
                    s.classList.remove('fas');
                    s.classList.add('far');
                }
            });
        });
    });
});
/*
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('reviewForm');
    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form); // Get form data
        const url = form.getAttribute('action'); // Get form action URL

        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                // Optionally, handle successful form submission (e.g., display success message)
                console.log('Review submitted successfully!');
            } else {
                // Handle form submission error
                console.error('Error submitting review:', response.statusText);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
*/
/*
$(document).ready(function() {
    $('.view-recipe-btn').on('click', function() {
        var recipeId = $(this).data('recipe-id');
        debugger
        fetchRecipeDetails(recipeId);
    });
});

function fetchRecipeDetails(recipeId) {
    $.ajax({
        url: '/recipe/' + recipeId + '/', // URL to Django view for fetching recipe details
        type: 'GET',
        success: function(response) {
            $('#recipe-details').html(response); // Update DOM with fetched recipe details
        },
        error: function(xhr, status, error) {
            console.error('Error fetching recipe:', error);
        }
    });
}
*/
/*
$(document).ready(function() {
    $('.view-recipe-btn').on('click', function() {
        var recipeId = $(this).data('recipeId');
        fetchRecipeDetails(recipeId);
    });
});

function fetchRecipeDetails(recipeId) {
    debugger
    axios.get('/recipe/' + recipeId + '/')
        .then(function(response) {
            $('#recipe-details').html(response.data); // Update DOM with fetched recipe details
        })
        .catch(function(error) {
            console.error('Error fetching recipe:', error);
        });
}
*/

document.addEventListener('DOMContentLoaded', function() {
    var viewRecipeBtns = document.querySelectorAll('.view-recipe-btn');

    viewRecipeBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var recipeId = this.getAttribute('data-recipe-id');
            fetchRecipeDetails(recipeId);
        });
    });
});

function fetchRecipeDetails(recipeId) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/recipe/' + recipeId + '/', true);
debugger
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 400) {
            // Success response
            var response = xhr.responseText;
            document.getElementById('hello').innerHTML = response;
        } 
        else {
            // Error response
            console.error('Error fetching recipe:', xhr.statusText);
        }
    };

    xhr.onerror = function() {
        console.error('Error fetching recipe:', xhr.statusText);
    };

    xhr.send();
}

