import random
import string
from decimal import Decimal

from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone

from .data import (
    ACCREDITATIONS,
    ACHIEVEMENTS,
    ACADEMIC_LEVELS,
    ADMISSION_STEPS,
    CHART_DATA,
    CORE_VALUES,
    DEPARTMENT_CONTACTS,
    FEE_STRUCTURE,
    GALLERY_IMAGES,
    IMPORTANT_DATES,
    INFRASTRUCTURE_IMAGES,
    METRIC_SUMMARY,
    SCHOLARSHIP_POINTS,
    SUBJECT_ICONS,
    TIMELINE_EVENTS,
    VIDEO_GALLERY,
)
from .forms import ContactForm, EnquiryForm, PaymentForm
from .models import FacultyMember, LeadershipMember, NewsEvent, Notification, PaymentRecord, Testimonial


def random_code(prefix, length=8):
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def home(request):
    news_items = NewsEvent.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:3]
    principal = LeadershipMember.objects.filter(designation__icontains='Principal').first() or LeadershipMember.objects.first()
    hero_slides = [
        {
            'title': 'Empowering Learners for a Global Future',
            'subtitle': 'Where academic excellence meets character, creativity, and confidence.',
            'image': 'https://picsum.photos/seed/school1/1600/850',
        },
        {
            'title': 'A Campus Designed for Discovery',
            'subtitle': 'Modern classrooms, innovative labs, vibrant clubs, and inspiring mentors.',
            'image': 'https://picsum.photos/seed/school2/1600/850',
        },
        {
            'title': 'Admissions Open for Session 2024-25',
            'subtitle': 'Join a nurturing community committed to every child’s growth and success.',
            'image': 'https://picsum.photos/seed/school3/1600/850',
        },
    ]
    stats = [('5000+', 'Students'), ('60+', 'Teachers'), ('50+', 'Courses'), ('25', 'Years of Excellence')]
    highlights = [
        ('fa-graduation-cap', 'Academic Excellence', 'Consistently strong board results, olympiad achievements, and concept-based learning.'),
        ('fa-futbol', 'Sports Facilities', 'Professional-grade courts, track field access, coaching programmes, and wellness clubs.'),
        ('fa-microscope', 'Modern Labs', 'Hands-on STEM learning with science labs, robotics kits, and coding workstations.'),
    ]
    why_choose_us = [
        ('fa-user-group', 'Student-Centred Learning', 'Personalised mentoring and a growth mindset approach for every learner.'),
        ('fa-earth-asia', 'Global Exposure', 'Exchange programmes, language labs, and future-ready international perspectives.'),
        ('fa-brain', 'Holistic Development', 'Balanced focus on academics, emotional wellbeing, leadership, arts, and sports.'),
        ('fa-shield-halved', 'Safe & Secure Campus', 'Structured safeguarding policies, smart access, CCTV, and trained staff.'),
    ]
    upcoming_ticker = [
        '05 April - Orientation for New Parents',
        '12 April - Inter-House Debate Championship',
        '20 April - Annual Sports Trial Registrations',
        '27 April - STEM Innovation Exhibition',
    ]
    return render(request, 'website/home.html', {
        'hero_slides': hero_slides,
        'stats': stats,
        'highlights': highlights,
        'why_choose_us': why_choose_us,
        'news_items': news_items,
        'testimonials': testimonials,
        'principal': principal,
        'upcoming_ticker': upcoming_ticker,
        'achievements': ACHIEVEMENTS,
        'page_title': 'Home',
        'meta_description': 'Greenwood International Academy is a premium school website demo with academics, admissions, faculty, fees, and interactive dashboards.',
    })


def about(request):
    return render(request, 'website/about.html', {
        'timeline_events': TIMELINE_EVENTS,
        'core_values': CORE_VALUES,
        'leadership': LeadershipMember.objects.all()[:4],
        'accreditations': ACCREDITATIONS,
        'infrastructure_images': INFRASTRUCTURE_IMAGES,
        'page_title': 'About Us',
        'meta_description': 'Discover Greenwood International Academy history, mission, vision, leadership, values, and infrastructure.',
    })


def academics(request):
    return render(request, 'website/academics.html', {
        'levels': ACADEMIC_LEVELS,
        'subject_icons': SUBJECT_ICONS,
        'page_title': 'Academics',
        'meta_description': 'Explore the academic structure, curriculum framework, class levels, and subjects at Greenwood International Academy.',
    })


