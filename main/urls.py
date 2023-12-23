from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('main.html', views.main),
    path('japan.html', views.japan),
    path('china.html', views.china),
    path('south_korea.html', views.south_korea),
    path('add_country.html', views.add),
    path('models.html', views.models),
    path('', views.main),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)