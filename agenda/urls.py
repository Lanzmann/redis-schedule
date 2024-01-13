from rest_framework.routers import DefaultRouter
from .views import AgendaViewSet

router = DefaultRouter()
router.register("agenda", AgendaViewSet, basename="agenda")

urlpatterns = router.urls