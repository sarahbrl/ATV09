from django.contrib import admin
from .models import Conteudo, Menu

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'ativo')
    prepopulated_fields = {'slug': ('titulo',)}
    list_filter = ('ativo',)
    search_fields = ('titulo', 'conteudo_html')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'ordem', 'ativo', 'conteudo', 'url_externa')
    list_filter = ('tipo', 'ativo')
    list_editable = ('ordem', 'ativo')
    search_fields = ('titulo',)
