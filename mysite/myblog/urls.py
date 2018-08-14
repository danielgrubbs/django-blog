from django.conf.urls import url
from myblog.views import stub_view, list_view, detail_view


urlpatterns = [
    url(r'^$', list_view, name="blog_index"),
    url(r'^posts/(\d+)/$', detail_view, name="blog_detail"),
]
