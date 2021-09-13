from django.urls import path
from.import views

app_name = 'mainapp'

urlpatterns = [
	path('',views.index, name='Home'),
	path('about/',views.about, name='About'),
	path('about/<str:sheikh_slug>',views.scholar, name='scholarDetailPage'),
	path('blog/',views.blog, name='Blog'),
	path('contact/',views.contact, name='Contact'),
	path('gallery/',views.gallery, name='gallery'),
	path('audio/',views.audio, name='audio'),
	path('blog/<str:blog_slug>',views.blog_detail, name='blogDetailPage'),
	path('ramadan/',views.ramadan, name='ramadan'),
]