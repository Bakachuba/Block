$(document).ready(function () {
    // Check if dark mode is enabled in cookies
    var isDarkMode = getCookie('dark-mode') === 'enabled';

    // Toggle the 'dark-mode' class and enable/disable the styles based on the cookie
    $('body').toggleClass('dark-mode', isDarkMode);
    $('#dark-mode-styles').attr('disabled', !isDarkMode);

    // Toggle dark mode on button click
    $('#toggle-dark-mode').click(function () {
        // Toggle the 'dark-mode' class on the body
        $('body').toggleClass('dark-mode');

        // Toggle the 'disabled' attribute on the dark-mode-styles link
        var isDarkModeEnabled = $('body').hasClass('dark-mode');
        $('#dark-mode-styles').attr('disabled', !isDarkModeEnabled);

        // Save the dark mode state in a cookie
        setCookie('dark-mode', isDarkModeEnabled ? 'enabled' : 'disabled', 365);

        // Toggle the visibility of the button
        $('#toggle-dark-mode').toggleClass('hidden', !isDarkModeEnabled);
    });

    // Function to set a cookie
    function setCookie(name, value, days) {
        var expires = '';
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = '; expires=' + date.toUTCString();
        }
        document.cookie = name + '=' + value + expires + '; path=/';
    }

    // Function to get a cookie
    function getCookie(name) {
        var nameEQ = name + '=';
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }
});