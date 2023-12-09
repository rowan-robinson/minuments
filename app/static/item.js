$(document).ready(function() {

    // get access to HTML elements
    const HTML_buyButton = document.getElementsByClassName("minument-buybutton");

    // handle AJAX for the favourite button
    $(".minument-star").on("click", function() {
        $.ajax({
            url: '/ajax_favourite',
            type: 'POST',
            // data holds id of minument-star, which holds the itemID
            data: JSON.stringify({ itemid: $(this).attr('id') }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",

            // if we get a response
            success: function(response){
                // handle what to do based on what the view responded with
                if (response.response == "favourited") {
                    $(".minument-star").attr("src","static/resources/star-filled.png");
                }
                else if (response.response == "unfavourited") {
                    $(".minument-star").attr("src","static/resources/star-unfilled.png");
                }
                else if (response.response == "needlogin") {
                    $("#login-message").attr("style","display: flex");
                }
            }
        });
    });

    // handle AJAX for the BUY NOW button
    $(".minument-buybutton").on("click", function() {
        $.ajax({
            url: '/ajax_buy',
            type: 'POST',
            // data holds id of minument-star, which holds the itemID
            data: JSON.stringify({ itemid: $(this).attr('id') }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",

            // if we get a response
            success: function(response){
                // handle what to do based on what the view responded with
                if (response.response == "buy") {
                    HTML_buyButton[0].innerHTML = "PURCHASED";
                    HTML_buyButton[0].classList.add("minument-buybutton-clicked");
                    HTML_buyButton[0].classList.remove("minument-buybutton");
                }
                else if (response.response == "needlogin") {
                    $("#login-message").attr("style","display: flex");
                }
            }
        });
    });
});