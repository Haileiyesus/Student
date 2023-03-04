# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddStudentForm
from student_management_app.EmailBackEnd import EmailBackEnd
from .models import LoginType
from .models import Courses

# def search_button(request):
#     if request.method == "POST":
#          searched = request.POST['searched']
#          Course = Courses,object.filter(id__contains=searched)
#          return render(request,'hod_template/manage_course_template.html', {
#           'searched':searched,
#           'Course':Course})
#     else:
#          return render(request,'hod_template/manage_student_template.html',{})
def home(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, 'login.html')



def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        print(user)
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def password_reset(request):
    return render(request, "password_reset.html")

# def add_students(request):
#     return render(request, "add_students.html")
def add_students(request):
    log = LoginType.objects.get(id=1)
    form = AddStudentForm()
    context = {
        "form": form
    }
    if (log.login_type == True):
        return render(request, 'add_students.html', context)
    else:
        return redirect('login')

    

