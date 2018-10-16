from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^index/$", views.index, name="index"),
    url(r"^add_article/$", views.add_article, name="add_article"),
    url(r"^delete_article/$", views.delete_article, name="delete_article"),
    url(r"^list_article/$", views.list_article, name="list_article"),
    url(r"^successfully/$", views.successfully, name="successfully"),
    url(r"^failed/$", views.failed, name="failed"),
    url(r"^(?P<u_id>\d+)/update/$", views.update, name="update"),
    url(r"^show/(\d+)/$", views.show, name="show"),
    url(r"^login/$", views.login, name="login"),
    url(r"^logout/$", views.logout, name="logout"),
    url(r"^show/(\d+)/$", views.show, name="show"),

]