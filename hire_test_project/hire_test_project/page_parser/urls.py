from django.conf.urls import url
from .views import Tags

urlpatterns = [
    url('tags$', Tags.as_view())
]
