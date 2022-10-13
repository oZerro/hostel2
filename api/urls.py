from django.urls import path, include
from rest_framework import routers

from .views import (
    ProfileViewSet,
    RoomViewSet,
    DeparturesViewSet,
    PaymentsViewSet,
    RefundsViewSet,
    SpendingAdminViewSet,
    SpendingBossViewSet,
    SpendingHostelViewSet,
)



router_profile = routers.SimpleRouter()
router_profile.register(r'profile', ProfileViewSet)
router_profile.register(r'rooms', RoomViewSet)
router_profile.register(r'depart', DeparturesViewSet)
router_profile.register(r'payments', PaymentsViewSet)
router_profile.register(r'refunds', RefundsViewSet)
router_profile.register(r'spend-admin', SpendingAdminViewSet)
router_profile.register(r'spend-boss', SpendingBossViewSet)
router_profile.register(r'spend-hostel', SpendingHostelViewSet)

urlpatterns = router_profile.urls
