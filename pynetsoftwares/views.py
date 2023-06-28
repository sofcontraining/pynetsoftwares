from django.shortcuts import render   
from .models import Userquery, Contactform 
from .forms import UserContactForm
from django.views import View
from django.contrib import messages
from .models import Addcourses, Addservice, Testimonial

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        course = request.POST['course']
        query = Userquery(name=name, phone=phone, email=email, course=course)
        query.save()
        messages.success(request, 'Form submitted successfully')
    return render(request, "pynetsoftwares/home.html", {})

def about(request):
    return render(request, "pynetsoftwares/about-us.html", {}) 

def contact(request):
    if request.method == "POST":
        form = UserContactForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            name = request.POST['name']
            mobile = request.POST['mobile']
            email = request.POST['email']
            course = request.POST['course']
            
            
    return render(request, "pynetsoftwares/contact.html", {}) 

def features(request):
    return render(request, "pynetsoftwares/features.html", {}) 

# def courses(request):
#     return render(request, "pynetsoftwares/courses.html", {})
class CourseView(View):
    def get(self, request):
        frontends = Addcourses.objects.filter(coursecategory='frontends')
        programming = Addcourses.objects.filter(coursecategory='programming')
        frameworks = Addcourses.objects.filter(coursecategory='frameworks')
        databases = Addcourses.objects.filter(coursecategory='databases')

        return render(request, 'pynetsoftwares/courses.html', {'frontends':frontends, 'programming':programming, 'frameworks':frameworks, 'databases':databases})

def projects(request):
    return render(request, "pynetsoftwares/projects.html", {}) 

class ServicesView(View):
    def get(self, request):
        AllServices = Addservice.objects.all()
        context = {'AllServices': AllServices, 
        'item':range(len(AllServices))}
        return render(request, "pynetsoftwares/services.html", context) 

# def services(request):
#     return render(request, "pynetsoftwares/services.html", {}) 

class TestimonialDetailsView(View):
    def get(self, request):
        AllTestimonials = Testimonial.objects.all()
        test = {'AllTestimonials':AllTestimonials}
        return render(request, "pynetsoftwares/testimonials.html", test)    

# def coursedetails(request, slug):
#     course = Addcourses.objects.filter(slug=slug).first()
#     context = {'course':course}
#     return render(request, 'pynetsoftwares/coursedetails.html', context)

class CourseDetailView(View):
    def get(self, request, slug):
        course = Addcourses.objects.all().get(slug=slug)
        return render(request, 'pynetsoftwares/coursedetails.html', {'course':course})
        if request.method == "POST":
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            course = request.POST['course']
            query = Userquery(name=name, phone=phone, email=email, course=course)
            query.save()
            messages.success(request, 'Form submitted successfully')
        return render(request, 'pynetsoftwares/coursedetails.html', {'course':course})
        
    
        


class ServiceDetailView(View):
    def get(self, request, serviceslug):
        # page = Addservice.objects.all().get(serviceslug=serviceslug)
        page = Addservice.objects.filter(serviceslug=serviceslug).first()
        return render(request, 'pynetsoftwares/servicesdetails.html', {'page':page})

def test(req):
    course = Addcourses.objects.all()
    return render(req, "pynetsoftwares/test.html", {'courses':course})