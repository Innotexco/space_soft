from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('potfolio/', views.potfolio, name='potfolio'),
    path('software_dev/', views.software_dev, name='software_dev'),
    path('career_dev/', views.career_dev, name='career_dev'),

    path('solar_panel/', views.solar_p, name='solar_p'),
    #--------------------------------------------------------------
    path('solar_panel/300w/', views.panel1, name='300w'),
    path('solar_panel/450w/', views.panel2, name='450w'),
    path('solar_panel/550w/', views.panel3, name='550w'),
    path('solar_panel/650w/', views.panel4, name='650w'),
    #--------------------------------------------------------------

    path('battery/', views.battery, name='battery'),
    #--------------------------------------------------------------
    path('battery/200ah/', views.battery1, name='200ah'),
    path('battery/300ah/', views.battery2, name='300ah'),
    path('battery/336ah/', views.battery3, name='336ah'),
    path('battery/600ah/', views.battery4, name='600ah'),
    #--------------------------------------------------------------

    path('inverter/', views.inverter, name='inverter'),
    #--------------------------------------------------------------
    path('inverter/6_2kva/', views.inverter1, name='6_2kva'),
    path('inverter/2kva/', views.inverter2, name='2kva'),
    path('inverter/10_2kva/', views.inverter3, name='10_2kva'),
    path('inverter/3_2kva/', views.inverter4, name='3_2kva'),
    #--------------------------------------------------------------


    path('potfolio/', views.potfolio, name='potfolio'),
    path('about/', views.about, name='about'), 

    path('contact/', views.contact, name='contact'),
    path('enroll-course/', views.course, name='course'),
    path('enroll/', views.student_enrollment_view, name='student_enroll'),
    path('enroll/success/', views.enroll_success, name='enroll_success'),
    
]
