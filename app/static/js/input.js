$("#runalert").hide();

$(this).siblings(".custom-file-label").css("color", "rgb(0,0,0,0.3)");
$("#disabled").click(function () {
    alert("Upload image folder first before visualizing")
});
$(".custom-file-input").on("change", function () {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html("Folder Selected");
    $(".selected").css("color", "rgb(0,0,0,0.3)");
});
$('#firstinfo').popover({
    container: "body",
    html: true,
    title: function () {
        return $("#firstinfo").html();
    },
    content: function () {
        return '<div class="popover-message">' + $(this).data("message") + '</div>';
    }
});
$('#secondinfo').popover({
    container: "body",
    html: true,
    title: function () {
        return $("#secondinfo").html();
    },
    content: function () {
        return '<div class="popover-message">' + $(this).data("message") + '</div>';
    }
});
$('#thirdinfo').popover({
    container: "body",
    html: true,
    title: function () {
        return $("#thirdinfo").html();
    },
    content: function () {
        return '<div class="popover-message">' + $(this).data("message") + '</div>';
    }
});

$('#runecseg').click(function(){
    $("#runalert").show();
});