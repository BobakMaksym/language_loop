# Generated by Django 4.1.1 on 2023-03-27 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('flag_pic', models.ImageField(upload_to='flag_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('picture', models.ImageField(upload_to='picture/')),
                ('location', models.CharField(max_length=100)),
                ('location_link', models.CharField(max_length=1000)),
                ('contacts', models.CharField(max_length=200)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meeting.language')),
            ],
        ),
    ]