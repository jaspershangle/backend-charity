# Generated by Django 2.2 on 2019-04-03 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to='charity.Campaign'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='charity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to='charity.Charity'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to='charity.User'),
        ),
    ]
