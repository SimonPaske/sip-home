let modal = document.getElementById("image-modal");
let modalImage = document.getElementById("modal-image");
let closeButton = document.querySelector(".close");
let lightboxTriggers = document.querySelectorAll(".lightbox-trigger");
let backButton = document.getElementById("back-button");
let mainContentContainer = document.getElementById("main-content-container");

function openModal(imageSrc) {
    modal.style.display = "block";
    modalImage.src = imageSrc;
    toggleFooter(true); 
    currentIndex = Array.from(lightboxTriggers).findIndex(trigger => trigger.src === imageSrc);
    updateButtons();
}


function closeModal() {
    modal.style.display = "none";
    toggleFooter(false); 
}

function toggleFooter(hide) {
    let footer = document.getElementById("page-footer");
    if (hide) {
        footer.classList.add("hidden");
    } else {
        footer.classList.remove("hidden");
    }
}


lightboxTriggers.forEach(trigger => {
    trigger.addEventListener("click", () => {
        openModal(trigger.src); 
    });
});

closeButton.addEventListener("click", closeModal);
backButton.addEventListener("click", closeModal);


let currentIndex = 0;

function nextImage() {
    currentIndex = (currentIndex + 1) % lightboxTriggers.length;
    openModal(lightboxTriggers[currentIndex].src);
}

function previousImage() {
    currentIndex = (currentIndex - 1 + lightboxTriggers.length) % lightboxTriggers.length;
    openModal(lightboxTriggers[currentIndex].src);
}

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

toggleMainContent(true);
