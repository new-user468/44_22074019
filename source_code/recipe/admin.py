from django.contrib import admin
from .models import Recipe, Recipe_prep_details, Nutri_content, feedback

admin.site.register(Recipe)
admin.site.register(Recipe_prep_details)
admin.site.register(Nutri_content)
admin.site.register(feedback)