# Generated by Django 4.2.3 on 2023-10-01 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClassicCake',
        ),
        migrations.DeleteModel(
            name='EasterCake',
        ),
        migrations.DeleteModel(
            name='OtherSweets',
        ),
        migrations.DeleteModel(
            name='Trifles',
        ),
    ]