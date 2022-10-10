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

router_room = routers.SimpleRouter()
router_room.register(r'rooms', RoomViewSet)

router_departures = routers.SimpleRouter()
router_departures.register(r'depart', DeparturesViewSet)

router_payments = routers.SimpleRouter()
router_payments.register(r'payments', PaymentsViewSet)

router_refund = routers.SimpleRouter()
router_refund.register(r'refunds', RefundsViewSet)

router_spend_admin = routers.SimpleRouter()
router_spend_admin.register(r'spend-admin', SpendingAdminViewSet)

router_spend_boss = routers.SimpleRouter()
router_spend_boss.register(r'spend-boss', SpendingBossViewSet)

router_spend_hostel = routers.SimpleRouter()
router_spend_hostel.register(r'spend-hostel', SpendingHostelViewSet)

urlpatterns = [
    path('', include(router_profile.urls)),
    path('', include(router_room.urls)),
    path('', include(router_departures.urls)),
    path('', include(router_payments.urls)),
    path('', include(router_refund.urls)),
    path('', include(router_spend_admin.urls)),
    path('', include(router_spend_boss.urls)),
    path('', include(router_spend_hostel.urls)),
]