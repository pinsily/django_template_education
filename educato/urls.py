from django.urls import path

from educato import views

app_name = "educato"

urlpatterns = [
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses-details/', views.courses_details, name='courses_details'),
    path('events/', views.events, name='events'),
    path('events-details/', views.events_details, name='events_details'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery_detail/', views.gallery_detail, name='gallery_detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('team/', views.team, name='team'),
    path('team_detail/', views.team_detail, name='team_detail'),
    path('faq/', views.faq, name='faq'),
    path('shop/', views.shop, name='shop'),
    path('shop_details/', views.shop_details, name='shop_details'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('services_detail/', views.services_detail, name='services_detail'),

]