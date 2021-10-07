# Generated by Django 3.2.6 on 2021-09-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_enquiry1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('full_name', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('district', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]