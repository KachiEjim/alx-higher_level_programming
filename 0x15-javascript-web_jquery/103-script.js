$(document).ready(function() {
    $("#btn_translate").click(fetchTranslation);
    
    $("#language_code").keypress(function(event) {
        if (event.which === 13) { // Check if Enter key is pressed
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        const languageCode = $("#language_code").val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

        $.ajax({
            url: apiUrl,
            method: 'GET',
            success: function(data) {
                $("#hello").text(data.hello);
            },
        });
    }
});