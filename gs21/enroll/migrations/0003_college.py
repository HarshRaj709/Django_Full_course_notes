# Generated by Django 4.2.5 on 2023-10-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeid', models.IntegerField()),
                ('collegename', models.CharField(max_length=50)),
                ('collegeemail', models.CharField(max_length=90)),
                ('collegepass', models.CharField(max_length=50)),
            ],
        ),
    ]
