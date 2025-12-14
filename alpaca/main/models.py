from django.db import models
from django.utils.translation import gettext_lazy as _


class Report(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок')
    content = models.TextField(max_length=1000,
                               verbose_name='Содержание')
    time_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Время обновления')
    is_accepted = models.BooleanField(default=False,
                                      verbose_name='Одобрен')
    car = models.ForeignKey('Car', on_delete=models.PROTECT,
                            verbose_name='Т/С')
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT,
                                 verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.title} ({self.time_created} - {self.time_updated})'

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
    

class Car(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Наименование')
    sign = models.CharField(max_length=6,
                            verbose_name='Регистрационный знак')

    def __str__(self):
        return f'{self.name} ({self.sign})'

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспотные средсва'


class Employee(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Имя')
    surname = models.CharField(max_length=50,
                               verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50,
                                  verbose_name='Отчество',
                                  blank=True,
                                  null=True)
    position = models.ForeignKey('EmployeePosition',
                                 on_delete=models.PROTECT,
                                 verbose_name='Должность')
    login = models.CharField(max_length=255,
                             verbose_name='Логин')
    password = models.CharField(max_length=1000,
                                verbose_name='Пароль')

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic} ({self.position})'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class EmployeePosition(models.Model):
    class AccessLevel(models.TextChoices):
        WORKER = 'WR', _("Worker")
        OPERATOR = "OP", _("Operator")
        ADMIN = "AD", _("Admin")

    name = models.CharField(max_length=100,
                            verbose_name='Наименование')
    description = models.TextField(max_length=1000,
                                   null=True,
                                   verbose_name='Описание',
                                   blank=True)
    access_level = models.CharField(max_length=2,
                                    choices=AccessLevel,
                                    default=AccessLevel.WORKER,
                                    verbose_name='Уровень доступа')

    def __str__(self):
        return f'{self.name} ({self.access_level})'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
