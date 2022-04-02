
from sre_constants import SUCCESS
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views, HOD_Views, Staff_Views,Student_Views  
from student_mgmt.HOD_Views import ( hod_profile, Student_list  ,HOD_UPDATE,all_category,course_category_update,course_category_delete)
from student_mgmt.views import*
from student_mgmt.Staff_Views import*


# def trigger_error(request):
#     division_by_zero = 1 / 0
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('__debug__/', include('debug_toolbar.urls')),
    # path('', views.base,name='base')
    #######Mycode##########
    path('hodprofile/', hod_profile, name='hodprofile'),
    path('staff', Staff_UPDATE, name='staff'),
    

    # path('Instructor/<int:id>', pk_Instructor, name='pk_Instructor'),

    path('studentlist/', Student_list, name='studentlist'),
    path('hodupdate/<str:id>/', HOD_UPDATE, name='hodupdate'),
    path('all_category', all_category, name='all_category'),
    path('course_category_update/<int:id>/',course_category_update, name='course_category_update'),
    path('course_category_delete/<int:id>/',course_category_delete, name='course_category_delete'),

    






    #######EndMycode#######

    #Login Path
    path('', views.Home, name='Home'),
    path('LOGIN', views.LOGIN, name='LOGIN'),
    path('courses', views.courses, name='courses'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('doLogout', views.doLogout, name='doLogout'), 
    path('rightside/<int:pk>', views.rightside, name='rightside'),
    # path('right/<int:pk>', views.right, name='right'), 


    # This is HOD Panel Url
    path('HOD/Home', HOD_Views.HOME,name='hod_home'),

    #CRUD STUDENT
    path('HOD/Student/View', HOD_Views.VIEW_STUDENT,name="view_student"),
    path('HOD/Student/Add', HOD_Views.ADD_STUDENT,name='add_student'),
    path('HOD/Student/Edit/<str:id>', HOD_Views.EDIT_STUDENT,name="edit_student"),
    path('HOD/Student/Update/', HOD_Views.UPDATE_STUDENT,name="update_student"),
    path('HOD/Student/DELETE/<str:admin>', HOD_Views.DELETE_STUDENT,name="delete_student"),
    #END CRUD STUDENT

    #####This is HOD Panel Url Course#######

    #CRUD COURSE

    path('Buy_Course/<int:id>', views.Buy_Course, name='Buy_Course'),
    path('success', views.success, name='success'),
    path('Add_To_Cart', views.Add_To_Cart, name='Add_To_Cart'),
    path('placeorder/', views.PLACEORDER, name='place_order'),

    path('HOD/Course/Add/', HOD_Views.ADD_COURSE,name="add_course"),
    path('CourseDetail/<int:pk>', views.CourseDetail, name='CourseDetail'),
    path('HOD/course/Edit/<str:id>',HOD_Views.EDIT_COURSE,name='edit_course'),
    path('HOD/course/Update/',HOD_Views.UPDATE_COURSE,name='update_course'),
    path('HOD/course/Delete/<str:id>',HOD_Views.DELETE_COURSE,name='delete_course'),
  
   #END CRUD COURSE
    path('HOD/all_courses', HOD_Views.all_courses,name='all_courses'),
    path('p<int:url>', HOD_Views.get_url,name='get_url'),

    path('HOD/course_category', HOD_Views.course_category,name='course_category'),
    path('HOD/course_detail', HOD_Views.course_detail,name='course_detail'),
   #COURSE


    # path('HOD/admin_instructor_list', HOD_Views.admin_instructor_list,name='admin_instructor_list'),
    #CRUD INSTRUCTOR
    path('HOD/instructors', HOD_Views.VIEW_INSTRUCTOR,name='instructors'),
    path('HOD/add_instructor', HOD_Views.add_instructor,name='add_instructor'),
    path('HOD/instructor/Update/', HOD_Views.UPDATE_INSTRUCTOR,name="UPDATE_INSTRUCTOR"),
    path('HOD/Instructor/Edit/<str:id>', HOD_Views.EDIT_INSTRUCTOR,name="edit_instructor"),
    path('HOD/instructor/DELETE/<str:admin>', HOD_Views.DELETE_INSTRUCTOR,name="delete_instructor"),
    #END CRUD INSTRUCTOR
   
    #INSTRUCTOR
    path('HOD/Instructor/Update/', HOD_Views.UPDATE_INSTRUCTOR,name="update_instructor"),
    path('HOD/instructors_detail', HOD_Views.instructors_detail,name='instructors_detail'),
    path('HOD/instructors_requests', HOD_Views.instructors_requests,name='instructors_requests'),
    path('HOD/admin_reviews', HOD_Views.admin_reviews,name='admin_reviews'),
    path('HOD/admin_earnings', HOD_Views.admin_earnings,name='admin_earnings'),
    path('HOD/admin_settings', HOD_Views.admin_settings,name='admin_settings'),
    # path('HOD/sign_up', HOD_Views.sign_up,name='sign_up'),
    #INSTRUCTOR


    # This is Students Url Panel
    #CRUD STUDENT

    #END CRUD STUDENT

    
    # path('Student/home', Student_Views.home,name='student_home'),
    path('Student_edit', Student_Views.Student_UPDATE,name='edit_student'),

    path('Student/Student_dashboard', Student_Views.Student_dashboard,name='Student_dashboard'),
    path('Student/Student_my_subscriptions', Student_Views.Student_my_subscriptions,name='Student_my_subscriptions'),
    path('Student/Student_my_course', Student_Views.Student_my_course,name='Student_my_course'),
    path('Student/Student_payment_info', Student_Views.Student_payment_info,name='Student_payment_info'),
    path('Student/Student_wishlist', Student_Views.Student_wishlist,name='Student_wishlist'),
    path('Student/Student_Edit_Profile', Student_Views.Student_Edit_Profile,name='Student_Edit_Profile'),
    path('Student/Student_settings', Student_Views.Student_settings,name='Student_settings'),
    path('Student/Student_Delete_Profile', Student_Views.Student_Delete_Profile,name='Student_Delete_Profile'),
    path('Student/Student_Sign_Out', Student_Views.Student_Sign_Out,name='Student_Sign_Out'),
    
    #This is Instructor Url Panel
    #CRUD STAFF
    
    #END CRUD STAFF

    path('Staff/Instructor_Dashboard', Staff_Views.Instructor_Dashboard,name='Instructor_Dashboard'),
    path('Staff/Create_course', Staff_Views.Create_course,name="Create_course"),
    path('Staff/Instructor_My_course', Staff_Views.Instructor_My_course,name='Instructor_My_course'),
    path('Staff/Instructor_Earning', Staff_Views.Instructor_Earning,name='Instructor_Earning'),
    path('Staff/Instructor_Student', Staff_Views.Instructor_Student,name='Instructor_Student'),
    path('Staff/Instructor_Orders', Staff_Views.Instructor_Orders,name='Instructor_Orders'),
    path('Staff/Instructor_Reviews', Staff_Views.Instructor_Reviews,name='Instructor_Reviews'),
    path('Staff/Instructor_Edit_Profile', Staff_Views.Instructor_Edit_Profile,name='Instructor_Edit_Profile'),
    path('Staff/Instructor_Payout', Staff_Views.Instructor_Payout,name='Instructor_Payout'),
    path('Staff/Instructor_Settings', Staff_Views.Instructor_Settings,name='Instructor_Settings'),
    path('Staff/Instructor_Delete_Profile', Staff_Views.Instructor_Delete_Profile,name='Instructor_Delete_Profile'),
    path('Staff/Instructor_Sign_Out', Staff_Views.Instructor_Sign_Out,name='Instructor_Sign_Out'),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [

#         path('__debug__/', include('debug_toolbar.urls')),

    # ]+urlpatterns

urlpatterns += staticfiles_urlpatterns()
    
