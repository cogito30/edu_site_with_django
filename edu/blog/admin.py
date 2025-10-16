from django.contrib import admin

"""
class ModelNameInline(admin.StackedInline):
    model = ModelName
    extra = 1

@admin.register(model_name)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', ...)
    list_filter = ('field1', 'field2', ...)
    search_fields = ('field1', 'field2')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModelNameInline]
"""