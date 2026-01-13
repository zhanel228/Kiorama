from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import news_list  # список новостей на главную

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_list, name='home'),         # главная страница /
    path('', include('news.urls')),           # остальные URL приложения news
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
]

# Чтобы медиа-файлы работали при DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
