from django.urls import path

from . import views

app_name = 'management'
urlpatterns = [
    path("leden/", views.LidTableView.as_view(), name='leden'),
    path("leden/<int:pk>/", views.LidEditView.as_view(), name="lid"),
    path("leden/<int:pk>/verwijder", views.verwijder_lid, name="verwijder_lid"),
    path('lid_modal/<int:pk>/', views.LidModalView.as_view(), name='lid_modal'),
    path("leden/verwerk/", views.verwerk_leden, name="verwerk_leden"),
    path("leden/nieuw/", views.LidNewView.as_view(), name='nieuw_lid'),
    path("ouder/new/", views.create_ouder, name="new_ouder"),
    path("ploegen/", views.PloegListView.as_view(), name='ploegen'),
    path("ploegen/new/", views.create_ploeg, name="new_ploeg"),
    path("ploegen/<int:pk>/select/", views.PloegSelectView.as_view(), name='ploeg_select'),
    path("ploegen/<int:pk>/view/", views.PloegView.as_view(), name='ploeg_view'),
    path("ploegen/<int:pk>/export/", views.export_ploeg, name='ploeg_export'),
    path("betalingen/stuur_mail/<int:pk>/", views.stuur_mail, name="betalingen_mail"),
    path("betalingen/", views.BetalingTableView.as_view(), name="betalingen"),
    path('', views.IndexView.as_view(), name='index'),
]
