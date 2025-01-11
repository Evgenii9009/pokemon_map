# Generated by Django 2.2.24 on 2025-01-11 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20250111_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolution', to='pokemon_entities.Pokemon'),
        ),
    ]
