# Generated by Django 2.2.24 on 2025-01-11 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20250111_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='из кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, verbose_name='название на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, verbose_name='название на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Defence',
            field=models.IntegerField(blank=True, null=True, verbose_name='защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Health',
            field=models.IntegerField(blank=True, null=True, verbose_name='здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Level',
            field=models.IntegerField(blank=True, null=True, verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Strength',
            field=models.IntegerField(blank=True, null=True, verbose_name='сила'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(null=True, verbose_name='время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(null=True, verbose_name='время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(null=True, verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(null=True, verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon', verbose_name='покемон'),
        ),
    ]
