from apps.core.urls import router

from apps.product_category import views

router.register('', views.ProductCategoryViewSet, basename='product')
urlpatterns = router.urls
