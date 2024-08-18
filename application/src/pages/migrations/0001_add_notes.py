from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def create_initial_notes(apps, schema_editor):
    Note = apps.get_model('pages', 'Note')
    User = apps.get_model(settings.AUTH_USER_MODEL)
    alice = User.objects.first()
    bob = User.objects.last()
    Note.objects.create(content='Cybersecurity is important', owner=alice)
    Note.objects.create(content="I hope my notes aren't public", owner=alice)
    Note.objects.create(content='Very secret note...', owner=alice)
    Note.objects.create(content="I use the same password everywhere; hopefully, it doesn't leak.", owner=bob)
    Note.objects.create(content='My address: The White House, Washington D.C.', owner=bob)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(create_initial_notes)
    ]
