# import django
# from django.conf import settings
# # Initialize Django
# django.setup()

import django
from django.conf import settings

# Check if Django is already initialized
if not settings.configured:
    # Initialize Django
    django.setup()
