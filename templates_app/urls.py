from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemplateComponentViewSet
from .views import RenderComponentView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)



router = DefaultRouter()
router.register(r'components', TemplateComponentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('render/<int:pk>/', RenderComponentView.as_view(), name='render_component'),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
