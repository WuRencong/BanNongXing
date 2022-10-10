from django import urls
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.urls.conf import include
from . import views

urlpatterns = [
    # http://localhost:8000/home/...
    path('Master_template', views.getMasterTemplate, name="master_template"),
    path('about_us', views.getAboutUsPage, name="about_us"),
    path('action_news', views.getActionnewsPage, name="action_news"),
    path('Crops/<str:crop_type_name>', views.getSeedMess, name="crop_type"),
    path('Search/<str:crop_type_name>', views.search, name="search"),
    path('SeedDetail/<int:crop_seed_id>', views.getSeedDetail, name="crop_seed_id"),
    path('SoilDetail/<int:crop_soil_id>', views.getSoilDetail, name="crop_soil_id"),
    path('SubSoil/<int:subsoil_id>', views.getSubSoil, name="subsoil_id"),
    path('SoilSeedDetail/<int:soil_seed_id>', views.getSoilSeed, name="soil_seed_id"),
    path('Create', views.getCreatePage, name="create"),
    path('map', views.getMapPage, name="map"),
    path('DataPlan', views.getDataPlanPage, name="data_plan"),
    path('ProductCenter', views.getProductCenterPage, name="product_center"),
    path('login', views.getLoginPage, name="login"),
    path('Liaison', views.getLiaisonPage, name="liaison"),
    path('Legal', views.getLegalPage, name="legal"),
    path('Information', views.getInformationPage, name="information"),
    path('index', views.getIndexPage, name="index"),
    path('News/<int:new_pk>', views.gatNewTemPage, name="new_tem"),
    path('NewType/<int:new_type_pk>', views.gatNewTypeTemPage, name="new_type_tem")
]
