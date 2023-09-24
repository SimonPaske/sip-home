console.log('remove_from_cart.js loaded');

function updateOrder(productId, action) {
    console.log('User is authenticated, sending data...');
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
        console.log('data:', data);
        location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function handleButtonClick(button, actionMessage, successMessage) {
    button.addEventListener('click', function () {
        console.log(`${actionMessage} clicked`);
        const productId = this.dataset.product;
        const action = this.dataset.action;
        console.log('productId:', productId, 'action:', action);

        console.log('USER NAME:', user);

        if (user === 'AnonymousUser') {
            console.log('Not logged in');
        } else {
            updateOrder(productId, action);
            console.log('User is logged in, sending data...');
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
        console.log('userForm:', userForm);
    });
}

function handleFormSubmission() {
    const form = document.getElementById('shipping-info');
    const submitButton = document.getElementById('submit-button');
    const paymentButton = document.getElementById('make-payment-button');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        console.log('Form submitted');

        submitButton.addEventListener('click', function () {
            console.log('clicked');
        });

        submitButton.classList.add('hidden');
        form.classList.add('hidden');
        paymentButton.classList.remove('hidden');
    });

    paymentButton.addEventListener('click', function () {
        console.log('Make Payment button clicked');
    });
}
