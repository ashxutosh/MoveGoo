document.addEventListener('DOMContentLoaded', () => {
    // Main booking widget tabs
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    if (tabButtons.length > 0 && tabContents.length > 0) {
        tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                tabButtons.forEach(btn => btn.classList.remove('active'));
                tabContents.forEach(content => content.classList.remove('active'));
                button.classList.add('active');
                
                const targetContent = document.getElementById(button.dataset.tab);
                if (targetContent) {
                    targetContent.classList.add('active');
                }
            });
        });
    }

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

    // Testimonial Scroller
    const scrollContainer = document.getElementById('testimonials-grid');
    const scrollLeftBtn = document.getElementById('scroll-left');
    const scrollRightBtn = document.getElementById('scroll-right');

    if (scrollContainer && scrollLeftBtn && scrollRightBtn) {
        scrollLeftBtn.addEventListener('click', () => {
            const card = scrollContainer.querySelector('.testimonial-card');
            if (card) {
                const cardWidth = card.offsetWidth;
                scrollContainer.scrollLeft -= (cardWidth + 32); // card width + gap
            }
        });

        scrollRightBtn.addEventListener('click', () => {
            const card = scrollContainer.querySelector('.testimonial-card');
            if (card) {
                const cardWidth = card.offsetWidth;
                scrollContainer.scrollLeft += (cardWidth + 32); // card width + gap
            }
        });
    }
});
