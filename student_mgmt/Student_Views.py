from django.shortcuts import render,redirect
from studentapp.models import*
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# def index(request):
    # return render(request, 'Student/home.html')

def Student_dashboard(request):
    student=request.user
    if Student.objects.all()==student:
        while(True):
         return render(request, 'Student/student-dashboard.html' , {'student':student})
    else:
        context={
            'student':student
        }
    return render(request, 'Student/student-dashboard.html' , context)

def Student_my_subscriptions(request):
    return render(request, 'Student/student-subscription.html')
def Student_my_course(request):
    student=request.user
    if Student.objects.all()==student:
        while(True):
         return render(request, 'Student/student-course-list.html' , {'student':student})
    else:
        context={
            'student':student
        }
    return render(request, 'Student/student-course-list.html' , context)

def Student_payment_info(request):
    student=request.user
    if Student.objects.all()==student:
        while(True):
         return render(request, 'Student/student-payment-info.html' , {'student':student})
    else:
        context={
            'student':student
        }
    return render(request, 'Student/student-payment-info.html' , context)
def Student_wishlist(request):
    return render(request, 'Student/student-bookmark.html')

def Student_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        
        print(first_name)
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic
            if password:
                 if password !=None and password != "":
                   customuser.set_password(password)
                   customuser.save()
                   return redirect('/LOGIN')
            customuser.save()
            
            messages.success(request, "Your Profile Updated Successfully !!")
            # return HttpResponseRedirect(reverse(""))
            # return redirect('')
        except :
            # messages.error(request, "Failed to Update Your Profile")
            pass
    # user=request.user.id
    # print(user)
    # user=CustomUser.objects.all().filter(id=user)
    return render(request, 'Student/student-edit-profile.html')

def Student_Edit_Profile(request):
    student=request.user
    # stu = Student.objects.all()
    if Student.objects.all()==student:
        while(True):
         return render(request,'Student/student-edit-profile.html' , {'student':student})
    else:
        context={
            'student':student,
            # 'stu':stu
        }
    return render(request, 'Student/student-edit-profile.html', context)
    








def Student_settings(request):
    return render(request, 'Student/instructor-setting.html')
def Student_Delete_Profile(request):
    return render(request, 'Student/instructor-delete-account.html')
def Student_Sign_Out(request):
    return render(request, 'login.html')
