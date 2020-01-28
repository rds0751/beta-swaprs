# Generated by Django 2.1 on 2020-01-27 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category_rel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='photos/storage/')),
                ('small_picture', models.ImageField(blank=True, null=True, upload_to='photos/storage/small/')),
                ('order_mark', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order_mark', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.FloatField(blank=True, default=0.0)),
                ('quantity', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='productPicture/')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_promotion', models.BooleanField(default=False)),
                ('promotion_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('preorder', models.BooleanField(default=False)),
                ('preorder_days', models.IntegerField(blank=True, default=0, null=True)),
                ('self_price', models.FloatField(blank=True, default=0.0)),
                ('internal_delivery', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Доставка по стране')),
                ('is_external', models.BooleanField(default=False, verbose_name='Доставляете за пределы своей страны ?')),
                ('external_delivery', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена международной доставки')),
                ('bought', models.IntegerField(default=0)),
                ('deals', models.IntegerField(default=0)),
                ('link', models.TextField(blank=True, null=True)),
                ('category', models.ManyToManyField(through='shop.Category_rel', to='shop.Category')),
                ('colors', models.ManyToManyField(blank=True, to='shop.Colors')),
                ('comments', models.ManyToManyField(blank=True, to='comments.Comment')),
                ('front_images', models.ManyToManyField(blank=True, related_name='front_images', to='shop.Images')),
                ('images', models.ManyToManyField(blank=True, to='shop.Images')),
                ('keywords', models.ManyToManyField(blank=True, to='shop.Keywords', verbose_name='Ключевый слова')),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TBCategoriesName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn_name', models.CharField(max_length=800)),
                ('en_name', models.CharField(max_length=800)),
                ('ru_name', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, default=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='shop.Sizes'),
        ),
        migrations.AddField(
            model_name='product',
            name='types',
            field=models.ManyToManyField(blank=True, to='shop.Types'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category_rel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='barcode',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
