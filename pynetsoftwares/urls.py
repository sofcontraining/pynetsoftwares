from django.urls import path
from pynetsoftwares import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [path('', views.index, name='index'),
                path('home', views.index, name='home'),
                path('test', views.test),
                path('about-us', views.about, name='about'),
                path('contact', views.contact, name='contact'),
                path('features', views.features),
                path('courses', views.CourseView.as_view(), name='courses'),
                path('projects', views.projects),
                path('services', views.ServicesView.as_view(), name='services'),
                path('testimonials', views.TestimonialDetailsView.as_view(), name='testimonials'),
                path('courses/<str:slug>', views.CourseDetailView.as_view(), name='coursedetails'),
                path('services/<str:serviceslug>',views.ServiceDetailView.as_view(), name='servicesdetails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)