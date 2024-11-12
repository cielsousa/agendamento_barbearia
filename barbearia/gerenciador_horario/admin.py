from django.contrib import admin
from .models import Monday, Tuesday, Wednesday, Thursday, Friday, Client

# Register your models here.
admin.site.register(Client)
admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)
