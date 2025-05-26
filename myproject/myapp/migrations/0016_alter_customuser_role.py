from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0015_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[("tenant", "Tenant"), ("landlord", "Landlord")],
                default="tenant",
                max_length=20,
            ),
        ),
    ]
