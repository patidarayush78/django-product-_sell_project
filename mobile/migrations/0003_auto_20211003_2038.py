# Generated by Django 3.2.6 on 2021-10-03 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobile', '0002_heloo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heloo',
            name='name',
        ),
        migrations.AddField(
            model_name='heloo',
            name='brand',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='heloo',
            name='coverphotoo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heloo',
            name='dateorder',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='heloo',
            name='priceo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heloo',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]