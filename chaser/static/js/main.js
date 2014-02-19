"use strict";

function runServer() {

    var keys = [38, 40, 37, 39];
    $(document).keydown(function (event) {
        console.log(event.which);
        console.log($.inArray( event.which, keys ));
        if ( $.inArray( event.which, keys ) >= 0 ) {
            $.post('/control', { key: event.which });
        }
    });
}
$(runServer, document);


function state() {
    var updateState = function(data) {
        $('#state').attr('class', data['state']);
    };
    var getState = function() {
        if($('#state')) {
            $.get('/state', updateState);
        }
    };

    setInterval(getState, 1000);
}
$(state, document);
