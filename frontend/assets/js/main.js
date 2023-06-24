(function ($) {
  "use strict";

  $(window).stellar({
    responsive: true,
    parallaxBackgrounds: true,
    parallaxElements: true,
    horizontalScrolling: false,
    hideDistantElements: false,
    scrollProperty: "scroll",
  });

  var fullHeight = function () {
    $(".js-fullheight").css("height", $(window).height());
    $(window).resize(function () {
      $(".js-fullheight").css("height", $(window).height());
    });
  };
  fullHeight();

  // loader
  var loader = function () {
    setTimeout(function () {
      if ($("#ftco-loader").length > 0) {
        $("#ftco-loader").removeClass("show");
      }
    }, 1);
  };
  loader();

  var carousel = function () {
    $(".carousel-testimony").owlCarousel({
      center: false,
      loop: true,
      items: 1,
      margin: 30,
      stagePadding: 0,
      nav: false,
      navText: [
        '<span class="ion-ios-arrow-back">',
        '<span class="ion-ios-arrow-forward">',
      ],
      responsive: {
        0: {
          items: 1,
        },
        600: {
          items: 2,
        },
        1000: {
          items: 3,
        },
      },
    });
  };
  // carousel();

  new Swiper(".slides-1", {
    speed: 200,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  /**
   * Init swiper slider with 2 slides at once in desktop view
   */
  new Swiper(".slides-2", {
    speed: 200,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20,
      },

      1200: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
    },
  });

  $("nav .dropdown").hover(
    function () {
      var $this = $(this);
      // 	 timer;
      // clearTimeout(timer);
      $this.addClass("show");
      $this.find("> a").attr("aria-expanded", true);
      // $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
      $this.find(".dropdown-menu").addClass("show");
    },
    function () {
      var $this = $(this);
      // timer;
      // timer = setTimeout(function(){
      $this.removeClass("show");
      $this.find("> a").attr("aria-expanded", false);
      // $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
      $this.find(".dropdown-menu").removeClass("show");
      // }, 100);
    }
  );

  $("#dropdown04").on("show.bs.dropdown", function () {
    console.log("show");
  });

  // magnific popup
  $(".image-popup").magnificPopup({
    type: "image",
    closeOnContentClick: true,
    closeBtnInside: false,
    fixedContentPos: true,
    mainClass: "mfp-no-margins mfp-with-zoom", // class to remove default margin from left and right side
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1], // Will preload 0 - before current, and 1 after the current image
    },
    image: {
      verticalFit: true,
    },
    zoom: {
      enabled: true,
      duration: 300, // don't foget to change the duration also in CSS
    },
  });

  $(".popup-youtube, .popup-vimeo, .popup-gmaps").magnificPopup({
    disableOn: 700,
    type: "iframe",
    mainClass: "mfp-fade",
    removalDelay: 160,
    preloader: false,

    fixedContentPos: false,
  });

  var counter = function () {
    $("#section-counter").waypoint(
      function (direction) {
        if (
          direction === "down" &&
          !$(this.element).hasClass("ftco-animated")
        ) {
          var comma_separator_number_step =
            $.animateNumber.numberStepFactories.separator(",");
          $(".number").each(function () {
            var $this = $(this),
              num = $this.data("number");
            console.log(num);
            $this.animateNumber(
              {
                number: num,
                numberStep: comma_separator_number_step,
              },
              7000
            );
          });
        }
      },
      { offset: "95%" }
    );
  };
  counter();

  var contentWayPoint = function () {
    var i = 0;
    $(".ftco-animate").waypoint(
      function (direction) {
        if (
          direction === "down" &&
          !$(this.element).hasClass("ftco-animated")
        ) {
          i++;

          $(this.element).addClass("item-animate");
          setTimeout(function () {
            $("body .ftco-animate.item-animate").each(function (k) {
              var el = $(this);
              setTimeout(
                function () {
                  var effect = el.data("animate-effect");
                  if (effect === "fadeIn") {
                    el.addClass("fadeIn ftco-animated");
                  } else if (effect === "fadeInLeft") {
                    el.addClass("fadeInLeft ftco-animated");
                  } else if (effect === "fadeInRight") {
                    el.addClass("fadeInRight ftco-animated");
                  } else {
                    el.addClass("fadeInUp ftco-animated");
                  }
                  el.removeClass("item-animate");
                },
                k * 50,
                "easeInOutExpo"
              );
            });
          }, 100);
        }
      },
      { offset: "95%" }
    );
  };
  contentWayPoint();

  function getCookie(name) {
	const cookieValue = document.cookie.match(
	  "(^|;)\\s*" + name + "\\s*=\\s*([^;]+)"
	);
	return cookieValue ? cookieValue.pop() : "";
  }
  
  const contactForm = document.getElementById("contactForm");
  const contactBtn = document.getElementById("contactBtn");
  const quoteBtn = document.getElementById("quoteBtn");
  const quoteForm = document.getElementById("quoteForm");
  const loadingMessage = document.querySelector(".loading");
  
  console.log(quoteBtn);

