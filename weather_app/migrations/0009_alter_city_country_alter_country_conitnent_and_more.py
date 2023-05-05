# Generated by Django 4.1.7 on 2023-04-19 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0008_alter_continent_continent_img_alter_country_flag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='weather_app.country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='conitnent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='weather_app.continent'),
        ),
        migrations.AlterField(
            model_name='dateweather',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dateweather', to='weather_app.city'),
        ),
    ]