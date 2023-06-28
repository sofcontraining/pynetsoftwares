import string
import random

from django.db import models
from ckeditor.fields import RichTextField

class Userquery(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Enquiry from ' + self.name + ' ' + self.phone + ' ' + self.email + ' ' + self.course

COURSE_CATEGORY = (
    ('frontends', 'frontends'),
    ('programming', 'programming'),
    ('frameworks', 'frameworks'),
    ('databases', 'databases'),
    ('marketing', 'marketing'),
)


class Addcourses(models.Model):
    coursename = models.CharField(max_length=100)
    courseduration = models.FloatField()
    liveprojects = models.IntegerField()
    eligibility = models.CharField(max_length=100)
    trainingmode = models.CharField(max_length=50)
    heading = models.CharField(max_length=100)
    slug = models.SlugField(max_length=500)
    coursecategory = models.CharField(choices = COURSE_CATEGORY, max_length=100)
    courseintroduction = RichTextField()
    coursecontent = RichTextField()
    courseimages = models.ImageField(upload_to='courseimg')
    # category = models.CharField(choices = CATEGORY_CHOICES, max_length=2)
    # product_images = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.coursename)

class Addservice(models.Model):
    servicetitle = models.CharField(max_length=100)
    serviceslug = models.SlugField(max_length=500)
    servicecontent = RichTextField()
    serviceimages = models.ImageField(upload_to='courseimg')
    # category = models.CharField(choices = CATEGORY_CHOICES, max_length=2)
    # product_images = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.servicetitle)

class Contactform(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    msg = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.mobile + ' ' + self.course

class Testimonial(models.Model):
    student_name = models.CharField(max_length=50)
    course_name =  models.CharField(max_length=50)
    review_heading = models.CharField(max_length=50)
    review_content = models.CharField(max_length=200)
    student_images = models.ImageField(upload_to='studentimg')
