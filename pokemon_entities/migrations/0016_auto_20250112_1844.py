# Generated by Django 2.2.24 on 2025-01-12 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20250112_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_objects', to='pokemon_entities.Pokemon', verbose_name='покемон'),
        ),
    ]
