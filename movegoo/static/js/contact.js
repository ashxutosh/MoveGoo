document.addEventListener('DOMContentLoaded', () => {
    // Hamburger menu toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    const hamburgerIcon = hamburger.querySelector('i'); // Get the icon element

    if (hamburger && navMenu && hamburgerIcon) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            
            // Toggle between bars and times (X) icon
            if (navMenu.classList.contains('active')) {
                hamburgerIcon.classList.remove('fa-bars');
                hamburgerIcon.classList.add('fa-times');
            } else {
                hamburgerIcon.classList.remove('fa-times');
                hamburgerIcon.classList.add('fa-bars');
            }
        });
    }
});
