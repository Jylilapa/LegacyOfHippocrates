from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ContactsTemplateView, DoctorCreateView, DoctorDeleteView, DoctorDetailView, DoctorListView,
                           DoctorUpdateView, HomeListView, MakeAnAppointmentCreateView, MakeAnAppointmentDetailView,
                           MakeAnAppointmentListView, ServiceCreateView, ServiceDeleteView, ServiceDetailView,
                           ServiceUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeListView.as_view(), name="service_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("catalog/create/", ServiceCreateView.as_view(), name="service_create"),
    path("catalog/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("catalog/<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"),
    path("catalog/<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_delete"),
    path("catalog/doctor/", DoctorListView.as_view(), name="doctor_list"),
    path("catalog/doctor/<int:pk>/", DoctorDetailView.as_view(), name="doctor_detail"),
    path("catalog/doctor/create/", DoctorCreateView.as_view(), name="doctor_create"),
    path("catalog/doctor/<int:pk>/update/", DoctorUpdateView.as_view(), name="doctor_update"),
    path("catalog/doctor/<int:pk>/delete/", DoctorDeleteView.as_view(), name="doctor_delete"),
    path("makeanappointment/create/", MakeAnAppointmentCreateView.as_view(), name="makeanappointment_create"),
    path("makeanappointment/", MakeAnAppointmentListView.as_view(), name="makeanappointment_list"),
    path("makeanappointment/<int:pk>/", MakeAnAppointmentDetailView.as_view(), name="makeanappointment_detail"),
]
