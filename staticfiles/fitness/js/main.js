

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Init AOS (Animate On Scroll) ---------- */
  if (window.AOS) {
    AOS.init({ duration: 800, once: true, offset: 80, easing: 'ease-out-cubic' });
  }

  const themeBtn = document.getElementById('themeToggleBtn');
  const body = document.body;
  const THEME_KEY = 'ironcore-theme';

  function applyTheme(theme) {
    if (theme === 'light') {
      body.classList.add('light-mode');
      if (themeBtn) themeBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
    } else {
      body.classList.remove('light-mode');
      if (themeBtn) themeBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
    }
  }

  const savedTheme = localStorage.getItem(THEME_KEY) || 'dark';
  applyTheme(savedTheme);

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      const isLight = body.classList.contains('light-mode');
      const newTheme = isLight ? 'dark' : 'light';
      applyTheme(newTheme);
      localStorage.setItem(THEME_KEY, newTheme);
    });
  }

  const navbar = document.getElementById('mainNavbar');
  const progressBar = document.getElementById('scrollProgressBar');
  const scrollTopBtn = document.getElementById('scrollTopBtn');

  function onScroll() {
    const scrollY = window.scrollY || document.documentElement.scrollTop;

    if (navbar) {
      if (scrollY > 60) navbar.classList.add('scrolled');
      else navbar.classList.remove('scrolled');
    }
    if (progressBar) {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
      progressBar.style.width = pct + '%';
    }
    if (scrollTopBtn) {
      if (scrollY > 400) scrollTopBtn.classList.add('show');
      else scrollTopBtn.classList.remove('show');
    }
  }
  window.addEventListener('scroll', onScroll);
  onScroll();

  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const navbarContent = document.getElementById('navbarContent');
  if (mobileMenuBtn && navbarContent && window.bootstrap) {
    mobileMenuBtn.addEventListener('click', function () {
      const collapseInstance = bootstrap.Collapse.getOrCreateInstance(navbarContent);
      collapseInstance.toggle();
    });
    // Swap icon based on open/close state
    navbarContent.addEventListener('show.bs.collapse', () => {
      mobileMenuBtn.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    });
    navbarContent.addEventListener('hide.bs.collapse', () => {
      mobileMenuBtn.innerHTML = '<i class="fa-solid fa-bars"></i>';
    });
  }

  const searchInput = document.getElementById('navSearchInput');
  const searchResults = document.getElementById('navSearchResults');

  if (searchInput && searchResults && window.SITE_PAGES) {
    searchInput.addEventListener('input', function () {
      const q = this.value.trim().toLowerCase();
      searchResults.innerHTML = '';
      if (!q) { searchResults.classList.remove('show'); return; }

      const matches = window.SITE_PAGES.filter(p => p.title.toLowerCase().includes(q));
      if (matches.length === 0) {
        searchResults.innerHTML = '<div class="no-result">No pages found</div>';
      } else {
        matches.slice(0, 6).forEach(p => {
          const a = document.createElement('a');
          a.href = p.url;
          a.textContent = p.title;
          searchResults.appendChild(a);
        });
      }
      searchResults.classList.add('show');
    });

    document.addEventListener('click', function (e) {
      if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
        searchResults.classList.remove('show');
      }
    });
  }

  const counters = document.querySelectorAll('.counter-num');
  if (counters.length) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(c => counterObserver.observe(c));
  }

  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-count'), 10) || 0;
    const suffix = el.getAttribute('data-suffix') || '';
    const duration = 1600;
    const startTime = performance.now();

    function tick(now) {
      const progress = Math.min((now - startTime) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
      else el.textContent = target + suffix;
    }
    requestAnimationFrame(tick);
  }

  const skillFills = document.querySelectorAll('.skill-bar .fill');
  if (skillFills.length) {
    const barObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = entry.target.getAttribute('data-width') || '0%';
          entry.target.style.width = target;
          barObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    skillFills.forEach(f => barObserver.observe(f));
  }
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    if (!question || !answer) return;

    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Close all others (single-open accordion)
      faqItems.forEach(other => {
        other.classList.remove('open');
        const otherAnswer = other.querySelector('.faq-answer');
        if (otherAnswer) otherAnswer.style.maxHeight = null;
      });

      if (!isOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  const sliderTrack = document.querySelector('.slider-track');
  if (sliderTrack) {
    const slides = sliderTrack.children;
    const dotsWrap = document.querySelector('.slider-dots');
    let slideIndex = 0;
    let slidesPerView = window.innerWidth < 768 ? 1 : (window.innerWidth < 1200 ? 2 : 3);
    const totalGroups = Math.max(1, slides.length - slidesPerView + 1);

    function buildDots() {
      if (!dotsWrap) return;
      dotsWrap.innerHTML = '';
      for (let i = 0; i < totalGroups; i++) {
        const dot = document.createElement('div');
        dot.className = 'dot' + (i === 0 ? ' active' : '');
        dot.addEventListener('click', () => goToSlide(i));
        dotsWrap.appendChild(dot);
      }
    }

    function goToSlide(i) {
      slideIndex = i;
      const slideWidth = slides[0].getBoundingClientRect().width;
      const gap = 24;
      sliderTrack.style.transform = `translateX(-${i * (slideWidth + gap)}px)`;
      if (dotsWrap) {
        [...dotsWrap.children].forEach((d, idx) => d.classList.toggle('active', idx === i));
      }
    }

    buildDots();

    let autoSlide = setInterval(() => {
      slideIndex = (slideIndex + 1) % totalGroups;
      goToSlide(slideIndex);
    }, 4500);

    sliderTrack.addEventListener('mouseenter', () => clearInterval(autoSlide));
    sliderTrack.addEventListener('mouseleave', () => {
      autoSlide = setInterval(() => {
        slideIndex = (slideIndex + 1) % totalGroups;
        goToSlide(slideIndex);
      }, 4500);
    });
  }

  const filterBtns = document.querySelectorAll('.filter-btn');
  const filterItems = document.querySelectorAll('[data-category]');
  if (filterBtns.length && filterItems.length) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-filter');

        filterItems.forEach(item => {
          const cats = (item.getAttribute('data-category') || '').split(' ');
          const show = filter === 'all' || cats.includes(filter);
          item.style.display = show ? '' : 'none';
        });
      });
    });
  }

  const validatedForms = document.querySelectorAll('.needs-validation-custom');
  validatedForms.forEach(form => {
    form.addEventListener('submit', function (event) {

      const fields = form.querySelectorAll('[data-validate]');
      fields.forEach(field => {
        const rule = field.getAttribute('data-validate');
        const value = field.value.trim();
        let fieldValid = true;

        if (rule.includes('required') && value === '') fieldValid = false;
        if (rule.includes('email') && value !== '') {
          const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRe.test(value)) fieldValid = false;
        }
        if (rule.includes('min6') && value.length < 6) fieldValid = false;
        if (rule.includes('phone') && value !== '') {
          const phoneRe = /^[0-9+\-\s()]{7,}$/;
          if (!phoneRe.test(value)) fieldValid = false;
        }
        if (rule.includes('match')) {
          const matchTarget = document.getElementById(field.getAttribute('data-match-id'));
          if (matchTarget && matchTarget.value !== value) fieldValid = false;
        }

        const feedback = field.parentElement.querySelector('.invalid-feedback-custom');
        if (!fieldValid) {
          valid = false;
          field.classList.add('is-invalid');
          field.classList.remove('is-valid');
          if (feedback) feedback.style.display = 'block';
        } else {
          field.classList.remove('is-invalid');
          field.classList.add('is-valid');
          if (feedback) feedback.style.display = 'none';
        }
      });

      const successBox = form.querySelector('.form-success-msg');
      if (valid) {
        // if (successBox) successBox.style.display = 'block';
        // form.reset();
        fields.forEach(f => f.classList.remove('is-valid'));
      } else {
        if (successBox) successBox.style.display = 'none';
      }
    });
  });

});
