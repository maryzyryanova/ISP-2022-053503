# """
# ASGI config for config project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# if os.path.isfile(os.path.join(os.path.dirname(__file__), 'local_settings.py')):
#     # Если рядом с manage.py лежит local_settings.py — используем его
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")
# else:
#     # Если нет — используем стандартные настройки без секретов
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


# application = get_asgi_application()