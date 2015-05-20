from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^article/(?P<slug>\S+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoryHome, name='category_home'),
    url(r'^$', views.Index, name='index'),
    url(r'^archives/', views.Archives, name='archives'),
    url(r'^works/', views.Works, name='works'),
    url(r'^about/', views.About, name='about'),
    url(r'^', views.Index, name='index'),
)
