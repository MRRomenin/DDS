const button_filter = document.getElementById('submitButton');
const dateInputStart = document.getElementById('date_picker_start');
const dateInputEnd = document.getElementById('date-picker_end');
document.addEventListener('DOMContentLoaded', function () {

        function toggleButton() {
            button_filter.disabled = !(dateInputStart.value && dateInputEnd.value);
        }

    dateInputStart.addEventListener('input', toggleButton);
    dateInputStart.addEventListener('change', toggleButton);
    dateInputEnd.addEventListener('input', toggleButton);
    dateInputEnd.addEventListener('change', toggleButton);
    toggleButton();
});
