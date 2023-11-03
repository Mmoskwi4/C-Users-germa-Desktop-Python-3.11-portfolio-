# Generated by Django 4.2.4 on 2023-09-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('basic', models.CharField(max_length=50, verbose_name='Бисквит')),
                ('cream', models.CharField(max_length=50, verbose_name='Крем')),
                ('filling', models.CharField(max_length=50, null=True, verbose_name='Начинка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Цена')),
                ('text', models.TextField(max_length=256, verbose_name='Описание')),
                ('date', models.DateTimeField()),
                ('img', models.ImageField(default='', upload_to='product_image/completed_works')),
            ],
            options={
                'verbose_name': 'Готовая работа',
                'verbose_name_plural': 'Готовые работы',
            },
        ),
    ]
