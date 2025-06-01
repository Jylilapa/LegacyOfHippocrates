from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.forms import MakeAnAppointmentForm
from catalog.models import Doctor, MakeAnAppointment, Service


class HomeListView(ListView):
    model = Service


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ServiceDetailView(DetailView):
    model = Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ("name", "description", "price", "doctor")
    success_url = reverse_lazy("catalog:service_list")


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ("name", "description", "price", "doctor")
    success_url = reverse_lazy("catalog:service_list")


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy("catalog:service_list")


class DoctorListView(ListView):
    model = Doctor
    template_name = "catalog/doctor_list.html"


class DoctorDetailView(DetailView):
    model = Doctor


class DoctorCreateView(CreateView):
    model = Doctor
    fields = ("first_name", "middle_name", "last_name", "specialization", "experience", "description", "photo")
    success_url = reverse_lazy("catalog:doctor_list")


class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ("first_name", "middle_name", "last_name", "specialization", "experience", "description", "photo")
    success_url = reverse_lazy("catalog:doctor_list")


class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy("catalog:doctor_list")


class MakeAnAppointmentListView(LoginRequiredMixin, ListView):
    model = MakeAnAppointment


class MakeAnAppointmentCreateView(LoginRequiredMixin, CreateView):
    model = MakeAnAppointment
    form_class = MakeAnAppointmentForm
    success_url = reverse_lazy("catalog:makeanappointment_list")


class MakeAnAppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = MakeAnAppointment
    form_class = MakeAnAppointmentForm
    success_url = reverse_lazy("catalog:makeanappointment_list")


class MakeAnAppointmentDetailView(LoginRequiredMixin, DetailView):
    model = MakeAnAppointment
