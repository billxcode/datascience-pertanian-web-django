from django.db import models

# Create your models here.

class Tanaman(models.Model):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class NameKriteria(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Kriteria(models.Model):
    tanaman = models.ForeignKey(Tanaman, on_delete=models.CASCADE)
    name_kriteria = models.ForeignKey(NameKriteria, default=None, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=6)
    periode = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.value)

class Bobot(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.value)
