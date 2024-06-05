from django.contrib import admin
from .models import Ad, Advertiser, AdSpaceProvider, Consumer

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'advertiser', 'ad_space_provider', 'url')
    search_fields = ('id', 'advertiser__name', 'ad_space_provider__name')

@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email')
    search_fields = ('id', 'name')

@admin.register(AdSpaceProvider)
class AdSpaceProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email')
    search_fields = ('id', 'name')

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'ad')
    search_fields = ('name', 'phone_number', 'email', 'ad__id')