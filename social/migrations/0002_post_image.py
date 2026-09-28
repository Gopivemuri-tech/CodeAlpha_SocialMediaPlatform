from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):
    dependencies=[('social','0001_initial')]
    operations=[
        migrations.AddField(
            model_name='post',name='image',
            field=models.FileField(blank=True,upload_to='posts/',validators=[django.core.validators.FileExtensionValidator(['jpg','jpeg','png','webp','gif'])]),
        ),
    ]
