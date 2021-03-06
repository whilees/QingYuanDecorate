# Generated by Django 2.0.1 on 2018-01-15 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='corresponding_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corresponding_supplier', to='controller.Supplier'),
        ),
        migrations.AlterField(
            model_name='material',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage', to='controller.Storage'),
        ),
        migrations.AlterField(
            model_name='order',
            name='foreman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oder_foreman', to='controller.Supplier'),
        ),
        migrations.AlterField(
            model_name='order',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oder_storage', to='controller.Storage'),
        ),
        migrations.AlterField(
            model_name='project',
            name='default_supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_supervisor', to='controller.Supervisor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='controller.Supplier'),
        ),
    ]
