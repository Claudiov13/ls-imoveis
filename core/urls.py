# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home pública
    path('', views.home, name='home'),

    # Proprietários
    path('proprietarios/',           views.ProprietarioList.as_view(),   name='prop_list'),
    path('proprietarios/novo/',      views.ProprietarioCreate.as_view(), name='prop_create'),
    path('proprietarios/<int:pk>/editar/',  views.ProprietarioUpdate.as_view(), name='prop_edit'),
    path('proprietarios/<int:pk>/excluir/', views.ProprietarioDelete.as_view(), name='prop_delete'),

    # Locatários
    path('locatarios/',           views.LocatarioList.as_view(),   name='loc_list'),
    path('locatarios/novo/',      views.LocatarioCreate.as_view(), name='loc_create'),
    path('locatarios/<int:pk>/editar/',  views.LocatarioUpdate.as_view(), name='loc_edit'),
    path('locatarios/<int:pk>/excluir/', views.LocatarioDelete.as_view(), name='loc_delete'),

    # Imóveis
    path('imoveis/',           views.ImovelList.as_view(),   name='imv_list'),
    path('imoveis/novo/',      views.ImovelCreate.as_view(), name='imv_create'),
    path('imoveis/<int:pk>/editar/',  views.ImovelUpdate.as_view(), name='imv_edit'),
    path('imoveis/<int:pk>/excluir/', views.ImovelDelete.as_view(), name='imv_delete'),
]

