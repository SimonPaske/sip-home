let modal = document.getElementById("image-modal");
let modalImage = document.getElementById("modal-image");
let closeButton = document.querySelector(".close");
let lightboxTriggers = document.querySelectorAll(".lightbox-trigger");
let backButton = document.getElementById("back-button");
let mainContentContainer = document.getElementById("main-content-container");

// Function to open the modal
function openModal(imageSrc) {
    modal.style.display = "block";
    modalImage.src = imageSrc;
    toggleFooter(true); // Hide the footer when the modal is opened
    currentIndex = Array.from(lightboxTriggers).findIndex(trigger => trigger.src === imageSrc);
    updateButtons();
}

// Function to close the modal
function closeModal() {
    modal.style.display = "none";
    toggleFooter(false); // Show the footer when the modal is closed
}

// Function to toggle the footer's visibility
function toggleFooter(hide) {
    let footer = document.getElementById("page-footer");
    if (hide) {
        footer.classList.add("hidden");
    } else {
        footer.classList.remove("hidden");
    }
}

// Event listeners
lightboxTriggers.forEach(trigger => {
    trigger.addEventListener("click", () => {
        openModal(trigger.src); // Open the clicked image in the modal
    });
});

closeButton.addEventListener("click", closeModal);
backButton.addEventListener("click", closeModal);

// Code for buttons
let currentIndex = 0;

// Function to navigate to the next image
function nextImage() {
    currentIndex = (currentIndex + 1) % lightboxTriggers.length;
    openModal(lightboxTriggers[currentIndex].src);
}

// Function to navigate to the previous image
function previousImage() {
    currentIndex = (currentIndex - 1 + lightboxTriggers.length) % lightboxTriggers.length;
    openModal(lightboxTriggers[currentIndex].src);
}

// Function to update "Next" and "Previous" button visibility
function updateButtons() {
    let nextButton = document.getElementById("next-button");
    let prevButton = document.getElementById("prev-button");
    nextButton.style.display = currentIndex === lightboxTriggers.length - 1 ? "none" : "block";
    prevButton.style.display = currentIndex === 0 ? "none" : "block";
}

let nextButton = document.getElementById("next-button");
let prevButton = document.getElementById("prev-button");

nextButton.addEventListener("click", nextImage);
prevButton.addEventListener("click", previousImage);

// Call the toggleMainContent function to show the main content initially
toggleMainContent(true);
