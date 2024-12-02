# Generated by Django 5.1.3 on 2024-12-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "category",
                    models.CharField(
                        choices=[("Academic", "Academic"), ("Personal", "Personal")],
                        max_length=100,
                    ),
                ),
                ("due_date", models.DateField(blank=True, null=True)),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
