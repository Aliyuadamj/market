# Generated by Django 4.2.5 on 2023-11-07 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',)},
        ),
    ]
