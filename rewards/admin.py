from django.contrib import admin
from .models import Rewards,UserRewards
# Register your models here.
class RewardsAdmin(admin.ModelAdmin):
    list_display = ('code','discount','description','bonus','condition')
    list_filter = ('code','discount','description','bonus','condition')
    search_field =('code','discount','description','bonus','condition')



class UserRewardsAdmin(admin.ModelAdmin):
    list_display = ('user','promocode',)
    list_filter = ('user','promocode',)
    search_field = ('user','promocode',)

admin.site.register(Rewards,RewardsAdmin)
admin.site.register(UserRewards, UserRewardsAdmin)