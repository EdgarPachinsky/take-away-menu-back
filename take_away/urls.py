"""
URL configuration for take_away project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path, include

from apps.core.urls import generate_url
from apps.product.urls import urlpatterns as product_category_urls
from apps.product.urls import urlpatterns as product_urls


admin.site.site_header = f'{settings.SITE_NAME} Admin'
admin.site.site_title = f'{settings.SITE_NAME} Admin'
admin.site.index_title = 'Welcome to Admin Portal'

admin.site.unregister(Group)

urlpatterns = [
    path('admin/', admin.site.urls),
    generate_url('product-category/', include(product_category_urls)),
    generate_url('product/', include(product_urls)),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

# http://localhost:8000/uploads/product/1/Screen_Shot_2024-04-21_at_19.15.31.png
