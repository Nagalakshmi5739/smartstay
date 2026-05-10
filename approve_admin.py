import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_project.settings')
django.setup()

from core.models import User

try:
    admin_user = User.objects.get(username='admin')
    admin_user.status = 'approved'
    admin_user.role = 'admin'
    admin_user.save()
    print("Admin user approved successfully!")
except User.DoesNotExist:
    print("Admin user does not exist.")
