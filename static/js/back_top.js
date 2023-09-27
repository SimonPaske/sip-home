let mybutton = document.getElementById("btn-back-to-top");
let timeoutId;

window.onscroll = function () {
  scrollFunction();
  clearTimeout(timeoutId);
  timeoutId = setTimeout(hideButton, 3000);
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function hideButton() {
  mybutton.style.display = "none";
}

mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
  clearTimeout(timeoutId);
  timeoutId = setTimeout(hideButton, 5000);
}
