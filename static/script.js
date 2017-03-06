$(
    function() {
        $( "#bt1" ).click( function() {
            $.ajax({
                type: "POST",
                contentType: "application/json",
                url: "verify_answer",
                data: JSON.stringify({
                    answer: $( "#inp1").val()
                }),
                success: function( data ) {
                    $("#result").html(data);
                }

            });
        });
    }
);
