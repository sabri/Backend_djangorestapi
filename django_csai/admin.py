from django.contrib import admin
from .models import Dictionary, Document


class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ['document']

    class Meta:
        model = True


class DictionaryModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'document', 'label', 'start', 'end']

    class Meta:
        model = True


admin.site.register(Dictionary, DictionaryModelAdmin)
admin.site.register(Document, DocumentModelAdmin)

