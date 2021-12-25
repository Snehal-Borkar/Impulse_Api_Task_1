from django.contrib import admin
from .models import Sample_Details
# Register your models here.


class FooAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt',)


admin.site.register(Sample_Details, FooAdmin)
# admin.site.register(Sample_Details)