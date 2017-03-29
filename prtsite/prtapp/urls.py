from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^summary-about-trees-root/$', views.summary_about_trees_root,
        name='summary_about_trees_root'),
    url(r'^cut-method/$', views.cut_method, name='cut_method'),
    url(r'^xhr-cut$', views.xhr_cut, name='xhr_cut'),
    url(r'^based-on-tops-height/$', views.based_on_tops_height, name='based_on_tops_height'),
    url(r'^xhr-height$', views.xhr_height, name='xhr_height'),
    url(r'^summary-about-stegano/$', views.summary_about_stegano, name='summary_about_stegano'),
    url(r'^stegano-in-images/$', views.stegano_in_images, name='stegano_in_images'),
    url(r'^upload-image-to-encode/$', views.upload_image_to_encode, name='upload_image_to_encode'),
    url(r'^upload-image-to-decode/$', views.upload_image_to_decode, name='upload_image_to_decode'),
    url(r'^stegano-in-videos/$', views.stegano_in_videos, name='stegano_in_videos'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]
