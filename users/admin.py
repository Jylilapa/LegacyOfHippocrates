from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "first_name", "middle_name", "last_name", "phone_number")
    list_filter = ("first_name", "email")
    search_fields = ("first_name", "email")
