/***** Settings for JSHINT.COM, including variables created before calling this script file */
/* jshint esversion: 8 */
/* global timeoutUrl, stripePublicKey, clientSecret, bootstrap, Stripe */

$(document).ready(function () {

    /***** STRIPE and payment functions *****/

    // Sleep function found at https://www.sitepoint.com/delay-sleep-pause-wait/
    // Used to display information modal at least four seconds
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Set up STRIPE card

    const stripe = Stripe(stripePublicKey);
    const elements = stripe.elements();
    const card = elements.create('card');
    card.mount('#card-element');
    const form = $('#payment-form');

    form.on('submit', async function (event) {
        event.preventDefault();

        //Disable submit button and show wait modal
        $('#submitbutton').prop("disabled", true);
        const pleaseWaitModal = new bootstrap.Modal(document.getElementById('pleaseWaitModal'));
        pleaseWaitModal.show();

        // How to measure time taken for a function found at https://stackoverflow.com/questions/313893/how-to-measure-time-taken-by-a-function-to-execute
        const startTime = performance.now();

        // Get data to attach to card or cache view
        const cardholderName = $('#id_cardholder_name').val();
        const email = $('#userEmail').val();
        var registrationId = $('#registrationId').val();
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        var postData = {
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'client_secret': clientSecret,
            'registration_id': registrationId,
        };
        var url = '/events/cache_registration_data/';
        try {
            // Use await for AJAX call
            await $.ajax({
                type: 'POST',
                url: url,
                data: postData,
            });

            // Confirm card payment
            const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: cardholderName,
                        email: email,
                    }
                }
            });

            const endTime = performance.now();
            const timeTaken = endTime - startTime;
            const timeRemaining = 4000 - timeTaken;

            // If wait modal hasn't been shown long enough
            if (timeRemaining > 0) {
                await sleep(timeRemaining);
            }

            if (error) {
                pleaseWaitModal.hide();
                $('#card-errors').text(error.message);
                $('#submitbutton').prop("disabled", false);
            } else if (paymentIntent.status === 'succeeded') {
                form[0].submit();
            }

        } catch (err) {
            console.log(err);
            //location.reload();  // fallback error handler
        }
    });

    /***** Countdown timer ******/

    /* Countdown script found at https://www.w3schools.com/howto/howto_js_countdown.asp Modified to suit project */

    // Create event handler for modal close button
    $('#modalTimeoutCloseButton').click(function () {
        window.location.href = timeoutUrl;
    });

    const time_in_minutes = 5; // The time to countdown
    var distance = time_in_minutes * 60; //Calculate time in seconds

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

