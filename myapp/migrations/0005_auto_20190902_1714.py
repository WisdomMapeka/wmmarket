# Generated by Django 2.2.3 on 2019-09-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_category_default_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_and_Prod_default_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to='uploads/default')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='default_picture',
        ),
    ]
