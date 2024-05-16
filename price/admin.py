from django.contrib import admin
from price.models import com_var_data , com_static_data

class varadmin(admin.ModelAdmin):
    list_display= ["sh_volume" ,"sh_price"]
admin.site.register(com_var_data,varadmin)

class staticadmin(admin.ModelAdmin):
    list_display=["com_name", "com_type","com_net_income"]

admin.site.register(com_static_data,staticadmin)
# Register your models here.
