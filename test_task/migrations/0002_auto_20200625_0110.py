# Generated by Django 3.0.7 on 2020-06-25 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.DeleteModel(
            name='PhantomUser',
        ),
        migrations.AddField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_task.Post'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
