# Generated by Django 5.1.7 on 2025-04-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_livro_categoria_livro_editora'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(blank=True, related_name='livros', to='core.autor'),
        ),
    ]
