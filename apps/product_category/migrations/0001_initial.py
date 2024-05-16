# Generated by Django 5.0.5 on 2024-05-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Last Update')),
                ('name', models.CharField(max_length=255)),
                ('name_translit', models.CharField(blank=True, max_length=255, null=True)),
                ('text_color', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'product_categories',
            },
        ),
    ]
