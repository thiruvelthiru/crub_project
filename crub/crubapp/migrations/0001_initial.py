# Generated by Django 4.2.4 on 2023-10-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Age', models.IntegerField(default='')),
                ('Dob', models.DateField(default='')),
                ('Email', models.CharField(default='', max_length=50)),
                ('Phone_no', models.IntegerField(default='')),
            ],
        ),
    ]