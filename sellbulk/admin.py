from django.contrib import admin

# Register your models here.
from .models import Devices, Inquerer, GeneralInquery

# Register your models here.
class DevicesAdmin(admin.ModelAdmin):
    list_display = ('deviceType','deviceOrder','deviceQuantity','deviceCondition','inquerer')
    list_filter = ('deviceType','deviceOrder','deviceQuantity','deviceCondition','inquerer')
    search_field =('deviceType','deviceOrder','deviceQuantity','deviceCondition','inquerer')



class InquererAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','email',)
    list_filter = ('firstName','lastName','email',)
    search_field = ('firstName','lastName','email',)

class GenaralInqueryAdmin(admin.ModelAdmin):
    list_display = ('description','subject','firstName','lastName','topic','email','phoneNumber')
    list_filter = ('description','subject','firstName','lastName','topic','email','phoneNumber')
    search_field =('description','subject','firstName','lastName','topic','email','phoneNumber')


admin.site.register(GeneralInquery,GenaralInqueryAdmin)
admin.site.register(Devices,DevicesAdmin)
admin.site.register(Inquerer, InquererAdmin)