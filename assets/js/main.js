document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Header scroll state ---------- */
  var header = document.querySelector('.site-header');
  function onScroll(){
    if(!header) return;
    if(window.scrollY > 40){ header.classList.add('scrolled'); }
    else{ header.classList.remove('scrolled'); }
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive:true });

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var mobileNav = document.querySelector('.mobile-nav');
  if(toggle && mobileNav){
    toggle.addEventListener('click', function(){
      var isOpen = toggle.classList.toggle('open');
      mobileNav.classList.toggle('open', isOpen);
      document.body.classList.toggle('nav-open', isOpen);
    });
    mobileNav.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        toggle.classList.remove('open');
        mobileNav.classList.remove('open');
        document.body.classList.remove('nav-open');
      });
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window && revealEls.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold:0.14, rootMargin:'0px 0px -60px 0px' });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('is-visible'); });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq-item').forEach(function(item){
    var q = item.querySelector('.faq-q');
    var a = item.querySelector('.faq-a');
    if(!q || !a) return;
    q.addEventListener('click', function(){
      var isOpen = item.classList.contains('open');
      item.closest('.faq-list').querySelectorAll('.faq-item.open').forEach(function(openItem){
        if(openItem !== item){
          openItem.classList.remove('open');
          openItem.querySelector('.faq-a').style.maxHeight = null;
        }
      });
      if(isOpen){
        item.classList.remove('open');
        a.style.maxHeight = null;
      } else {
        item.classList.add('open');
        a.style.maxHeight = a.scrollHeight + 'px';
      }
    });
  });

  /* ---------- Active nav link ---------- */
  var path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.main-nav a, .mobile-nav a').forEach(function(a){
    var href = a.getAttribute('href');
    if(href === path || (path === '' && href === 'index.html')){
      a.classList.add('active');
    }
  });

  /* ---------- Contact form ---------- */
  var form = document.getElementById('contact-form');
  if(form){
    var statusBox = document.getElementById('form-status');
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var original = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Sending…';
      statusBox.className = 'form-status';

      var data = Object.fromEntries(new FormData(form).entries());

      fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      })
      .then(function(res){ return res.json().then(function(json){ return { ok: res.ok, json: json }; }); })
      .then(function(result){
        if(result.ok){
          statusBox.textContent = "Thank you — your message has been sent. I'll get back to you soon.";
          statusBox.className = 'form-status show ok';
          form.reset();
        } else {
          throw new Error(result.json && result.json.error ? result.json.error : 'Something went wrong');
        }
      })
      .catch(function(){
        statusBox.textContent = "Something went wrong sending your message. Please email hello@beyondframe.studio directly.";
        statusBox.className = 'form-status show err';
      })
      .finally(function(){
        btn.disabled = false;
        btn.textContent = original;
      });
    });
  }

  /* ---------- Calendly lazy embed ---------- */
  var calShell = document.getElementById('calendly-embed');
  if(calShell){
    var url = calShell.getAttribute('data-url');
    var script = document.createElement('script');
    script.src = 'https://assets.calendly.com/assets/external/widget.js';
    script.async = true;
    script.onload = function(){
      if(window.Calendly){
        window.Calendly.initInlineWidget({
          url: url,
          parentElement: calShell,
          prefill: {},
          utm: {}
        });
        var loading = calShell.querySelector('.cal-loading');
        setTimeout(function(){ if(loading){ loading.style.display = 'none'; } }, 1200);
      }
    };
    document.body.appendChild(script);
  }
});
