# Generated by Django 3.2.14 on 2022-07-21 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='商品')),
                ('slug', models.SlugField(max_length=250, verbose_name='URLに表示される名前')),
                ('description', models.TextField(verbose_name='商品説明')),
                ('price', models.IntegerField(verbose_name='価格')),
                ('image', models.ImageField(upload_to='product')),
                ('file', models.FileField(blank=True, upload_to='product/file')),
                ('stock', models.IntegerField(verbose_name='在庫')),
                ('created', models.DateTimeField(auto_now=True)),
                ('baroname1', models.CharField(blank=True, default='光沢感', max_length=150, null=True)),
                ('baroint1', models.IntegerField(blank=True, default=True, null=True)),
                ('baroname2', models.CharField(blank=True, default='伸縮性', max_length=150, null=True)),
                ('baroint2', models.IntegerField(blank=True, default=True, null=True)),
                ('baroname3', models.CharField(blank=True, default='透け感', max_length=150, null=True)),
                ('baroint3', models.IntegerField(blank=True, default=True, null=True)),
            ],
            options={
                'db_table': 'detail',
            },
        ),
        migrations.CreateModel(
            name='Detail_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='コーディネート名')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URLに表示される名前')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, upload_to='file')),
                ('detail', models.ManyToManyField(to='shop.Detail')),
                ('tags', models.ManyToManyField(blank=True, to='shop.PostTag')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='detail',
            name='subtag',
            field=models.ManyToManyField(blank=True, to='shop.Detail_tag'),
        ),
        migrations.AddField(
            model_name='detail',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shop.PostTag'),
        ),
    ]
