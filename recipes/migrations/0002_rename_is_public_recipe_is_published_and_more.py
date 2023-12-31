# Generated by Django 4.2.1 on 2023-06-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="is_public",
            new_name="is_published",
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cover",
            field=models.ImageField(
                blank=True, default="", upload_to="recipes/covers/%Y/%m/%d"
            ),
        ),
    ]
