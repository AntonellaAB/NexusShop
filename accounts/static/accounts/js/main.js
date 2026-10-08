/* Carrusel del hero: navegación por flechas, puntos y scroll nativo (touch/trackpad) */
document.addEventListener('DOMContentLoaded', function () {
  const track = document.querySelector('.hero-track');
  if (!track) return;

  const slides = Array.from(track.children);
  const dotsWrap = document.querySelector('.hero-dots');
  const prevBtn = document.querySelector('.hero-arrow.prev');
  const nextBtn = document.querySelector('.hero-arrow.next');

  // Genera un punto por slide
  slides.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.setAttribute('aria-label', 'Ir a la diapositiva ' + (i + 1));
    if (i === 0) dot.classList.add('active');
    dot.addEventListener('click', () => scrollToSlide(i));
    dotsWrap.appendChild(dot);
  });
  const dots = Array.from(dotsWrap.children);

  function scrollToSlide(index) {
    track.scrollTo({ left: track.clientWidth * index, behavior: 'smooth' });
  }

  function currentIndex() {
    return Math.round(track.scrollLeft / track.clientWidth);
  }

  function updateDots() {
    const idx = currentIndex();
    dots.forEach((d, i) => d.classList.toggle('active', i === idx));
  }

  prevBtn.addEventListener('click', () => scrollToSlide(Math.max(currentIndex() - 1, 0)));
  nextBtn.addEventListener('click', () => scrollToSlide(Math.min(currentIndex() + 1, slides.length - 1)));

  let scrollTimeout;
  track.addEventListener('scroll', () => {
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(updateDots, 80);
  });

  window.addEventListener('resize', () => scrollToSlide(currentIndex()));
});
