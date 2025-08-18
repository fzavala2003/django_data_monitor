import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')  # Cambia 'tu_proyecto' por el nombre de tu proyecto
django.setup()

from django.contrib.auth.models import User

usuario01 = User.objects.create_user(username='usuario01', password='password01')
usuario01.is_staff = False
usuario01.is_superuser = False
usuario01.save()

usuario02 = User.objects.create_user(username='usuario02', password='password02')
usuario02.is_staff = False
usuario02.is_superuser = False
usuario02.save()

print("Usuarios creados correctamente.")