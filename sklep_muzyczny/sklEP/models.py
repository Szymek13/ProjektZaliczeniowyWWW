from django.db import models

RODZAJ = (
    ('SI', 'Singiel'),
    ('EP', 'Extended Play'),
    ('LP', 'LongPlay'),
    ('MX', 'Mixtape')
)

class Gatunek(models.Model):

    gatunek = models.CharField(max_length=60)

    def __str__(self):
        return self.gatunek

    class Meta:
        ordering = ["gatunek"]

class Wytwornia(models.Model):

    nazwa = models.CharField(max_length=60)
    gatunek = models.ForeignKey(Gatunek, null=True, blank=True, on_delete=models.SET_NULL)
    zalozyciel = models.CharField(max_length=100)
    siedziba = models.CharField(max_length=60)

    def __str__(self):
        return self.nazwa

    class Meta:
        ordering = ["nazwa"]

class Producent(models.Model):

    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    pseudonim = models.CharField(max_length=60)
    gatunek = models.ForeignKey(Gatunek, null=True, blank=True, on_delete=models.SET_NULL)
    pochodzenie = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ["pseudonim"]

class Album(models.Model):

    rodzaj = models.CharField(max_length=2, choices=RODZAJ, default=RODZAJ[0][0])
    autor = models.ForeignKey(Producent, null=True, blank=True, on_delete=models.SET_NULL)
    nazwa = models.CharField(max_length=60)
    gatunek = models.ForeignKey(Gatunek, null=True, blank=True, on_delete=models.SET_NULL)
    data_premiery = models.DateField()
    ilosc_utworow = models.IntegerField()

    def __str__(self):
        return self.nazwa

    class Meta:
        ordering = ["nazwa"]

class Festiwal(models.Model):

    nazwa = models.CharField(max_length=150)
    gospodarz = models.ForeignKey(Producent, null=True, blank=True, on_delete=models.SET_NULL)
    kraj = models.CharField(max_length=60)

    def __str__(self):
        return self.nazwa

    class Meta:
        ordering = ["nazwa"]

