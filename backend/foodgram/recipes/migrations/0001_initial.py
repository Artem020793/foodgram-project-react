# Generated by Django 3.2.17 on 2023-02-08 16:06

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Список покупок',
                'verbose_name_plural': 'Список покупок',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название ингредиента', max_length=256, verbose_name='Название ингредиента')),
                ('measurement_unit', models.CharField(help_text='Введите единицу измерения', max_length=100, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(help_text='Укажите количество', validators=[django.core.validators.MinValueValidator(1, message='Количество ингредиентов не может быть меньше 1')], verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Количество ингредиента',
                'verbose_name_plural': 'Количества ингредиента',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название рецепта', max_length=200, verbose_name='Название рецепта')),
                ('image', models.ImageField(help_text='Добавьте изображение', upload_to='recipes/', verbose_name='Изображение')),
                ('text', models.CharField(help_text='Введите текст', max_length=6144, verbose_name='Текст')),
                ('cooking_time', models.PositiveSmallIntegerField(help_text='Укажите время приготовления', validators=[django.core.validators.MinValueValidator(1, message='Время приготовления не может быть меньше 1 минуты')], verbose_name='Время приготовления')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название тега', max_length=100, unique=True, verbose_name='Название тега')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Укажите цвет в HEX', image_field=None, max_length=18, samples=None, unique=True, verbose_name='Цвет в HEX')),
                ('slug', models.SlugField(help_text='Введите уникальную строку', unique=True, verbose_name='Уникальная строка')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='TagRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(help_text='Укажите рецепт', on_delete=django.db.models.deletion.CASCADE, related_name='tag_recipes', to='recipes.recipe', verbose_name='Рецепт')),
                ('tag', models.ForeignKey(help_text='Укажите тег', on_delete=django.db.models.deletion.CASCADE, related_name='tag_recipes', to='recipes.tag', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Рецепты с тегами',
                'verbose_name_plural': 'Рецепты с тегами',
                'ordering': ('-id',),
            },
        ),
    ]
