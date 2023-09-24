function updateOrder(productId, action) {
    const url = '/update_cart/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
    .then(response => response.json())
    .then(data => {
        location.reload();
    })
    .catch(error => {
    });
}

function handleButtonClick(button, actionMessage, successMessage) {
    button.addEventListener('click', function () {

        const productId = this.dataset.product;
        const action = this.dataset.action;

        if (user === 'AnonymousUser') {
        } else {
            updateOrder(productId, action);
            alert(successMessage);
        }
    });
}

const removeBtn = document.querySelectorAll('.remove_from_cart');
removeBtn.forEach(button => {
    handleButtonClick(button, 'remove from cart', 'Product removed from the cart.');
});

const addBtn = document.querySelectorAll('.add_to_cart');
addBtn.forEach(button => {
    handleButtonClick(button, 'add to cart', 'Product added to the cart.');
});

function submitUserForm() {
    const form = document.getElementById('shipping-info');
    const userForm = {
        'first_name': document.getElementById('first_name').value,
        'last_name': document.getElementById('last_name').value,
        'email': document.getElementById('email').value,
        'address': document.getElementById('address').value,
        'city': document.getElementById('country').value,
        'zip': document.getElementById('zip').value,
    };

    form.addEventListener('submit', function (e) {
        e.preventDefault();
    });
}

function handleFormSubmission() {
    const form = document.getElementById('shipping-info');
    const submitButton = document.getElementById('submit-button');
    const paymentButton = document.getElementById('make-payment-button');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        submitButton.addEventListener('click', function () {
        });

        submitButton.classList.add('hidden');
        form.classList.add('hidden');
        paymentButton.classList.remove('hidden');
    });

    paymentButton.addEventListener('click', function () {

    });
}
