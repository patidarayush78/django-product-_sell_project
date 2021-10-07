from django.contrib import admin
from .models import heloo, mobile, user_enquiry1, userorder
# Register your models here.
admin.site.register(mobile)
admin.site.register(userorder)
admin.site.register(user_enquiry1)
admin.site.register(heloo)