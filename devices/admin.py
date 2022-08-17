from django.contrib import admin
from .models import Iphone,Macbook,Ipad, SamsungPhone, GooglePhone,Ipod,Iwatch, Devices, Airpods
from import_export.admin import ImportExportModelAdmin

@admin.register(Iphone)
class IphoneAdmin(ImportExportModelAdmin):
    pass
    list_display = ('iphone_model','carrier','capacity','condition','Offer')
    list_filter = ('iphone_model','carrier','capacity','condition','Offer')
    search_field =('iphone_model','carrier','capacity','condition','Offer')

'''class IphoneAdmin(admin.ModelAdmin):
    list_display = ('iphone_model','carrier','capacity','Offer')
    list_filter = ('iphone_model', 'capacity', 'carrier',)
    search_field =('iphone_model', 'capacity', 'carrier',)'''

class MacbookAdmin(admin.ModelAdmin):
    list_display = ('macbook_model','screen_size','year','touch','processer','storage_capacity','ram_capacity','cosmetic_condition','macbook_functional','battery_health','macbook_powercord','graphics_card','offer')
    list_filter =('macbook_model','screen_size','year','touch','processer','storage_capacity','ram_capacity','cosmetic_condition','macbook_functional','battery_health','macbook_powercord','graphics_card','offer')
    search_field =('macbook_model','screen_size','year','touch','processer','storage_capacity','ram_capacity','cosmetic_condition','macbook_functional','battery_health','macbook_powercord','graphics_card','offer')
class IpadAdmin(admin.ModelAdmin):
    list_display = ('ipad_model','ipad_generation','ipad_carrier','ipad_capacity','ipad_screensize','ipad_condition','offer')
    list_filter = ('ipad_model','ipad_generation','ipad_carrier','ipad_capacity','ipad_screensize','ipad_condition','offer')
    search_field =('ipad_model','ipad_generation','ipad_carrier','ipad_capacity','ipad_screensize','ipad_condition','offer')

class SamsungphoneAdmin(admin.ModelAdmin):
    list_display = ('samsung_model','samsung_capacity','samsung_carrier','samsung_isunlock','samsung_condition','samsung_functional','samsung_screenburn','samsung_powercord','samsung_box','samsung_headset','offer')
    list_filter = ('samsung_model','samsung_capacity','samsung_carrier','samsung_isunlock','samsung_condition','samsung_functional','samsung_screenburn','samsung_powercord','samsung_box','samsung_headset','offer')
    search_field =('samsung_model','samsung_capacity','samsung_carrier','samsung_isunlock','samsung_condition','samsung_functional','samsung_screenburn','samsung_powercord','samsung_box','samsung_headset','offer')

class GooglephoneAdmin(admin.ModelAdmin):
    list_display = ('google_model','google_capacity','google_carrier','google_condition','google_functional','google_powercord','google_box','google_headset','offer')
    list_filter = ('google_model','google_capacity','google_carrier','google_condition','google_functional','google_powercord','google_box','google_headset','offer')
    search_field =('google_model','google_capacity','google_carrier','google_condition','google_functional','google_powercord','google_box','google_headset','offer')
class IpodAdmin(admin.ModelAdmin):
    list_display = ('ipod_model','ipod_capacity','offer','ipod_generation')
    list_filter = ('ipod_model','ipod_capacity','offer','ipod_generation')
    search_field =('ipod_model','ipod_capacity','offer','ipod_generation')

class IwatchAdmin(admin.ModelAdmin):
    list_display = ('iwatch_model','iwatch_carrier','iwatch_size','iwatch_edition_casing','iwatch_band','iwatch_condition','iwatch_functional','iwatch_powercord','iwatch_box','offer')
    list_filter = ('iwatch_model','iwatch_carrier','iwatch_size','iwatch_edition_casing','iwatch_band','iwatch_condition','iwatch_functional','iwatch_powercord','iwatch_box','offer')
    search_field =('iwatch_model','iwatch_carrier','iwatch_size','iwatch_edition_casing','iwatch_band','iwatch_condition','iwatch_functional','iwatch_powercord','iwatch_box','offer')

class DevicesAdmin(admin.ModelAdmin):
    list_display = ('device','info')

class AirpodsAdmin(admin.ModelAdmin):
    list_display = ('airpods_model','charging_case', 'airpods_condition', 'offer')
    list_filter = ('airpods_model','charging_case', 'airpods_condition', 'offer')
    search_field =('airpods_model','charging_case', 'airpods_condition', 'offer')


admin.site.register(Macbook, MacbookAdmin)
admin.site.register(Ipad, IpadAdmin)
admin.site.register(SamsungPhone, SamsungphoneAdmin)
admin.site.register(GooglePhone, GooglephoneAdmin)
admin.site.register(Ipod, IpodAdmin)
admin.site.register(Iwatch, IwatchAdmin)
admin.site.register(Devices, DevicesAdmin)
admin.site.register(Airpods, AirpodsAdmin)

