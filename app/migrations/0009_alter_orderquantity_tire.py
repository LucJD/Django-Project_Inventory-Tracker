# Generated by Django 4.1.5 on 2023-03-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_outvoice_is_finalized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderquantity',
            name='tire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tire'),
        ),
    ]
