from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="1jylilapa@yandex.ru")
        user.set_password("CV_5fhK9")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
