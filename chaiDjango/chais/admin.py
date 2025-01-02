from django.contrib import admin
from .models import ChaiVarity,ChaiCertificate,ChaiReview,Store


# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model =ChaiReview
    extra =2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display =('name','type','date_added')
    inlines =[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display =('name','location')
    filter_horizontal =('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display =('chai','certificate_number')

admin.site.register(ChaiVarity,ChaiVarityAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
admin.site.register(ChaiReview,ChaiReviewInline)

