from django.contrib import admin
from .models import Maker, AutoModel, Color, Body, Person, Advert, MakerAndModel

class OtherInline(admin.TabularInline):
    model = MakerAndModel
    extra = 3


class MakerAdmin(admin.ModelAdmin):
    inlines = [OtherInline]


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_maker', 'get_model', 'body', 'color', 'ad_user', 'year', 'day', 'price', 'status', 'phone')
    list_filter = ['status','day', 'maker', 'body', 'color']
    search_fields = ['maker__name', 'automodel__name']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "body":
            kwargs["queryset"] = Body.objects.order_by('name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter().order_by('maker__name')


admin.site.register(Body)
admin.site.register(Color)
admin.site.register(Person)
admin.site.register(Maker, MakerAdmin)
admin.site.register(AutoModel)
admin.site.register(Advert, AdvertAdmin)
