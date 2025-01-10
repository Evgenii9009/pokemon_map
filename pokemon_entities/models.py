from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    """Покемон"""
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    title_en = models.CharField(max_length=200, null=True)
    title_jp = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.title}'
    

class PokemonEntity(models.Model):
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    Level = models.IntegerField(null=True)
    Health = models.IntegerField(null=True)
    Strength = models.IntegerField(null=True)
    Defence = models.IntegerField(null=True)
    Stamina = models.IntegerField(null=True)


    def __str__(self):
        return f'{self.pokemon}'
