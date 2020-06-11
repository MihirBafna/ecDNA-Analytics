$("#disabled").click(function () {
    alert("Upload image folder first before visualizing")
});
$(".custom-file-input").on("change", function () {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html("Folder Uploaded");
    $(".selected").css("color", "rgb(0,0,0,0.3)");
});