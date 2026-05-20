


function toggle_sidebar() {
    const menu_icon = document.getElementById('menu_icon');
    const side_bar = document.getElementById('side_bar');

    if (side_bar.classList.contains('hidden')) {
        side_bar.classList.remove('hidden');
        menu_icon.innerHTML = `
            <span class="text-white hover:text-[#57af3c]">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                     stroke-width="1.5" stroke="currentColor" class="size-10">
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="M6 18 18 6M6 6l12 12" />
                </svg>                         
            </span>`;
    } else {
        side_bar.classList.add('hidden');
        menu_icon.innerHTML = `
            <span class="text-white hover:text-[#57af3c]">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                     fill="currentColor" class="w-10 h-10">
                    <path fill-rule="evenodd"
                          d="M3 6.75A.75.75 0 0 1 3.75 6h16.5a.75.75 0 0 1 0 1.5H3.75A.75.75 0 0 1 3 6.75ZM3 12a.75.75 0 0 1 .75-.75h16.5a.75.75 0 0 1 0 1.5H3.75A.75.75 0 0 1 3 12Zm0 5.25a.75.75 0 0 1 .75-.75h16.5a.75.75 0 0 1 0 1.5H3.75a.75.75 0 0 1-.75-.75Z"
                          clip-rule="evenodd" />
                </svg>                          
            </span>`;
    }
}



function toggleSidebarDropdown(id) {
  const menu = document.getElementById(id);
  const icon = document.getElementById('icon-' + id);

  if (menu.classList.contains('hidden')) {
      menu.classList.remove('hidden');
      icon.classList.add('rotate-180');
  } else {
      menu.classList.add('hidden');
      icon.classList.remove('rotate-180');
  }
}





document.addEventListener('DOMContentLoaded', () => {
  var swiper = new Swiper(".vertical-slide-carousel", {
    loop: true,
    direction: 'vertical',
    mousewheelControl: true,
    mousewheel: {
      releaseOnEdges: true,
    },
    spaceBetween: 30,
    grabCursor: true,
    pagination: {
      el: ".vertical-slide-carousel .swiper-pagination",
      clickable: true,
    },
  });

  // Debug: Log to ensure initialization
  console.log("Vertical Swiper initialized:", swiper);
});



document.addEventListener("DOMContentLoaded", () => {
  var swiper = new Swiper(".progress-slide-carousel", {
    loop: true,
    autoplay: {
      delay: 3000, // Time (in ms) between slide changes
      disableOnInteraction: false, // Keep autoplay active even after user interaction
    },
    pagination: {
      el: ".progress-slide-carousel .swiper-pagination",
      type: "progressbar", // Progress bar pagination
    },
  });

  // Debug: Log to ensure initialization
  console.log("Progress bar carousel initialized:", swiper);
});




// This code handles the dropdown menu functionality for the "Services" and "Product" section
let activeDropdown = null;

function toggleDropdown(id) {
    const dropdown = document.getElementById(id);

    // Close any previously active dropdown
    if (activeDropdown && activeDropdown !== dropdown) {
        activeDropdown.classList.add('hidden');
    }

    // Toggle current dropdown
    dropdown.classList.toggle('hidden');

    // Set or reset activeDropdown
    activeDropdown = dropdown.classList.contains('hidden') ? null : dropdown;
}

// Close dropdown when clicking outside
document.addEventListener('click', function (event) {
    const clickedInsideDropdown = event.target.closest('.dropdown-menu'); // Use a class to mark dropdowns
    const clickedToggle = event.target.closest('.dropdown-toggle'); // Use a class to mark toggles

    if (!clickedInsideDropdown && !clickedToggle) {
        if (activeDropdown) {
            activeDropdown.classList.add('hidden');
            activeDropdown = null;
        }
    }
});


document.querySelectorAll('.portfolio-img').forEach(img => {
  img.addEventListener('click', () => {
      const enlargedImgContainer = document.getElementById('enlargedImgContainer');
      const enlargedImg = document.getElementById('enlargedImg');
      enlargedImg.src = img.src;
      enlargedImgContainer.style.display = 'flex';
  });
});















