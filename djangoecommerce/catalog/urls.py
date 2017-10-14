

from django.conf.urls import url

# de onde estou import as views
from . import views

urlpatterns = [
    url(r'^$',views.product_list, name='product_list'),
]