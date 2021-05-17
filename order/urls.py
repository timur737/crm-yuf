from django.urls import path
#CBV
from .views import CreateForNew
#for static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', CreateForNew.as_view(extra_context={'page_title': 'Создание заказа', 'header': 'Заказ'}),
         name='order_create'),
] + static(settings.STATIC_URL)
