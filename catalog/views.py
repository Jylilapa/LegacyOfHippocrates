from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.models import Doctor, Service


class HomeListView(ListView):
    model = Service
    # template_name = "catalog/service_list.html"


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
