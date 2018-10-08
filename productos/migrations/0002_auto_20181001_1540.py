# Generated by Django 2.1.1 on 2018-10-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
