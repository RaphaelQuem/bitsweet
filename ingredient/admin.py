from django.contrib import admin
from .models import Ingredient

admin.site.site_header = "Bitsweet Admin"
admin.site.site_title = "Bitsweet"
admin.site.site_header = "Bitsweet Admin"
admin.site.register(Ingredient)
