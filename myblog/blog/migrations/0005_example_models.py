# Generated by Django 4.1 on 2022-12-19 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comments_remove_post_category_delete_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example_Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('posts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Посты')),
            ],
        ),
    ]
