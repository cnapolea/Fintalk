# Generated by Django 2.2.5 on 2019-11-13 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritetalk',
            name='talk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to='talks.Talk'),
        ),
    ]