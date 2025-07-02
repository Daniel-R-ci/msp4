
/** Loop through and initiate all toasts after document has loaded **/

$(document).ready(function () {
    $(".toast").each(function () {
        const toast = new bootstrap.Toast(this);
        toast.show();
    });
});
