# Generated by Django 2.2.3 on 2019-09-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190902_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Content for description meta tag', max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(blank=True, help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Content for description meta tag', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(blank=True, help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, help_text='Unique value for product page URL, created from name.', max_length=255, null=True, unique=True),
        ),
    ]
