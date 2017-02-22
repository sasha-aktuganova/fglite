from django.contrib import admin
from .models import Store
from .models import Menu
from .models import Menu_item

admin.site.register(Store)
admin.site.register(Menu)
admin.site.register(Menu_item)