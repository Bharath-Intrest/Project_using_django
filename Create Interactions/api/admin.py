from django.contrib import admin 
from .models import log_in

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('user_name','password1')
    search_fields=('user_name','password1')
admin.site.register(log_in,PostAdmin)