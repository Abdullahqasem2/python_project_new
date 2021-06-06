# Generated by Django 2.2.4 on 2021-06-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0002_auto_20210604_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='lancer_info',
            name='language',
        ),
        migrations.AddField(
            model_name='lancer_info',
            name='lan',
            field=models.ManyToManyField(null=True, related_name='lancer', to='logapp.Language'),
        ),
    ]