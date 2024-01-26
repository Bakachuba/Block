document.addEventListener('DOMContentLoaded', function() {
    var toggleDarkModeButton = document.getElementById('toggle-dark-mode');
    var body = document.body;

    // Проверка сохраненной темы в localStorage
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
    }

    toggleDarkModeButton.addEventListener('click', function() {
        body.classList.toggle('dark-mode');

        // Сохранение текущей темы в localStorage
        var darkModeEnabled = body.classList.contains('dark-mode');
        localStorage.setItem('darkMode', darkModeEnabled ? 'enabled' : 'disabled');
    });

    var toggleIdeaFormButton = document.getElementById('toggle-idea-form');
    var formContainer = document.getElementById('idea-form-container');

    if (toggleIdeaFormButton && formContainer) {
        toggleIdeaFormButton.addEventListener('click', function() {
            formContainer.style.display = (formContainer.style.display === 'none' || formContainer.style.display === '') ? 'block' : 'none';
        });
    }
});

document.getElementById('toggle-idea-form').addEventListener('click', function() {
    var formContainer = document.getElementById('idea-form-container');
    formContainer.style.display = (formContainer.style.display === 'none' || formContainer.style.display === '') ? 'block' : 'none';

    console.log('Button clicked, formContainer style:', formContainer.style.display);
});