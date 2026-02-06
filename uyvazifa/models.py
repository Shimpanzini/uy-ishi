from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.





class Maktab(AbstractUser):
    nom = models.CharField(max_length=255)
    ishga_tushurilgan_vaqt = models.DateField()
    rasm = models.ImageField(upload_to='maktablar/', blank=True, null=True)
    direktor = models.IntegerField(default=0)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    ozgargan_vaqt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Oquvchi(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField()
    tugulgan_kun = models.DateField()
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE, related_name='oquvchilar')
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    ozgargan_vaqt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ism} {self.familya}"


class Oqituvchi(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField()
    tugulgan_kun = models.DateField()
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE, related_name='oqituvchilar')
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    ozgartirlgan_vaqt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ism} {self.familya}"


class Gurux(models.Model):
    nom = models.CharField(max_length=100)
    ustoz = models.ForeignKey(Oqituvchi, on_delete=models.CASCADE, related_name='guruxlar')
    oquvchilar = models.ManyToManyField(Oquvchi, related_name='guruxlar')
    boshlanish_vaqt = models.DateField()
    tugash_vaqt = models.DateField()
    dars_vaqti = models.TimeField(help_text="Masalan: 15:00")

    def __str__(self):
        return self.nom
