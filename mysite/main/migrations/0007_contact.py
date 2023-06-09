# Generated by Django 4.1.7 on 2023-03-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='User name')),
                ('email', models.EmailField(max_length=254, verbose_name='User email')),
                ('company', models.CharField(max_length=50, verbose_name='User name')),
                ('message', models.TextField(verbose_name='User message')),
            ],
        ),
    ]
