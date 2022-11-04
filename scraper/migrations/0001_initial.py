# Generated by Django 3.2.15 on 2022-11-03 16:42

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrapableURL', models.CharField(max_length=128)),
                ('sourceURL', models.CharField(max_length=128)),
                ('lastSuccessfulScrape', models.DateTimeField(null=True, blank=True)),
                ('lastFailedScrape', models.DateTimeField(null=True, blank=True)),
                ('jsonConfig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visualizer.jsonconfig')),
                ('areResultsCertified', models.BooleanField(default=False)),
            ],
        ),
    ]
