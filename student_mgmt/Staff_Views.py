from django.shortcuts import render,redirect
from studentapp.models import*
from django.contrib import messages

def Instructor_Dashboard(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
         return render(request, 'Staff/instructor-dashboard.html' , {'Instructor':Instructor})
    else:
        context={
            'Instructor':Instructor
        }
    return render(request, 'Staff/instructor-dashboard.html' , context)


def Instructor_My_course(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
           return render(request, 'Staff/instructor-manage-course.html',{'Instructor':  Instructor})
    else:
        context={
            'Instructor':Instructor
        }
        return render(request, 'Staff/instructor-manage-course.html',context)
   
def Instructor_Earning(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
           return render(request, 'Staff/instructor-earning.html',{'Instructor':  Instructor})
    else:
        context={
            'Instructor':Instructor
        }
        return render(request, 'Staff/instructor-earning.html',context)

def Instructor_Student(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
           return render(request, 'Staff/Instructor_Student.html',{'Instructor':  Instructor})
    else:
        context={
            'Instructor':Instructor
        }
        return render(request, 'Staff/Instructor_Student.html',context)



def Instructor_Orders(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
           return render(request, 'Staff/instructor-order.html',{'Instructor':  Instructor})
    else:
        context={
            'Instructor':Instructor
        }
        return render(request, 'Staff/instructor-order.html',context)

def Instructor_Reviews(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-review.html',{'Instructor':  Instructor})

def Instructor_Edit_Profile(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
           return render(request, 'Staff/instructor-edit-profile.html',{'Instructor':  Instructor})
    else:
        context={
            'Instructor':Instructor
        }

        
        return render(request, 'Staff/instructor-edit-profile.html',context)
       

def Staff_UPDATE(request):
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
            return redirect('/staff')
        except :
            # messages.error(request, "Failed to Update Your Profile")
            pass
    # user=request.user.id
    # print(user)
    # user=CustomUser.objects.all().filter(id=user)
    return render(request, 'Staff/instructor-edit-profile.html')
   




# def Staff_UPDATE(request):
#     user=request.user.id
#     print(user)
#     if request.method=='POST':
#             instructor_id = request.POST.get('instructor_id')
#             print(instructor_id)
#             profile_pic=request.FILES.get('profile_pic')
#             username=request.POST.get('username')
#             first_name=request.POST.get('first_name')
#             last_name=request.POST.get('last_name')
#             email=request.POST.get('email')
#             print(profile_pic ,username , first_name ,last_name ,email)
#             user = CustomUser.objects.get(id=instructor_id)
#             user.username=username ,
#             user.first_name=first_name , 
#             user.last_name=last_name , 
#             user.email=email,
#             user.save()
#             messages.success(request , "Recoard Successfully Update!!")
#             return redirect('/staff')
#     return render(request, 'Staff/instructor-edit-profile.html',{'user':user})


def Instructor_Payout(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
           return render(request, 'Staff/instructor-payout.html',{'Instructor':  Instructor})
    else:
        context={
            'Instructor':Instructor
        }
        return render(request, 'Staff/instructor-payout.html',context)
   
def Create_course(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
           return render(request,'Staff/instructor-create-course.html',{'Instructor':  Instructor})
    else:
        context={
            'Instructor':Instructor
        }
        return render(request, 'Staff/instructor-create-course.html',context)



def Instructor_Settings(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-setting.html',{'Instructor':  Instructor})

def Instructor_Delete_Profile(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-delete-account.html',{'Instructor':  Instructor})

def Instructor_Sign_Out(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'login.html',{'Instructor':  Instructor})