def gallery(request):
    return render(request, 'website/gallery.html', {
        'gallery_images': GALLERY_IMAGES,
        'video_gallery': VIDEO_GALLERY,
        'page_title': 'Gallery',
        'meta_description': 'See campus life through the Greenwood International Academy gallery of events, sports, labs, and classrooms.',
    })


def stats_dashboard(request):
    return render(request, 'website/dashboard.html', {
        'metric_summary': METRIC_SUMMARY,
        'chart_data': CHART_DATA,
        'page_title': 'School at a Glance',
        'meta_description': 'School dashboard with enrollment, academic performance, class-level distribution, and department charts.',
    })


def fees(request):
    payment_success = None
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.transaction_id = random_code('GIA')
            payment.status = 'Paid'
            payment.payment_date = timezone.now()
            payment.save()
            payment_success = payment
            messages.success(request, 'Fee payment processed successfully.')
            form = PaymentForm(initial={
                'student_name': payment.student_name,
                'roll_number': payment.roll_number,
                'class_section': payment.class_section,
                'fee_type': payment.fee_type,
                'amount': payment.amount,
                'payment_method': payment.payment_method,
            })
    else:
        form = PaymentForm(initial={
            'student_name': 'Aarav Khanna',
            'roll_number': 'GIA2024-1187',
            'class_section': 'Class 8 - C',
            'fee_type': 'Quarterly',
            'amount': Decimal('28500.00'),
            'payment_method': 'UPI',
        })
    fee_rows = []
    for class_name, tuition, transport, lab_fee, sports_fee in FEE_STRUCTURE:
        fee_rows.append({
            'class_name': class_name,
            'tuition': tuition,
            'transport': transport,
            'lab_fee': lab_fee,
            'sports_fee': sports_fee,
            'total': tuition + transport + lab_fee + sports_fee,
        })
    return render(request, 'website/fees.html', {
        'form': form,
        'fee_rows': fee_rows,
        'payment_history': PaymentRecord.objects.all()[:5],
        'scholarship_points': SCHOLARSHIP_POINTS,
        'payment_success': payment_success,
        'page_title': 'Fee Payment',
        'meta_description': 'View fee structure, make a demo online fee payment, and review receipt and payment history.',
    })


def notifications_page(request):
    return render(request, 'website/notifications.html', {
        'notifications': Notification.objects.all(),
        'page_title': 'Notifications',
        'meta_description': 'Stay updated with academic, exam, event, fee, and general notifications from Greenwood International Academy.',
    })


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            messages.success(request, 'Thank you for contacting us. Our team will connect with you shortly.')
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {
        'form': form,
        'department_contacts': DEPARTMENT_CONTACTS,
        'submitted': submitted,
        'page_title': 'Contact Us',
        'meta_description': 'Contact Greenwood International Academy for admissions, academics, transport, fees, and general enquiries.',
    })


def enquiry(request):
    enquiry_success = None
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.reference_number = random_code('ENQ')
            enquiry.documents = ', '.join(form.cleaned_data['documents'])
            enquiry.save()
            enquiry_success = enquiry
            messages.success(request, 'Admission enquiry submitted successfully.')
            form = EnquiryForm()
    else:
        form = EnquiryForm(initial={
            'student_name': 'Aanya Mehra',
            'nationality': 'Indian',
            'applying_class': 'Class 5',
            'medium': 'English',
            'father_name': 'Rahul Mehra',
            'mother_name': 'Simran Mehra',
            'occupation': 'Senior Project Manager',
            'income': '₹12,00,000 - ₹18,00,000',
            'contact': '+91 98111 22334',
            'email': 'rahul.mehra@example.com',
            'address': 'B-214, Vasant Kunj, New Delhi - 110070',
            'preferred_session': '2024-25',
        })
    return render(request, 'website/enquiry.html', {
        'form': form,
        'admission_steps': ADMISSION_STEPS,
        'important_dates': IMPORTANT_DATES,
        'enquiry_success': enquiry_success,
        'page_title': 'Admission Enquiry',
        'meta_description': 'Submit a multi-step admission enquiry form and learn the Greenwood admission process and important dates.',
    })


def faculty(request):
    return render(request, 'website/faculty.html', {
        'faculty_members': FacultyMember.objects.all(),
        'page_title': 'Faculty',
        'meta_description': 'Meet the faculty of Greenwood International Academy and explore departments, subjects, and experience.',
    })
