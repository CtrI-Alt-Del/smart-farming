document.addEventListener('DOMContentLoaded', function() {
    function toggleButtonVisibility(checkboxId, buttonId) {
        var checkboxes = document.querySelectorAll(`#${checkboxId}`);
        var button = document.getElementById(buttonId);

        var anyChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);
        if (anyChecked) {
            button.style.display = 'inline-block';
        } else {
            button.style.display = 'none';
        }
    }

    var checkboxId = 'checkbox-table'; 
        var buttonId = 'deleteButton'; 

    toggleButtonVisibility(checkboxId, buttonId);

    var checkboxes = document.querySelectorAll(`#${checkboxId}`);
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            toggleButtonVisibility(checkboxId, buttonId);
        });
    });
});