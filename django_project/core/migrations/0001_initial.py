# Generated by Django 5.1.6 on 2025-03-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('github', models.CharField(max_length=50)),
                ('linkedin', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
                'ordering': ['email'],
            },
        ),
    ]
