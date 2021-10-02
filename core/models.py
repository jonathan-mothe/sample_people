from django.db import models
from datetime import date


class PeopleManager(models.Manager):

    def first_five_people(self):
        return self.model.objects.order_by('nome')[:5]

    def starts_with(self, text):
        return self.model.objects.filter(nome__istartswith=text)

    def search_people(self, nome):
        return self.model.objects.filter(nome__icontains=nome)



class People(models.Model):

    GENDER_CHOICES = [
        ("F", "Feminino"),
        ("M", "Masculino"),
    ]

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=15)
    data_nasc = models.DateField()
    sexo = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mae = models.CharField(max_length=150)
    pai = models.CharField(max_length=150)
    celular = models.CharField(max_length=150)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.PositiveIntegerField()
    tipo_sanguineo = models.CharField(max_length=4)

    objects = PeopleManager()


    @property
    def idade(self):
        today = date.today()
        born = self.data_nasc
        return today.year - born.year


    def __str__(self):
        return self.nome