var newUrl = window.location.href;
var url = new URL(newUrl);
var endpoint = url.pathname;
// console.log(endpoint);
console.log(endpoint, 'endpont');
  if (endpoint === "/contact"){

	contactBtn.addEventListener("click", function (event) {
		event.preventDefault(); // Prevent form submission
		loadingMessage.style.display = "block";
		const formData = new FormData(contactForm);
		fetch("/contact_form", {
		  method: "POST",
		  headers: {
			"X-CSRFToken": getCookie("csrftoken"), // Get the CSRF token from cookies
		  },
		  body: formData,
		})
		  .then((response) => {
			if (response.ok) {
			  // Request was successful
			  return response.json();
			} else {
			  // Request failed
			  throw new Error("Error: " + response.status);
			}
		  })
		  .then((data) => {
			// Handle the response data
			console.log(data);
			if (data.success) {
			  // Form submission was successful
			  // Do something with the data
			  const successMessage = document.querySelector(".sent-message");
			  successMessage.style.display = "block";
			  contactForm.reset();
			  
			} else {
			  // Form submission failed
			  // Handle the error
			  const errorMessage = document.querySelector(".error-message");
			  errorMessage.textContent = data.error;
			  errorMessage.style.display = "block";
			  console.error(data.error);
			}
		  })
		  .catch((error) => {
			// Handle any errors
			console.error(error);
		  })
		  .finally(() => {
			// Hide the loading message
			loadingMessage.style.display = "none";
		  });
	  });
  }
  else{
	quoteBtn.addEventListener("click", function (event) {
		console.log('hey clicker');
		event.preventDefault(); // Prevent form submission
		loadingMessage.style.display = "block";
		console.log(quoteForm, 'hey');
		const formData = new FormData(quoteForm);
		fetch("/quote_form", {
		  method: "POST",
		  headers: {
			"X-CSRFToken": getCookie("csrftoken"), // Get the CSRF token from cookies
		  },
		  body: formData,
		})
		  .then((response) => {
			if (response.ok) {
			  // Request was successful
			  return response.json();
			} else {
			  // Request failed
			  throw new Error("Error: " + response.status);
			}
		  })
		  .then((data) => {
			// Handle the response data
			console.log(data);
			if (data.success) {
			  // Form submission was successful
			  // Do something with the data
			  const successMessage = document.querySelector(".sent-message");
			  successMessage.style.display = "block";
			  contactForm.reset();
			  
			} else {
			  // Form submission failed
			  // Handle the error
			  const errorMessage = document.querySelector(".error-message");
			  errorMessage.textContent = data.error;
			  errorMessage.style.display = "block";
			  console.error(data.error);
			}
		  })
		  .catch((error) => {
			// Handle any errors
			console.error(error);
		  })
		  .finally(() => {
			// Hide the loading message
			loadingMessage.style.display = "none";
		  });
	  });
  }

  
  
})(jQuery);
