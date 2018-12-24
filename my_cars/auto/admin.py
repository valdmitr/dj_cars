from django.contrib import admin
from .models import Maker, AutoModel, Color, Body, Person, Advert

class OtherInline(admin.TabularInline):
    model = AutoModel
    extra = 3


class MakerAdmin(admin.ModelAdmin):
    inlines = [OtherInline]


class AdvertAdmin(admin.ModelAdmin):
    list_filter = ['day']


admin.site.register(Body)
admin.site.register(Color)
admin.site.register(Person)
admin.site.register(Maker, MakerAdmin)
admin.site.register(AutoModel)
admin.site.register(Advert, AdvertAdmin)
