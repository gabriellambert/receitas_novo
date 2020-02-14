# Generated by Django 3.0.3 on 2020-02-14 11:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=100)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('date_receita', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('foto_receita', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y')),
                ('publicada', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa')),
            ],
        ),
    ]
