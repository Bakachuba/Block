document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const button = document.querySelector('button');

    form.addEventListener('submit', function (event) {
        button.classList.add('submitting');

        setTimeout(function() {
            button.classList.remove('submitting');
        }, 1000);
    });
});