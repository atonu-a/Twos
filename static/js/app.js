// Simple Mobile Toggle
const menuBtn = document.getElementById("menuBtn");
const mobileMenu = document.getElementById("mobileMenu");
if (menuBtn && mobileMenu) {
  menuBtn.addEventListener("click", (e) => {
    e.stopPropagation();
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

document.addEventListener("DOMContentLoaded", function () {
  const loadingButtons = document.querySelectorAll(".btn-loading");

  loadingButtons.forEach((button) => {
    const parentForm = button.closest("form");

    if (parentForm) {
      parentForm.addEventListener("submit", function (event) {
        const btnText = button.dataset.text;
        console.log(btnText);
        button.dataset.originalHtml = button.innerHTML;

        button.innerHTML = `
          <span class="loading loading-spinner loading-xs" role="status" aria-hidden="true"></span>
          ${btnText}
        `;
        button.disabled = true;
      });
    }
  });

  // --- Back Button Error Fixer ---

  window.addEventListener("pageshow", function (event) {
    if (event.persisted) {
      loadingButtons.forEach((button) => {
        if (button.dataset.originalHtml) {
          button.innerHTML = button.dataset.originalHtml;
        }
        button.disabled = false;
      });
    }
  });
});



// Password eye button
// Password Visibility Toggle Logic
document.addEventListener('click', function (e) {

    const toggleBtn = e.target.closest('.toggle-password');
    
    if (!toggleBtn) return; 

    const container = toggleBtn.closest('.relative') || toggleBtn.closest('.group');
    const input = container ? container.querySelector('input') : null;
    const icon = toggleBtn.querySelector('i');

    if (input) {
        if (input.type === 'password') {
            input.type = 'text';
            if (icon) {
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            }
        } else {
            input.type = 'password';
            if (icon) {
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        }
    }
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


// Notification toggle
document.addEventListener("DOMContentLoaded", () => {

  const notiButtons = document.querySelectorAll(".notification");
  const notiDropdown = document.getElementById("notiDropdown");


  if (notiButtons.length > 0 && notiDropdown) {

    notiButtons.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        notiDropdown.classList.toggle("hidden");
      });
    });

    document.addEventListener("click", (e) => {
      let isClickInsideButtons = false;
      notiButtons.forEach((btn) => {
        if (btn.contains(e.target)) {
          isClickInsideButtons = true;
        }
      });

      if (!notiDropdown.contains(e.target) && !isClickInsideButtons) {
        notiDropdown.classList.add("hidden");
      }
    });

    notiDropdown.addEventListener("click", (e) => {
      e.stopPropagation();
    });
  }
});

//Notification close btn
const alertMsgs = document.querySelectorAll(".django-alert")


alertMsgs.forEach((alert) => {
  const alertClose = document.querySelector(".close-alert-btn");
  alertClose.addEventListener("click", () => {
    alert.remove()
  });
});



document.querySelectorAll("input").forEach((input) => {
  if (input.type !== "submit" && input.type !== "hidden") {
    input.className =
      "w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-slate-200 focus:outline-none focus:border-indigo-500 transition placeholder-slate-700";
  }
});


// Profile picture upload
const profilePicInput = document.getElementById('profile_pic_input');
const avatarPreview = document.getElementById('avatarPreview');

if (profilePicInput && avatarPreview) {
    profilePicInput.onchange = evt => {
        const [file] = evt.target.files;
        if (file) {
            avatarPreview.src = URL.createObjectURL(file);
        }
    };
}




