# Generated by Django 4.2.3 on 2023-09-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassicCake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('basic', models.CharField(max_length=50, verbose_name='Бисквит')),
                ('cream', models.CharField(max_length=50, verbose_name='Крем')),
                ('filling', models.CharField(max_length=50, null=True, verbose_name='Начинка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Цена')),
                ('date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='product_image')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Классические',
            },
        ),
        migrations.CreateModel(
            name='EasterCake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('basic', models.CharField(max_length=50, verbose_name='Бисквит')),
                ('cream', models.CharField(max_length=50, verbose_name='Крем')),
                ('filling', models.CharField(max_length=50, null=True, verbose_name='Начинка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Цена')),
                ('date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='product_image')),
            ],
            options={
                'verbose_name': 'Кулич',
                'verbose_name_plural': 'Куличи',
            },
        ),
        migrations.CreateModel(
            name='OtherSweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('basic', models.CharField(max_length=50, verbose_name='Бисквит')),
                ('cream', models.CharField(max_length=50, verbose_name='Крем')),
                ('filling', models.CharField(max_length=50, null=True, verbose_name='Начинка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Цена')),
                ('date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='product_image')),
            ],
            options={
                'verbose_name': 'Сладость',
                'verbose_name_plural': 'Другий сладости',
            },
        ),
        migrations.CreateModel(
            name='Trifles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('basic', models.CharField(max_length=50, verbose_name='Бисквит')),
                ('cream', models.CharField(max_length=50, verbose_name='Крем')),
                ('filling', models.CharField(max_length=50, null=True, verbose_name='Начинка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Цена')),
                ('date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='product_image')),
            ],
            options={
                'verbose_name': 'Трайфл',
                'verbose_name_plural': 'Трайфлы',
            },
        ),
    ]