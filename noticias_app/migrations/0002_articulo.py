# Generated by Django 5.0.3 on 2024-03-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
