# Generated by Django 2.0.1 on 2018-01-16 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_storage_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='client',
        ),
        migrations.AddField(
            model_name='supplier',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='controller.Client'),
            preserve_default=False,
        ),
    ]
