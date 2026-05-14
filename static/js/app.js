// Simple Mobile Toggle
const menuBtn = document.getElementById("menuBtn");
const mobileMenu = document.getElementById("mobileMenu");
if (menuBtn && mobileMenu) {
  menuBtn.addEventListener("click", (e) => {
    e.stopPropagation(); // যেন নিচের window ক্লিক ইভেন্ট ট্রিগার না হয়
    mobileMenu.classList.toggle("hidden");
  });
}

//Page loader
window.addEventListener("load", () => {
  const loader = document.getElementById("loader");

  setTimeout(() => {
    loader.classList.add("loader-hidden");
  }, 300);
});

//calender toggle
const calendarBtn = document.querySelectorAll(".calendar-btn");
const crossBtn = document.getElementById("cross-btn");
const calendarContainer = document.querySelector(".calendar-container");

calendarBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    calendarContainer.classList.toggle("hidden");
  });
});

crossBtn.addEventListener("click", () => {
  calendarContainer.classList.toggle("hidden");
});




document.querySelectorAll("input").forEach((input) => {
  if (input.type !== "submit" && input.type !== "hidden") {
    input.className =
      "w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-slate-200 focus:outline-none focus:border-indigo-500 transition placeholder-slate-700";
  }
});
