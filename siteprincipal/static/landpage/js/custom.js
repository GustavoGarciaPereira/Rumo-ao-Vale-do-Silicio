jQuery(document).ready(function ($) {

    "use strict";


    // Sticky Navigation
    $("#sticky-nav").sticky({topSpacing: 0});

    // Smooth scroll 
    var $root = $('html, body');
    $('a').on('click', function () {
        $root.animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 1200, 'easeInOutCubic');
        return false;
    });


});


