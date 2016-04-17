from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'transactions', views.TransactionViewSet)
# urlpatters = router.urls

urlpatterns = [
    # url(r'get_user/(?P<username>[A-Za-z]+)$', views.get_user),
    # url(r'get_item/?', views.get_items_all),
    # url(r'get_item/id/(?P<id>[0-9]+)$', views.get_item_id),
    # url(r'get_item/owner/(?P<username>[A-Za-z0-9]+)$', views.get_items_owner),
    # url(r'get_transaction/?', views.get_transactions_all),
    # url(r'get_transaction/id/(?P<id>[0-9]+)$', views.get_transaction_id),
    # url(r'get_transaction/owner/(?P<username>[A-Za-z0-9]+)$', views.get_transactions_owner),
    url(r'^register', views.register_account),
    url(r'^nearest_items/(?P<lat>)/(?P<lon>)', views.nearest_items),
    url(r'^', include(router.urls)),
    url(r'^items/by_owner/(?P<username>.+)/?$',views.ItemList.as_view()),
    url(r'^transaction/by_owner/(?P<username>.+)/?$',views.TransactionList.as_view()),
]
