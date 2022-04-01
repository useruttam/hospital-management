
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(max_length=100),
        ),
    ]
