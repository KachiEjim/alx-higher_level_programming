$(document).ready(function() {
    $("#btn_translate").click(function() {
        const languageCode = $("#language_code").val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

        $.ajax({
            url: apiUrl,
            method: 'GET',
            success: function(data) {
                $("#hello").text(data.hello);
            },
        });
    });
});