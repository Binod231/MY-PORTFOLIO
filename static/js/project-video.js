// ======================
// Video Card Functionality
// ======================

function initVideoCards() {
    const videoCards = document.querySelectorAll('.small-video-card');
    
    videoCards.forEach(card => {
      const video = card.querySelector('video');
      
      // Set initial paused state
      card.classList.add('paused');
      
      // Desktop hover events
      card.addEventListener('mouseenter', () => playVideo(card));
      card.addEventListener('mouseleave', () => pauseVideo(card));
      
      // Mobile touch events
      card.addEventListener('touchstart', (e) => {
        toggleVideo(card);
        e.preventDefault();
      });
      
      // Reset when video ends
      video.addEventListener('ended', () => {
        video.currentTime = 0;
        card.classList.add('paused');
      });
    });
  }
  
  function playVideo(card) {
    const video = card.querySelector('video');
    video.play()
      .then(() => card.classList.remove('paused'))
      .catch(e => console.log("Playback error:", e));
  }
  
  function pauseVideo(card) {
    const video = card.querySelector('video');
    video.pause();
    card.classList.add('paused');
  }
  
  function toggleVideo(card) {
    const video = card.querySelector('video');
    if (video.paused) {
      playVideo(card);
    } else {
      pauseVideo(card);
    }
  }
  
  // ======================
  // Project Description Animations
  // ======================
  
  function initProjectAnimations() {
    const projectDescriptions = document.querySelectorAll('.project-description');
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate');
        } else {
          entry.target.classList.remove('animate');
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -100px 0px' // Triggers 100px before element enters view
    });
  
    projectDescriptions.forEach(desc => {
      observer.observe(desc);
    });
  }
  
// Alternative version that scrolls to next section
function initScrollButton() {
    const scrollButton = document.querySelector('.scroll-down');
    const sections = document.querySelectorAll('section'); // Or your specific sections
    
    if (scrollButton && sections.length > 0) {
      let currentSection = 0;
      
      scrollButton.addEventListener('click', () => {
        currentSection = (currentSection + 1) % sections.length;
        sections[currentSection].scrollIntoView({
          behavior: 'smooth'
        });
      });
    }
  }

  // ======================
  // Initialize Everything
  // ======================
  
  document.addEventListener('DOMContentLoaded', function() {
    initVideoCards();
    initProjectAnimations();
    initScrollButton();
  });
  
  // Add scroll event listener to handle page navigations
  window.addEventListener('scroll', function() {
    // This ensures animations retrigger after scrolling stops
    setTimeout(initProjectAnimations, 100);
  });