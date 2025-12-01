# mentors/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from faker import Faker
import random
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta

from accounts.models import CustomUser
from mentors.models import MentorProfile, Booking
from chat.models import Message

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake mentors, mentees, bookings and messages'

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        # ---- Create mentors ----
        mentors = []
        for i in range(5):
            username = f"mentor_{fake.user_name()}_{i}"
            email = fake.unique.email()
            # avoid duplicates
            user, created = CustomUser.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'role': 'mentor'
                }
            )
            if created:
                user.set_password('password123')
                user.save()

            # create mentor profile if not exists
            profile, prof_created = MentorProfile.objects.get_or_create(
                user=user,
                defaults={
                    'bio': fake.paragraph(nb_sentences=3),
                    'expertise': ', '.join(fake.words(nb=3)),
                    'hourly_rate': Decimal(random.randint(20, 150)),
                }
            )
            mentors.append(profile)

        # ---- Create mentees ----
        mentees = []
        for i in range(10):
            username = f"mentee_{fake.user_name()}_{i}"
            email = fake.unique.email()
            user, created = CustomUser.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'role': 'mentee'
                }
            )
            if created:
                user.set_password('password123')
                user.save()
            mentees.append(user)

        # ---- Create bookings (random mentee -> random mentor) ----
        for i in range(15):
            mentee = random.choice(mentees)
            mentor_profile = random.choice(mentors)
            # random future date within next 30 days
            days_ahead = random.randint(1, 30)
            booking_date = (timezone.now() + timedelta(days=days_ahead)).date()
            # random hour between 9 and 17
            hour = random.randint(9, 17)
            booking_time = timezone.datetime(
                booking_date.year, booking_date.month, booking_date.day, hour, 0, tzinfo=timezone.get_current_timezone()
            ).time()

            Booking.objects.create(
                mentee=mentee,
                mentor=mentor_profile,
                date=booking_date,
                time=booking_time,
                status=random.choice(['pending', 'confirmed'])
            )

        # ---- Create messages between random pairs ----
        for i in range(25):
            sender_is_mentor = random.choice([True, False])
            if sender_is_mentor:
                sender_profile = random.choice(mentors)
                sender = sender_profile.user
                receiver = random.choice(mentees)
            else:
                sender = random.choice(mentees)
                receiver = random.choice(mentors).user

            Message.objects.create(
                sender=sender,
                receiver=receiver,
                message=fake.sentence(nb_words=12)
            )

        self.stdout.write(self.style.SUCCESS('Seeding complete.'))
        self.stdout.write('Created mentors: %d, mentees: %d' % (len(mentors), len(mentees)))
        self.stdout.write('All fake users have password: password123')
