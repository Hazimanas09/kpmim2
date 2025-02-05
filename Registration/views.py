from django.shortcuts import render
from Registration.models import Course, Mentor  # Import your Course model
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    context = {
        'fathername': "Anas",
        'greeting': 1,
    }
    return render(request, "index.html", context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST.get('code')
        c_desc = request.POST.get('description')
        data = Course(code=c_code, description=c_desc)
        data.save()
        allcourse = Course.objects.all().values()
        dict = {
        'message' : 'Data Save',
        'allcourse' : allcourse,
            }
    else:
        allcourse = Course.objects.all().values()
        dict = {
        'message' : 'Unsuccess',
        'allcourse' : allcourse,
             } 
        
        
        
    return render(request, "course.html", dict)

def mentor(request):
    if request.method == 'POST':
        m_code = request.POST.get('mentorCd')
        m_name = request.POST.get('mentorName')
        m_email = request.POST.get('mentorEmail')
        data = Mentor(mentorCd = m_code, mentorName = m_name, mentorEmail = m_email)
        data.save()
        allmentor = Mentor.objects.all().values()
        dict = {
            'message' : 'Save Data',
            'allmentor' : allmentor,
        }
    
    else:
        allmentor = Mentor.objects.all().values()
        dict = {
            'message' : "Unsuccess",
            'allcourse' : allmentor,
            
        }
    return render(request, "mentor.html", dict)

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')
        
        if c_code:
            
            data = Course.objects.filter(code = c_code.upper())
        
        else:
            data = None
            
        
        context = {
            'data':data
        }
    
    return render(request,"search_course.html",context)

def search_mentor(request):
    if request.method == 'GET':
        m_code = request.GET.get('m_code')
        
        if m_code :
            
            data = Mentor.objects.filter(mentorCd = m_code.upper())
            
        else :
            
            data = None
            
        context = {
            'data' : data
        }
            
    return render(request, "search_mentor.html",context)

def update_course(request,code):
    
    data = Course.objects.get(code=code)
    
    dict = {
        'data':data
    }
    
    return render(request, "update_course.html", dict)

def delete_course(code) :
    
    data = Course.objects.get(code=code)
    
    data.delete()
    
    return HttpResponseRedirect(reverse('course'))

def save_update_course(request,code):
    c_desc = request.POST['desc']
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect (reverse("course"))
