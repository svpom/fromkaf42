from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^summary-about-trees-root/$', views.summary_about_trees_root,
        name='summary_about_trees_root'),
]
