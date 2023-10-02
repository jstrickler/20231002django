from django.core.management.utils import get_random_secret_key
import shutil

settings_path = '{{ cookiecutter.project_slug}}/settings.py'
temp_path = settings_path + ".tmp"
backup_path = settings_path + ".bak"

secret_key = get_random_secret_key()

with open(settings_path) as settings_in:
    with open(temp_path, "w") as settings_out:
        old_content = settings_in.read()
        new_content = old_content.replace('###SECRET_KEY###', secret_key)
        settings_out.write(new_content)

shutil.move(settings_path, backup_path)
shutil.move(temp_path, settings_path)

print("""
Congratulations! you have created project {{ cookiecutter.project_name }}
  
  Now, cd into the {{ cookiecutter.project_slug }} folder.

  Execute this command to set up Django's admin and user databases:
      python manage.py migrate

  You can start creating apps with:
      cookiecutter ../SETUP/cookiecutter-django-app
""")