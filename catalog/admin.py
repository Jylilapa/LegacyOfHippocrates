from django.contrib import admin

from catalog.models import Doctor, MakeAnAppointment, Service


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name", "specialization", "experience")
    list_filter = ("specialization", "experience")
    search_fields = ("first_name", "specialization", "experience")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "doctor", "price")
    list_filter = (
        "name",
        "price",
    )
    search_fields = ("name",)


@admin.register(MakeAnAppointment)
class MakeAnAppointmentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "doctor", "date")
    list_filter = ("first_name", "doctor", "date")
    search_fields = ("first_name",)
