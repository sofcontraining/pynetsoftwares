from django.contrib import admin
from . models import (
    Userquery,
    Addcourses,
    Addservice,
    Contactform,
    Testimonial
)

admin.site.register(Userquery)

@admin.register(Addcourses)
class AddcoursesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'coursename', 'courseduration', 'liveprojects', 'eligibility', 'trainingmode', 'heading', 'slug', 'coursecategory','courseintroduction', 'coursecontent','courseimages']

@admin.register(Addservice)
class AddserviceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'servicetitle','serviceslug', 'servicecontent', 'serviceimages']

admin.site.register(Contactform)
@admin.register(Testimonial)
class AddtestimonialsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'course_name', 'review_heading', 'review_content', 'student_images']