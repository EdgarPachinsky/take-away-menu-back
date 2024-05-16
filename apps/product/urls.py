from apps.core.urls import router

from apps.product import views

router.register('', views.ProductViewSet, basename='product')
urlpatterns = router.urls
