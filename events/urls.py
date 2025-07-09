from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path('', views.event_list, name='events'),
   path('event/<int:event_id>/registration/', views.event_registration, name='event_registration'), # noqa
   path('event/<int:event_id>/confirmed/', views.event_confirmed, name='event_confirmed'), # noqa
   path('event/<int:event_id>', views.event_detail, name='event_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
