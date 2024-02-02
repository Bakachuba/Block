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

document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.querySelector("#theme-toggle");

    themeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark-theme");
    });
});