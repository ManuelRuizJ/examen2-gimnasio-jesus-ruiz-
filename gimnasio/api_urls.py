from rest_framework.routers import DefaultRouter

from .api_views import ClaseViewSet, SocioViewSet

router = DefaultRouter()
router.register("socios", SocioViewSet)
router.register("clases", ClaseViewSet)

urlpatterns = router.urls
