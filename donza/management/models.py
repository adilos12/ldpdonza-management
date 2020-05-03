from django.db import models
from django import forms

from phonenumber_field.modelfields import PhoneNumberField
from localflavor.generic.models import IBANField


class Functie(models.Model):

    functie_id = models.AutoField(primary_key=True)
    functie = models.CharField(max_length=20)

    def __str__(self):
        return self.functie


class Ouder(models.Model):

    ouder_id = models.AutoField(primary_key=True)
    gsmnummer = PhoneNumberField()
    voornaam = models.CharField(max_length=20)
    familienaam = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.voornaam + " " + self.familienaam


class Seizoen(models.Model):

    seizoen_id = models.AutoField(primary_key=True)
    naam = models.CharField(max_length=20)
    startdatum = models.DateField()
    einddatum = models.DateField()
    bezig = models.BooleanField()

    def __str__(self):
        return "({}-{})".format(self.startdatum.year, self.einddatum.year)


class Ploeg(models.Model):

    ploeg_id = models.AutoField(primary_key=True)
    seizoen = models.ForeignKey(
        'management.Seizoen', on_delete=models.CASCADE)
    naam = models.CharField(max_length=20)
    korte_naam = models.CharField(max_length=5)
    leeftijdscategorie = models.IntegerField()

    def __str__(self):
        return "{} ({}-{})".format(self.naam, self.seizoen.startdatum.year, self.seizoen.einddatum.year)

class PloegLid(models.Model):

    ploeg = models.ForeignKey('management.Ploeg', on_delete=models.CASCADE)
    lid = models.ForeignKey('management.Lid', on_delete=models.CASCADE)
    functie = models.ForeignKey('management.Functie', on_delete=models.CASCADE)

    def __str__(self):
        return "Ploeg: {} -- Lid: {} ({})".format(self.ploeg, self.lid, self.functie)


class Lid(models.Model):

    MAN = "m"
    VROUW = "v"
    ANDER = "x"
    GESLACHT_CHOICES = [
        (MAN, "Man"),
        (VROUW, "Vrouw"),
        (ANDER, "Verkies niet te zeggen"),
    ]

    club_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=20)
    familienaam = models.CharField(max_length=50)
    geslacht = models.CharField(
        max_length=1,
        choices=GESLACHT_CHOICES,
        default=MAN
    )
    sportief_lid = models.BooleanField(default=False)
    betalend_lid = models.BooleanField(default=False)
    straatnaam_en_huisnummer = models.CharField(max_length=50)
    postcode = models.IntegerField()
    gemeente = models.CharField(max_length=50)
    geboortedatum = models.DateField(null=True)
    gsmnummer = PhoneNumberField(null=True, blank=True)
    moeder = models.ForeignKey(
        'management.Ouder', related_name='moeder', on_delete=models.SET_NULL, null=True, blank=True)
    vader = models.ForeignKey(
        'management.Ouder', related_name='vader', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    gescheiden_ouders = models.BooleanField(default=False)
    extra_informatie = models.CharField(default="", max_length=500, blank=True)
    rekeningnummer = IBANField(null=True, blank=True)
    lidnummer_vbl = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    functies = models.ManyToManyField(Functie)
    familieleden = models.ManyToManyField("self")

    def __str__(self):
        return "{} {}".format(self.voornaam, self.familienaam, self.lidnummer_vbl)
