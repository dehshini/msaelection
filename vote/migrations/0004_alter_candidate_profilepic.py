# Generated by Django 3.2 on 2021-04-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_alter_candidate_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='profilePic',
            field=models.ImageField(blank=True, default='/profile_pics/candidate.png', null=True, upload_to='profile_pics'),
        ),
    ]
