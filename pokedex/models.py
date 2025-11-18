from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    level = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='pokemons/', null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
