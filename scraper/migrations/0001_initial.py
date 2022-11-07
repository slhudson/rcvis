# Generated by Django 3.2.15 on 2022-11-06 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visualizer', '0027_alter_jsonconfig_textforwinner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scraper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrapableURL', models.CharField(max_length=128)),
                ('sourceURL', models.CharField(max_length=128)),
                ('lastSuccessfulScrape', models.DateTimeField(blank=True, null=True)),
                ('lastFailedScrape', models.DateTimeField(blank=True, null=True)),
                ('areResultsCertified', models.BooleanField(default=False)),
                ('jsonConfig', models.OneToOneField(blank=True, null=True,
                                                    on_delete=django.db.models.deletion.CASCADE, to='visualizer.jsonconfig')),
            ],
        ),
    ]
