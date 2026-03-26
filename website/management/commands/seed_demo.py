from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from website.models import FacultyMember, LeadershipMember, NewsEvent, Notification, PaymentRecord, Testimonial


class Command(BaseCommand):
    help = 'Seed demo data for Greenwood International Academy'

    def handle(self, *args, **options):
        news = [
            {
                'title': 'Admissions Open for Session 2024-25',
                'excerpt': 'Applications are now open from Nursery to Class XI. Campus tours are available on all weekdays.',
                'category': 'Announcement',
                'event_date': timezone.datetime(2024, 12, 1).date(),
                'image_url': 'https://picsum.photos/seed/news1/800/500',
            },
            {
                'title': 'Greenwood Students Win National STEM Challenge',
                'excerpt': 'Our robotics team secured the national runner-up title with an AI-powered smart irrigation model.',
                'category': 'News',
                'event_date': timezone.datetime(2024, 11, 18).date(),
                'image_url': 'https://picsum.photos/seed/news2/800/500',
            },
            {
                'title': 'Winter Cultural Fiesta Scheduled for 20 December',
                'excerpt': 'An evening celebrating music, dance, theatre, and creative arts with parents and alumni.',
                'category': 'Event',
                'event_date': timezone.datetime(2024, 12, 20).date(),
                'image_url': 'https://picsum.photos/seed/news3/800/500',
            },
        ]
        for item in news:
            NewsEvent.objects.update_or_create(title=item['title'], defaults=item)

        testimonials = [
            {
                'name': 'Riya Bansal',
                'role': 'Parent of Grade 6 Student',
                'quote': 'The school balances discipline, care, and innovation beautifully. My child has grown in confidence and communication.',
                'image_url': 'https://picsum.photos/seed/parent1/200/200',
            },
            {
                'name': 'Aditya Nair',
                'role': 'Alumnus, Batch 2023',
                'quote': 'From coding labs to debate opportunities, Greenwood helped me discover both my strengths and my direction.',
                'image_url': 'https://picsum.photos/seed/student1/200/200',
            },
            {
                'name': 'Mrs. Kavita Sethi',
                'role': 'Parent of Grade 2 Student',
                'quote': 'The teachers are responsive, warm, and very thoughtful. We always feel informed and supported as parents.',
                'image_url': 'https://picsum.photos/seed/parent2/200/200',
            },
        ]
        for item in testimonials:
            Testimonial.objects.update_or_create(name=item['name'], defaults=item)

        leadership = [
            {
                'name': 'Dr. Meera Khanna',
                'designation': 'Principal',
                'bio': 'An experienced education leader with over 22 years in K-12 school transformation, curriculum design, and student wellbeing.',
                'image_url': 'https://picsum.photos/seed/principal/500/500',
                'display_order': 1,
            },
            {
                'name': 'Mr. Sanjay Kapoor',
                'designation': 'Vice Principal',
                'bio': 'Leads academic strategy, teacher mentoring, and structured quality assurance across middle and senior grades.',
                'image_url': 'https://picsum.photos/seed/vp/500/500',
                'display_order': 2,
            },
            {
                'name': 'Ms. Nandini Rao',
                'designation': 'Head of Admissions',
                'bio': 'Guides family counselling, admissions communication, and student transition planning with a parent-first approach.',
                'image_url': 'https://picsum.photos/seed/admissions/500/500',
                'display_order': 3,
            },
            {
                'name': 'Mr. Arvind Batra',
                'designation': 'Director - Operations',
                'bio': 'Oversees transport, campus safety, facilities, and strategic infrastructure improvements for a modern school experience.',
                'image_url': 'https://picsum.photos/seed/ops/500/500',
                'display_order': 4,
            },
        ]
        for item in leadership:
            LeadershipMember.objects.update_or_create(name=item['name'], defaults=item)

        faculty = [
            ('Dr. Ishita Verma', 'Senior Faculty', 'Physics', 'Ph.D. Physics', 14, 'Science', 'https://picsum.photos/seed/fac1/400/400'),
            ('Mr. Kunal Arora', 'PGT', 'Chemistry', 'M.Sc., B.Ed.', 11, 'Science', 'https://picsum.photos/seed/fac2/400/400'),
            ('Ms. Radhika Jain', 'TGT', 'Biology', 'M.Sc. Zoology', 9, 'Science', 'https://picsum.photos/seed/fac3/400/400'),
            ('Mrs. Sneha Chopra', 'PGT', 'Economics', 'M.A. Economics', 12, 'Commerce', 'https://picsum.photos/seed/fac4/400/400'),
            ('Mr. Kartik Bedi', 'PGT', 'Accountancy', 'M.Com., B.Ed.', 10, 'Commerce', 'https://picsum.photos/seed/fac5/400/400'),
            ('Ms. Aastha Sharma', 'TGT', 'Business Studies', 'MBA, B.Ed.', 8, 'Commerce', 'https://picsum.photos/seed/fac6/400/400'),
            ('Ms. Pooja Lamba', 'HOD', 'English', 'M.A. English', 15, 'Arts', 'https://picsum.photos/seed/fac7/400/400'),
            ('Mr. Dev Malhotra', 'TGT', 'History', 'M.A. History', 7, 'Arts', 'https://picsum.photos/seed/fac8/400/400'),
            ('Mrs. Reema Tandon', 'Counsellor', 'Psychology', 'M.A. Psychology', 13, 'Arts', 'https://picsum.photos/seed/fac9/400/400'),
            ('Mr. Yash Bhatia', 'Coach', 'Physical Education', 'B.P.Ed.', 9, 'Sports', 'https://picsum.photos/seed/fac10/400/400'),
            ('Ms. Tanvi Kohli', 'Activity Coordinator', 'Performing Arts', 'M.P.A.', 6, 'Sports', 'https://picsum.photos/seed/fac11/400/400'),
            ('Mr. Mohit Gulati', 'Admin Manager', 'Operations', 'MBA', 16, 'Administration', 'https://picsum.photos/seed/fac12/400/400'),
        ]
        for name, designation, subject, qualification, exp, dept, image in faculty:
            FacultyMember.objects.update_or_create(
                name=name,
                defaults={
                    'designation': designation,
                    'subject': subject,
                    'qualification': qualification,
                    'experience_years': exp,
                    'department': dept,
                    'image_url': image,
                },
            )

        notices = [
            ('Term-II Midterm Timetable Released', 'Academic', 'The midterm exam schedule for Grades VI-XII has been uploaded to the student portal.', 'fa-solid fa-file-lines', False),
            ('Winter Fiesta Volunteer Registration', 'Events', 'Student council volunteers can register by Friday for cultural fest coordination.', 'fa-solid fa-calendar-days', False),
            ('Quarterly Fee Reminder', 'Fees', 'Fee payment for Quarter 3 is due by 10 January to avoid late charges.', 'fa-solid fa-wallet', False),
            ('Board Practical Schedule', 'Exams', 'Class XII practical examinations begin on 08 January in the senior labs.', 'fa-solid fa-clipboard-check', True),
            ('School Bus Route Update', 'General', 'Minor timing changes have been made for Route 4 and Route 7 with effect from Monday.', 'fa-solid fa-bus', False),
            ('Olympiad Coaching Batch Starts', 'Academic', 'New after-school coaching batches for Maths and Science Olympiads start next week.', 'fa-solid fa-medal', True),
            ('Founders Day Dress Rehearsal', 'Events', 'All performing students must report to the auditorium by 1:30 PM on Thursday.', 'fa-solid fa-masks-theater', False),
            ('Scholarship Renewal Notice', 'Fees', 'Merit scholarship renewal forms must be submitted before the annual review meeting.', 'fa-solid fa-hand-holding-dollar', True),
            ('Pre-Board Guidelines', 'Exams', 'Students are advised to carry ID cards, transparent pouches, and hall tickets.', 'fa-solid fa-pen-ruler', False),
            ('Parent Orientation Deck Shared', 'General', 'A summary presentation from the new parent orientation is now available.', 'fa-solid fa-users-viewfinder', True),
            ('Language Lab Sign-Ups Open', 'Academic', 'Registrations for spoken English and French skill labs are now open.', 'fa-solid fa-language', False),
            ('Inter-House Basketball Fixtures', 'Events', 'Fixtures for junior and senior categories are displayed on the sports board.', 'fa-solid fa-basketball', False),
            ('Transport Helpline Extended', 'General', 'The transport desk will now be available till 6:30 PM during exam week.', 'fa-solid fa-phone-volume', True),
            ('Lab Safety Orientation', 'Academic', 'Mandatory safety orientation for all Grade IX science students on Monday.', 'fa-solid fa-flask-vial', False),
            ('Result Analysis Meeting', 'Exams', 'Faculty meeting scheduled to review class-wise performance trends and action points.', 'fa-solid fa-chart-column', True),
        ]
        base_time = timezone.now()
        for idx, (title, category, description, icon, is_read) in enumerate(notices):
            Notification.objects.update_or_create(
                title=title,
                defaults={
                    'category': category,
                    'description': description,
                    'icon': icon,
                    'is_read': is_read,
                    'timestamp': base_time - timezone.timedelta(hours=idx * 6),
                },
            )

        payments = [
            ('Aarav Khanna', 'GIA2024-1187', 'Class 8 - C', 'Quarterly', 28500.00, 'UPI', 'GIAA1B2C3D4', 'Paid'),
            ('Vihaan Sood', 'GIA2024-1032', 'Class 10 - A', 'Monthly', 9800.00, 'Card', 'GIAX9Y8Z7W6', 'Paid'),
            ('Kiara Mehta', 'GIA2024-0915', 'Class 5 - A', 'Annual', 111500.00, 'NetBanking', 'GIAP7Q6R5S4', 'Paid'),
            ('Anaya Singh', 'GIA2024-0841', 'Class 2 - B', 'Monthly', 7600.00, 'UPI', 'GIAT3U2V1W0', 'Paid'),
            ('Ishaan Kapoor', 'GIA2024-1320', 'Class 12 - Commerce', 'Quarterly', 36250.00, 'BankTransfer', 'GIAM4N5O6P7', 'Paid'),
        ]
        for name, roll, class_section, fee_type, amount, method, txn, status in payments:
            PaymentRecord.objects.update_or_create(
                transaction_id=txn,
                defaults={
                    'student_name': name,
                    'roll_number': roll,
                    'class_section': class_section,
                    'fee_type': fee_type,
                    'amount': amount,
                    'payment_method': method,
                    'status': status,
                },
            )

        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@gia.edu.in', 'Greenwood@123')

        self.stdout.write(self.style.SUCCESS('Demo data seeded successfully.'))
