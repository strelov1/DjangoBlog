from django.conf.urls import url
from .views import ArticleIndex, ArticleDetail

urlpatterns = [
    url(r'^$', ArticleIndex.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', ArticleDetail.as_view(), name='view'),
]
