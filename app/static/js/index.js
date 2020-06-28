$(document).ready(function () {
    $("#up").hide();
    $("#start").click(function () {
        $('html, body').animate({
            scrollTop: $("#toolslide").offset().top
        }, 2000
        );
        $("#up").show(3000);
    });
    $("#up").click(function () {
        $('html, body').animate({
            scrollTop: -$("#toolslide").offset().top
        }, 2000
        );
        $("#up").hide(3000);
    });
});