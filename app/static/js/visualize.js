$(document).ready(function () {
    var clicked = true;
    var orig = false;
    var dapi = false;
    var ecSeg = false;
    var rowwidth = $(".myrow").width();
    var dapiorigvalue = 0;
    var metaphasespreads = {};
    var clustercounter = 0;
    initialize();
    $(window).mousemove(function (event) {
        rowwidth = $(".myrow").width();
        if (!clicked) {
            if (orig) {
                initialize();
                $("#selector1").css({ "top": event.pageY + "px", "left": event.pageX + "px" });
                $("#selector2").css({ "top": event.pageY + "px", "left": event.pageX + rowwidth / 3 + "px" });
                $("#selector3").css({ "top": event.pageY + "px", "left": event.pageX + 2 * rowwidth / 3 + "px" });
                $("#selector1").show();
                $("#selector2").show();
                $("#selector3").show();
                var zerox = $("#orig").offset().left;
                var zeroy = $("#orig").offset().top;
                var x = $("#selector1").offset().left - $("#orig").offset().left + $("#selector1").width() / 2;
                var y = $("#selector1").offset().top - $("#orig").offset().top + $("#selector1").height() / 2;
                if (x < $("#selector1").width() / 2) {
                    orig = false;
                    $("#selector1").css({ "left": zerox + $("#selector1").width() / 2 + "px" });
                    $("#selector2").css({ "left": zerox + $("#selector1").width() / 2 + rowwidth / 3 + "px" });
                    $("#selector3").css({ "left": zerox + $("#selector1").width() / 2 + 2 * rowwidth / 3 + "px" });

                }
                if (x > $("#orig").width() - $("#selector1").width() / 2) {
                    orig = false;
                    $("#selector1").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 + "px" });
                    $("#selector2").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 + rowwidth / 3 + "px" });
                    $("#selector3").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 + 2 * rowwidth / 3 + "px" });

                }
                if (y < $("#selector1").height() / 2) {
                    orig = false;
                    $("#selector1").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });
                    $("#selector2").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });
                    $("#selector3").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });

                }
                if (y > $("#orig").height() - $("#selector1").height() / 2) {
                    orig = false;
                    $("#selector1").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });
                    $("#selector2").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });
                    $("#selector3").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });

                }
                showZoom(x, y);

            }
            if (dapi) {
                initialize();
                $("#selector2").css({ "top": event.pageY + "px", "left": event.pageX + "px" });
                $("#selector1").css({ "top": event.pageY + "px", "left": event.pageX - rowwidth / 3 + "px" });
                $("#selector3").css({ "top": event.pageY + "px", "left": event.pageX + rowwidth / 3 + "px" });
                $("#selector1").show();
                $("#selector2").show();
                $("#selector3").show();
                var zerox = $("#dapi").offset().left;
                var zeroy = $("#dapi").offset().top;
                var x = $("#selector2").offset().left - $("#dapi").offset().left + $("#selector2").width() / 2;
                var y = $("#selector2").offset().top - $("#dapi").offset().top + $("#selector2").height() / 2;
                showZoom(x, y);
                if (x < $("#selector1").width() / 2) {
                    dapi = false;
                    $("#selector2").css({ "left": zerox + $("#selector1").width() / 2 + "px" });
                    $("#selector1").css({ "left": zerox + $("#selector1").width() / 2 - rowwidth / 3 + "px" });
                    $("#selector3").css({ "left": zerox + $("#selector1").width() / 2 + rowwidth / 3 + "px" });

                }
                if (x > $("#orig").width() - $("#selector1").width() / 2) {
                    dapi = false;
                    $("#selector2").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 + "px" });
                    $("#selector1").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 - rowwidth / 3 + "px" });
                    $("#selector3").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 + rowwidth / 3 + "px" });

                }
                if (y < $("#selector1").height() / 2) {
                    dapi = false;
                    $("#selector2").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });
                    $("#selector1").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });
                    $("#selector3").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });
                }
                if (y > $("#orig").height() - $("#selector1").height() / 2) {
                    dapi = false;
                    $("#selector2").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });
                    $("#selector1").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });
                    $("#selector3").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });

                }
            }
            if (ecSeg) {
                initialize();
                $("#selector3").css({ "top": event.pageY + "px", "left": event.pageX + "px" });
                $("#selector1").css({ "top": event.pageY + "px", "left": event.pageX - 2 * rowwidth / 3 + "px" });
                $("#selector2").css({ "top": event.pageY + "px", "left": event.pageX - rowwidth / 3 + "px" });
                $("#selector1").show();
                $("#selector2").show();
                $("#selector3").show();
                var zerox = $("#ecSeg").offset().left;
                var zeroy = $("#ecSeg").offset().top;
                var x = $("#selector3").offset().left - $("#ecSeg").offset().left + $("#selector3").width() / 2;
                var y = $("#selector3").offset().top - $("#ecSeg").offset().top + $("#selector3").height() / 2;
                showZoom(x, y);
                if (x < $("#selector3").width() / 2) {
                    ecSeg = false;
                    $("#selector3").css({ "left": zerox + $("#selector3").width() / 2 + "px" });
                    $("#selector1").css({ "left": zerox + $("#selector3").width() / 2 - 2 * rowwidth / 3 + "px" });
                    $("#selector2").css({ "left": zerox + $("#selector3").width() / 2 - rowwidth / 3 + "px" });

                }
                if (x > $("#orig").width() - $("#selector1").width() / 2) {
                    ecSeg = false;
                    $("#selector3").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 + "px" });
                    $("#selector1").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 - 2 * rowwidth / 3 + "px" });
                    $("#selector2").css({ "left": zerox + $("#orig").width() - $("#selector1").width() / 2 - rowwidth / 3 + "px" });

                }
                if (y < $("#selector1").height() / 2) {
                    ecSeg = false;
                    $("#selector3").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });
                    $("#selector1").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });
                    $("#selector2").css({ "top": zeroy + $("#selector1").height() / 2 + "px" });

                }
                if (y > $("#orig").height() - $("#selector1").height() / 2) {
                    ecSeg = false;
                    $("#selector3").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });
                    $("#selector1").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });
                    $("#selector2").css({ "top": zeroy + $("#orig").height() - $("#selector1").height() / 2 + "px" });

                }
            }
        }

    });

    $(window).resize(function (event) {
        $(".selector").hide();
        $("#origZoom").hide();
        $("#ecSegZoom").hide();
    })

    $(window).click(function (event) {
        if (orig || dapi || ecSeg) {
            clicked = true;
            $(".selector").css({ "border-color": "red", "background-color": "rgb(255,0,0,0.5)" })

        }
        if (orig) {
            for (i = 1; i <= clustercounter; i++) {
                var key = "#cluster" + i;
                if (overlap(key, "#selector1")) {
                    console.log(key + "showing");
                }
            }
        } else {
            console.log(key + "showing");

        }
    });
    $(window).dblclick(function (event) {
        if (orig || dapi || ecSeg) {
            clicked = false;
            $(".selector").css({ "border-color": "white", "background-color": "rgb(255,255,255,0.5)" })
        }
    });


    $("#orig").mousemove(function (event) {
        orig = true;
    });
    $("#dapi").mousemove(function (event) {
        dapi = true;
    });
    $("#ecSeg").mousemove(function (event) {
        ecSeg = true;
    });

    function showZoom(x, y) {
        var left = x - ($("#selector1").width() / 2);
        var right = $("#orig").width() - (x + $("#selector1").width() / 2);
        var bottom = $("#orig").height() - (y + $("#selector1").height() / 2);
        var top = y - ($("#selector1").height() / 2);
        var xshift = $("#orig").width() / 2 - x;
        var yshift = $("#orig").height() / 2 - y;
        $("#origZoom").css({
            "overflow": "hidden",
            "clip-path": "inset(" + top + "px " + right + "px " + bottom + "px " + left + "px )",
            "-webkit-clip-path": "inset(" + top + "px " + right + "px " + bottom + "px " + left + "px )",
            "transform": "scale(10) translate(" + xshift + "px, " + yshift + "px)"
        });
        $("#ecSegZoom").css({
            "overflow": "hidden",
            "clip-path": "inset(" + top + "px " + right + "px " + bottom + "px " + left + "px )",
            "-webkit-clip-path": "inset(" + top + "px " + right + "px " + bottom + "px " + left + "px )",
            "transform": "scale(10) translate(" + xshift + "px, " + yshift + "px)"
        });

    }

    function initialize() {
        $("#origZoom").show();
        $("#ecSegZoom").show();
        $("#selector1").hide();
        $("#selector2").hide();
        $("#selector3").hide();
        var lensWidth = $("#orig").width() / 10;
        var lensHeight = $("#orig").height() / 10;
        $("#selector1").css({
            "height": lensHeight,
            "width": lensWidth
        });
        $("#selector2").css({
            "height": lensHeight,
            "width": lensWidth
        });
        $("#selector3").css({
            "height": lensHeight,
            "width": lensWidth
        });
    }

    function overlap(idOne, idTwo) {
        var objOne = $(idOne),
            objTwo = $(idTwo),
            offsetOne = objOne.offset(),
            offsetTwo = objTwo.offset(),
            topOne = offsetOne.top,
            topTwo = offsetTwo.top,
            leftOne = offsetOne.left,
            leftTwo = offsetTwo.left,
            widthOne = objOne.width(),
            widthTwo = objTwo.width(),
            heightOne = objOne.height(),
            heightTwo = objTwo.height();
        var leftTop = leftTwo > leftOne && leftTwo < leftOne + widthOne && topTwo > topOne && topTwo < topOne + heightOne, rightTop = leftTwo + widthTwo > leftOne && leftTwo + widthTwo < leftOne + widthOne && topTwo > topOne && topTwo < topOne + heightOne, leftBottom = leftTwo > leftOne && leftTwo < leftOne + widthOne && topTwo + heightTwo > topOne && topTwo + heightTwo < topOne + heightOne, rightBottom = leftTwo + widthTwo > leftOne && leftTwo + widthTwo < leftOne + widthOne && topTwo + heightTwo > topOne && topTwo + heightTwo < topOne + heightOne;
        return leftTop || rightTop || leftBottom || rightBottom;
    }

    $("#menubtn").click(function () {
        $("#mySidenav").css({
            "width": "400px"
        })
    });
    $("#closebtn").click(function () {
        $("#mySidenav").css({
            "width": "0px"
        })
    });

    $("#toolbtn").click(function () {
        $("#toolnav").css({
            "width": "100px",
        })
    });
    $("#closetoolnav").click(function () {
        $("#toolnav").css({
            "width": "0px",
        })
    });

    $("#origdapi").click(function () {
        dapiorigvalue = (dapiorigvalue + 1) % 2;
        var origpath = $('#orig').attr('src');
        var dapipath = $('#dapi').attr('src');
        if(dapiorigvalue==1){
            $("#origZoom").attr("src", dapipath);
        }else{
            $("#origZoom").attr("src", origpath);
        }
    });  

    $('[data-toggle="tooltip"]').tooltip()
    $("#alert").delay(5000).slideUp(200, function () {
        $(this).alert('close');
    });

    $(".annotate").click(function(event){
        var zoomx = event.pageX - $("#zoomed").offset().left -20;
        var zoomy = event.pageY - $("#zoomed").offset().top-55;
        var selectorx = $("#selector1").offset().left-$("#orig").offset().left;
        var selectory = $("#selector1").offset().top - $("#orig").offset().top;
        var x = Math.round(selectorx + zoomx / 10);
        var y = Math.round(selectory + zoomy / 10);
        clustercounter++;
        var key = "cluster" + clustercounter;
        var size = 5;
        metaphasespreads[key] = [x*10, y*10, size];
        console.log(metaphasespreads[key])
        showsquare(x + $("#orig").offset().left, y + $("#orig").offset().top,size);


    });

     $('#downloadMPS').click(function() {
        console.log(metaphasespreads);
        $.ajax({
          type: "POST",
          contentType: "application/json;charset=utf-8",
          url: "/downloadMetaphaseSpreads",
          traditional: "true",
          data: JSON.stringify(metaphasespreads),
          dataType: "json"
          });
    });

    function showsquare(x,y,size){
        var key = "cluster" + clustercounter;
        $("#divrow").append('<div id="'+key+'" class="selection" style="left: '+x+'px; top: '+y+'px;"></div>');

    }
});