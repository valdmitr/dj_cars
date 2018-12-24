from django.contrib import admin
from .models import Maker, AutoModel, Color, Body, Person, Advert

# class OtherInline(admin.TabularInline):
#     model = AutoModel
#     extra = 3
#
#
# class MakerAdmin(admin.ModelAdmin):
#     inlines = [OtherInline]


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_maker', 'automodel', 'body', 'color', 'ad_user', 'year', 'day', 'price')
    list_filter = ['day']
    # search_fields = ['maker', 'automodel']
    # search_fields = ['get_maker']


admin.site.register(Body)
admin.site.register(Color)
admin.site.register(Person)
admin.site.register(Maker) #MakerAdmin)
admin.site.register(AutoModel)
admin.site.register(Advert, AdvertAdmin)
