# Generated by Django 4.2.5 on 2023-10-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=10)),
                ('stuemail', models.EmailField(max_length=20)),
                ('stupass', models.CharField(max_length=20)),
            ],
        ),
    ]
