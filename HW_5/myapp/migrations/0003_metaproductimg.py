

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_productimg"),
    ]

    operations = [
        migrations.CreateModel(
            name="MetaProductImg",
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
                ("name", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="img_prod/")),
            ],
        ),
    ]
