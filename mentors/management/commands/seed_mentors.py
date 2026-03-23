from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from mentors.models import MentorProfile

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed Tamil mentor data'

    def handle(self, *args, **kwargs):
        mentors = [
            {'username': 'arjun_dev', 'email': 'arjun@example.com', 'first_name': 'Arjun', 'last_name': 'Murugan', 'bio': 'Full Stack Developer with 5 years experience in Django and React.', 'expertise': 'Python, Django, React', 'rate': 60.00},
            {'username': 'priya_data', 'email': 'priya@example.com', 'first_name': 'Priya', 'last_name': 'Krishnamurthy', 'bio': 'Data Scientist specializing in machine learning and AI solutions.', 'expertise': 'Machine Learning, Python, TensorFlow', 'rate': 80.00},
            {'username': 'karthik_cloud', 'email': 'karthik@example.com', 'first_name': 'Karthik', 'last_name': 'Sundaram', 'bio': 'AWS Certified Cloud Architect with 7 years of experience.', 'expertise': 'AWS, DevOps, Docker, Kubernetes', 'rate': 90.00},
            {'username': 'deepa_ui', 'email': 'deepa@example.com', 'first_name': 'Deepa', 'last_name': 'Rajendhiran', 'bio': 'UI/UX Designer with expertise in Figma and user research.', 'expertise': 'UI/UX, Figma, Adobe XD', 'rate': 55.00},
            {'username': 'vijay_cyber', 'email': 'vijay@example.com', 'first_name': 'Vijay', 'last_name': 'Annamalai', 'bio': 'Cybersecurity expert with CEH certification and 6 years experience.', 'expertise': 'Cybersecurity, Ethical Hacking, Network Security', 'rate': 95.00},
            {'username': 'kavitha_mobile', 'email': 'kavitha@example.com', 'first_name': 'Kavitha', 'last_name': 'Subramanian', 'bio': 'Mobile app developer specializing in Flutter and React Native.', 'expertise': 'Flutter, React Native, Android', 'rate': 70.00},
            {'username': 'senthil_db', 'email': 'senthil@example.com', 'first_name': 'Senthil', 'last_name': 'Pandian', 'bio': 'Database Administrator with expertise in PostgreSQL and MySQL.', 'expertise': 'PostgreSQL, MySQL, MongoDB', 'rate': 65.00},
            {'username': 'anitha_qa', 'email': 'anitha@example.com', 'first_name': 'Anitha', 'last_name': 'Velmurugan', 'bio': 'QA Engineer with strong automation testing skills using Selenium.', 'expertise': 'Selenium, QA Testing, Python', 'rate': 50.00},
            {'username': 'rajan_finance', 'email': 'rajan@example.com', 'first_name': 'Rajan', 'last_name': 'Thirumalai', 'bio': 'Chartered Accountant with 10 years experience in financial planning.', 'expertise': 'Finance, Accounting, Tax Planning', 'rate': 75.00},
            {'username': 'meena_hr', 'email': 'meena@example.com', 'first_name': 'Meena', 'last_name': 'Saravanan', 'bio': 'HR Manager with expertise in talent acquisition and employee relations.', 'expertise': 'Human Resources, Recruitment, Training', 'rate': 45.00},
            {'username': 'balaji_marketing', 'email': 'balaji@example.com', 'first_name': 'Balaji', 'last_name': 'Natarajan', 'bio': 'Digital Marketing expert with experience in SEO and social media.', 'expertise': 'Digital Marketing, SEO, Social Media', 'rate': 55.00},
            {'username': 'suganya_design', 'email': 'suganya@example.com', 'first_name': 'Suganya', 'last_name': 'Ramamoorthy', 'bio': 'Graphic designer with 8 years experience in branding and illustration.', 'expertise': 'Graphic Design, Branding, Illustration', 'rate': 50.00},
            {'username': 'murugan_edu', 'email': 'murugan@example.com', 'first_name': 'Murugan', 'last_name': 'Palanisamy', 'bio': 'Experienced educator and curriculum developer for STEM subjects.', 'expertise': 'Education, Mathematics, Science', 'rate': 40.00},
            {'username': 'lavanya_health', 'email': 'lavanya@example.com', 'first_name': 'Lavanya', 'last_name': 'Govindarajan', 'bio': 'Healthcare consultant with expertise in hospital management.', 'expertise': 'Healthcare, Hospital Management, Public Health', 'rate': 85.00},
        ]

        for m in mentors:
            if not User.objects.filter(username=m['username']).exists():
                u = User.objects.create_user(
                    username=m['username'],
                    email=m['email'],
                    password='mentor123',
                    first_name=m['first_name'],
                    last_name=m['last_name'],
                    role='mentor'
                )
                MentorProfile.objects.create(
                    user=u,
                    bi

Set-Content build.sh @"
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py seed_mentors
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    u = User.objects.create_superuser('admin', 'dharshinidr05@gmail.com', 'admin1234')
    u.is_staff = True
    u.is_superuser = True
    u.save()
else:
    u = User.objects.get(username='admin')
    u.is_staff = True
    u.is_superuser = True
    u.set_password('admin1234')
    u.save()
"
