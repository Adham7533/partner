from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from taxi import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('taxi/', include('taxi.urls')),
    path('api/', include('api.urls')),
]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

