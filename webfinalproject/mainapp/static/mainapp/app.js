const categorySelect = document.querySelector('select[name="category"]');
const anonymousCheckbox = document.querySelector('input[name="is_anonymous"]');
const locationInput = document.querySelector('input[name="location"]');
const contactInput = document.querySelector('input[name="contact_info"]');

if (categorySelect && anonymousCheckbox) {
    const updateFields = () => {
        const category = categorySelect.value;
        const isConfession = category === 'CONFESSION';
        if (isConfession) {
            anonymousCheckbox.checked = true;
        }
        if (locationInput) {
            locationInput.disabled = isConfession;
            if (isConfession) {
                locationInput.value = '';
            }
        }
        if (contactInput) {
            contactInput.disabled = isConfession;
            if (isConfession) {
                contactInput.value = '';
            }
        }
    };

    categorySelect.addEventListener('change', updateFields);
    updateFields();
}
