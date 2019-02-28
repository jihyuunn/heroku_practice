# Generated by Django 2.1.5 on 2019-01-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='year_in_school',
            new_name='year',
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_sort',
            field=models.CharField(choices=[('Books&Magazines', 'Books&Magazines'), ('Patent', 'Patent'), ('International Conference', 'International Conference'), ('Domestic Conference', 'Domestic Conference')], default='International Conference', max_length=30),
        ),
    ]