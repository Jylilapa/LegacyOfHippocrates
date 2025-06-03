from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Отчество")
    specialization = models.CharField(max_length=200, verbose_name="Специализация")
    experience = models.CharField(max_length=20, verbose_name="Опыт работы")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="catalog/images", verbose_name="Фото")

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
        ordering = ["first_name", "specialization"]

    def __str__(self):
        return self.first_name


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Доктор")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["name"]

    def __str__(self):
        return self.name


class MakeAnAppointment(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Отчество")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Доктор")
    date = models.DateTimeField(verbose_name="Дата и время приема")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["first_name"]

    def __str__(self):
        return self.first_name
