from django.contrib import admin
from passagens.models import Voo, Status, Clientes

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')
    list_display_links = ('id','status')
    search_fields = ('id','status_compra')
    list_per_page = 10

admin.site.register(Status, StatusAdmin)

class VooAdmin(admin.ModelAdmin):
   list_display = ('id','numero_do_voo','preco','data_ida','data_volta','companhia_ida','companhia_volta','passageiro')
   list_display_links = ('id','numero_do_voo','preco','passageiro')
   search_fields = ('id','data_ida','companhia_ida')
   list_per_page = 10

admin.site.register(Voo, VooAdmin)

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id','primeiro_nome','sobrenome','status_compra')
    list_display_links = ('id','primeiro_nome','sobrenome')
    search_fields = ('id','primeiro_nome','sobrenome')
    list_per_page = 10

admin.site.register(Clientes, ClientesAdmin)





