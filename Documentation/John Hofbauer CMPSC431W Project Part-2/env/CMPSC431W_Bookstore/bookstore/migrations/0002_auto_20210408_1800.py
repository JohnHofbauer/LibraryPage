# Generated by Django 3.2 on 2021-04-08 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('AuthorID', models.AutoField(primary_key=True, serialize=False)),
                ('ISBN', models.CharField(max_length=20)),
                ('FullName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('ISBN', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Subject', models.CharField(max_length=255)),
                ('keywords', models.TextField()),
                ('Price', models.FloatField()),
                ('StockLevel', models.IntegerField()),
                ('NumberOfPages', models.IntegerField()),
                ('PublicationDate', models.DateField()),
                ('Language', models.CharField(max_length=255)),
                ('Publisher', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
