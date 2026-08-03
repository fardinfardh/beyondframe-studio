/* Beyond Frame — interactions */
(function () {
  var header = document.querySelector('.site-header');
  var onHero = header && header.classList.contains('on-hero');

  function onScroll() {
    if (!header) return;
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
      if (onHero) header.classList.remove('on-hero');
    } else {
      header.classList.remove('scrolled');
      if (onHero) header.classList.add('on-hero');
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var burger = document.querySelector('.hamburger');
  var mnav = document.querySelector('.mobile-nav');
  function toggleMenu() {
    if (!mnav) return;
    mnav.classList.toggle('open');
    document.body.classList.toggle('menu-open');
  }
  if (burger) burger.addEventListener('click', toggleMenu);
  if (mnav) {
    mnav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mnav.classList.remove('open');
        document.body.classList.remove('menu-open');
      });
    });
  }

  // Reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }
})();
