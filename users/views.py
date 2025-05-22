from django.views.generic import CreateView

from users.models import User


class UserCreateView(CreateView):
    model = User
