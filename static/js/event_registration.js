/* Countdown script found at 
https://www.w3schools.com/howto/howto_js_countdown.asp
Modified to suit project
*/

$(document).ready(function () {

    // Create event handler for modal close button
    $('#modalCloseButton').click(function () {
        window.location.href = timeoutUrl;
    });


    time_in_minutes = 1; // The time to countdown
    distance = time_in_minutes * 60;
    // Update the countdown every second
    var x = setInterval(function () {

        // Time calculations for minutes and seconds
        var minutes = Math.floor(distance % (60 * 60) / 60);
        var seconds = Math.floor(distance % (60));

        // Display the result in the element with id="demo"
        document.getElementById("timer").innerHTML = minutes + "m " + seconds + "s ";

        distance--;

        // If the countdown is finished, show modal
        if (distance < 0) {
            clearInterval(x);
            // Disable submit button to prevent user from clicking on it while page reloads
            $('submitbutton').prop("disabled", true);
            const timeOutModal = new bootstrap.Modal(document.getElementById('timeExpiredModal'));
            timeOutModal.show();
        }
    }, 1000);
});

