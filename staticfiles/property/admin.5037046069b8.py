from django.contrib import admin
from.models import (Property, Property_type, Property_state,
                    Property_management)
# Register your models here.
admin.site.register(Property)
admin.site.register(Property_type)
admin.site.register(Property_state)
admin.site.register(Property_management)
