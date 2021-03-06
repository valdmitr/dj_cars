from django.contrib import admin
from .models import Maker, AutoModel, Color, Body, Person, Advert, MakerAndModel
from .forms import ForGroupForm


class OtherInline(admin.TabularInline):
    model = MakerAndModel
    extra = 3


class MakerAdmin(admin.ModelAdmin):
    """
    Для каждого производителя
    Включаем 3 поля для моделей авто
    """
    inlines = [OtherInline]


class AdvertAdmin(admin.ModelAdmin):
    """
    кастомная админка для объявлений
    """
    list_display = ('__str__', 'get_maker', 'get_model', 'body', 'color',
                    'ad_user', 'year', 'day', 'price', 'status', 'phone')
    list_filter = ['status', 'day', 'maker', 'body', 'color']
    search_fields = ['maker__name', 'automodel__name']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        настраиваем сортировку объявлений в поле body
        """
        if db_field.name == "body":
            kwargs["queryset"] = Body.objects.order_by('name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """
        переопределяем queryset для модераторов, чтобы они видели
        только активные объявления
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(status=True)

    def get_form(self, request, obj=None, change=False, **kwargs):
        """
        переопределяем  форму для всех модераторов, кроме суперпользователя
        """
        if not request.user.is_superuser:
            self.form = ForGroupForm
            return self.form

        return super().get_form(request, obj=None, change=False, **kwargs)
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter().order_by('maker__name')


admin.site.register(Body)
admin.site.register(Color)
admin.site.register(Person)
admin.site.register(Maker, MakerAdmin)
admin.site.register(AutoModel)
admin.site.register(Advert, AdvertAdmin)
