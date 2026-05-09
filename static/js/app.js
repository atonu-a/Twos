// Simple Mobile Toggle
const menuBtn = document.getElementById("menuBtn");
const mobileMenu = document.getElementById("mobileMenu");
if (menuBtn && mobileMenu) {
  menuBtn.addEventListener("click", (e) => {
    e.stopPropagation(); // যেন নিচের window ক্লিক ইভেন্ট ট্রিগার না হয়
    mobileMenu.classList.toggle("hidden");
  });
}

window.addEventListener("load", () => {
  const loader = document.getElementById("loader");

  setTimeout(() => {
    loader.classList.add("loader-hidden");
  }, 300);
});

window.toggleCalendarPopup = function () {
  const popup = document.getElementById("timePopup");
  if (popup) {
    popup.classList.toggle("hidden");
  } else {
    console.error("ID 'timePopup' was not found in the DOM.");
  }
};

window.addEventListener("click", function (e) {
  const popup = document.getElementById("timePopup");
  if (e.target === popup) {
    popup.classList.add("hidden");
  }
});
