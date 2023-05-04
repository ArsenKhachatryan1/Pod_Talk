# Generated by Django 4.1.7 on 2023-03-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_download'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('link', models.CharField(max_length=60, verbose_name='link')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
    ]
