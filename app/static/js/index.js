$(document).ready(function () {
    $("#start").click(function () {
        // console.log($("#toolslide").offset().top);
        $('html, body').animate({
            scrollTop: $("#toolslide").offset().top
        }, 2000
        );
        $(".footer").animate({ background: 'rgba(37, 193, 255, 0.6)' }, 2000);
    });
});