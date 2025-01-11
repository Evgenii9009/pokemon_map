from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    """Покемон"""
    title = models.CharField('название', max_length=200)
    image = models.ImageField('картинка', null=True)
    title_en = models.CharField('название на английском', max_length=200, null=True)
    title_jp = models.CharField('название на японском', max_length=200, null=True)
    description = models.TextField('описание', null=True)
    previous_evolution = models.ForeignKey("self", null=True, on_delete=models.SET_NULL, related_name='next_evolution', verbose_name='из кого эволюционирует')

    def __str__(self):
        return f'{self.title}'
    

class PokemonEntity(models.Model):
    """Покемон на карте"""
    lon = models.FloatField('долгота', null=True)
    lat = models.FloatField('широта', null=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='покемон')
    appeared_at = models.DateTimeField('время появления', null=True)
    disappeared_at = models.DateTimeField('время исчезновения', null=True)
    Level = models.IntegerField('уровень', null=True)
    Health = models.IntegerField('здоровье', null=True)
    Strength = models.IntegerField('сила', null=True)
    Defence = models.IntegerField('защита', null=True)
    Stamina = models.IntegerField('выносливость', null=True)


    def __str__(self):
        return f'{self.pokemon}'
