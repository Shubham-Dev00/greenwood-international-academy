document.addEventListener('DOMContentLoaded', function () {
    setTimeout(() => {
        const loader = document.getElementById('loading-screen');
        if (loader) loader.classList.add('hide');
    }, 1500);

    AOS.init({ duration: 900, once: true, offset: 80 });
    if (typeof GLightbox !== 'undefined') GLightbox({ selector: '.glightbox' });

    const navbar = document.querySelector('.custom-navbar');
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    function handleScroll() {
        if (window.scrollY > 30) navbar?.classList.add('scrolled');
        else navbar?.classList.remove('scrolled');

        if (window.scrollY > 500) scrollTopBtn?.classList.add('show');
        else scrollTopBtn?.classList.remove('show');
    }
    handleScroll();
    window.addEventListener('scroll', handleScroll);
    scrollTopBtn?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

    document.querySelectorAll('.counter').forEach(counter => {
        const target = parseFloat(counter.dataset.target || '0');
        let current = 0;
        const increment = target / 50;
        const animate = () => {
            current += increment;
            if (current < target) {
                counter.textContent = counter.dataset.target.includes('.') ? current.toFixed(1) : Math.floor(current);
                requestAnimationFrame(animate);
            } else {
                counter.textContent = counter.dataset.target;
            }
        };
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animate();
                    observer.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });
        observer.observe(counter);
    });

    const cookieBanner = document.getElementById('cookieBanner');
    const acceptCookies = document.getElementById('acceptCookies');
    if (localStorage.getItem('giaCookiesAccepted')) cookieBanner?.classList.add('hide');
    acceptCookies?.addEventListener('click', () => {
        localStorage.setItem('giaCookiesAccepted', 'yes');
        cookieBanner?.classList.add('hide');
    });

    const paymentOptions = document.querySelectorAll('input[name="payment_method"]');
    const cardFields = document.getElementById('cardFields');
    const upiField = document.getElementById('upiField');
    function togglePaymentFields() {
        const selected = document.querySelector('input[name="payment_method"]:checked')?.value;
        if (cardFields) cardFields.style.display = selected === 'Card' ? 'flex' : 'none';
        if (upiField) upiField.style.display = selected === 'UPI' ? 'block' : 'none';
    }
    paymentOptions.forEach(option => option.addEventListener('change', togglePaymentFields));
    togglePaymentFields();

    const feeForm = document.getElementById('feePaymentForm');
    feeForm?.addEventListener('submit', () => {
        document.getElementById('paySpinner')?.classList.remove('d-none');
        feeForm.querySelector('.btn-text')?.classList.add('me-2');
    });

    const filterButtons = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            const filter = button.dataset.filter;
            galleryItems.forEach(item => {
                item.style.display = filter === 'All' || item.dataset.category === filter ? 'block' : 'none';
            });
        });
    });

    const notifyFilterButtons = document.querySelectorAll('.notify-filter');
    const notificationCols = document.querySelectorAll('.notification-col');
    notifyFilterButtons.forEach(button => {
        button.addEventListener('click', () => {
            notifyFilterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            const filter = button.dataset.filter;
            notificationCols.forEach(col => {
                col.style.display = filter === 'All' || col.dataset.category === filter ? 'block' : 'none';
            });
        });
    });
    document.querySelectorAll('.mark-read-btn').forEach(button => {
        button.addEventListener('click', () => {
            const card = button.closest('.notification-card');
            card?.classList.remove('unread');
            card?.classList.add('read');
            button.textContent = 'Read';
        });
    });
    document.getElementById('markAllReadBtn')?.addEventListener('click', () => {
        document.querySelectorAll('.notification-card').forEach(card => card.classList.remove('unread'));
        document.querySelectorAll('.mark-read-btn').forEach(btn => btn.textContent = 'Read');
    });
    setTimeout(() => {
        const toastEl = document.getElementById('notificationToast');
        if (toastEl) new bootstrap.Toast(toastEl, { delay: 4500 }).show();
    }, 2000);

    const steps = document.querySelectorAll('.form-step');
    const nextBtn = document.getElementById('nextStepBtn');
    const prevBtn = document.getElementById('prevStepBtn');
    const submitBtn = document.getElementById('submitEnquiryBtn');
    const progressBar = document.getElementById('enquiryProgress');
    let currentStep = 1;
    function updateSteps() {
        steps.forEach(step => step.classList.toggle('active', Number(step.dataset.step) === currentStep));
        if (progressBar) {
            const percent = (currentStep / 3) * 100;
            progressBar.style.width = `${percent}%`;
            progressBar.textContent = `Step ${currentStep} of 3`;
        }
        prevBtn?.classList.toggle('d-none', currentStep === 1);
        nextBtn?.classList.toggle('d-none', currentStep === 3);
        submitBtn?.classList.toggle('d-none', currentStep !== 3);
    }
    nextBtn?.addEventListener('click', () => {
        if (currentStep < 3) currentStep += 1;
        updateSteps();
    });
    prevBtn?.addEventListener('click', () => {
        if (currentStep > 1) currentStep -= 1;
        updateSteps();
    });
    updateSteps();

    const facultyFilterButtons = document.querySelectorAll('.faculty-filter');
    const facultyCards = document.querySelectorAll('.faculty-col');
    const facultySearch = document.getElementById('facultySearch');
    let activeFacultyFilter = 'All';
    function applyFacultyFilter() {
        const keyword = facultySearch?.value?.trim().toLowerCase() || '';
        facultyCards.forEach(card => {
            const matchesDept = activeFacultyFilter === 'All' || card.dataset.department === activeFacultyFilter;
            const matchesSearch = card.dataset.name.includes(keyword);
            card.style.display = matchesDept && matchesSearch ? 'block' : 'none';
        });
    }
    facultyFilterButtons.forEach(button => {
        button.addEventListener('click', () => {
            facultyFilterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            activeFacultyFilter = button.dataset.filter;
            applyFacultyFilter();
        });
    });
    facultySearch?.addEventListener('input', applyFacultyFilter);
});
