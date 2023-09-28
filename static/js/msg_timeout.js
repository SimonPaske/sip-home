document.addEventListener('DOMContentLoaded', function () {
    displayDjangoMessagesWithTiming(3);

});

function displayDjangoMessagesWithTiming(durationInSeconds = 3) {
    const messages = document.querySelectorAll('.alert');

    messages.forEach(function (message) {
        const messageText = message.textContent.trim();
        const messageTag = message.classList.contains('alert-success')
            ? 'success'
            : message.classList.contains('alert-danger')
            ? 'error'
            : message.classList.contains('alert-info')
            ? 'info'
            : message.classList.contains('alert-warning')
            ? 'warning'
            : 'default';

        displayDjangoMessage(messageText, messageTag, durationInSeconds);
        message.remove();
    });
}

function displayDjangoMessage(message, tag, durationInSeconds) {
    const messagesContainer = document.querySelector('.messages');
    const messageElement = document.createElement('div');
    messageElement.classList.add('alert', `alert-${tag}`);
    messageElement.textContent = message;
    messagesContainer.appendChild(messageElement);

    setTimeout(() => {
        messageElement.remove();
    }, durationInSeconds * 3000);
}
