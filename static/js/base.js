/***** Settings for JSHINT.COM, including variables created before calling this script file */
/* jshint esversion: 8 */
/* global bootstrap */

/** Loop through and initiate all toasts after document has loaded **/

$(document).ready(function () {
    $(".toast").each(function () {
        const toast = new bootstrap.Toast(this);
        toast.show();
    });
});
