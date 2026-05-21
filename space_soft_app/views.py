from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail, BadHeaderError, EmailMessage, get_connection
from django.contrib import messages
from .models import *
from .forms import *
from django.templatetags.static import static


# email functions
def send_with_diffrent_smtp(subject, body, user, password, to):
    connection = get_connection(
        host='server355.web-hosting.com',
        port=587,
        username=user,  # ✅ Fixed
        password=password,
        use_tls=True
    )

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email= user,
        to=to,
        connection=connection
    )

    email.send()



# Create your views here.

def home(request):
    gallery_a = [
        {'url': static('img/sol.jpg')},
        {'url': static('img/we.png')},
        {'url': static('img/electronic.jpg')},
    ]
    return render(request, 'space_soft/home.html', dict(gallery_a=gallery_a))

def software_dev(request):
    return render(request, 'space_soft/software_dev.html')

def career_dev(request):
    return render(request, 'space_soft/career_dev.html')

def solar_p(request):
    return render(request, 'space_soft/solar_panel.html')

# -------------------------------------------------------
def panel1(request):
    return render(request, 'space_soft/300w.html')

def panel2(request):
    return render(request, 'space_soft/450w.html')

def panel3(request):
    return render(request, 'space_soft/550w.html')

def panel4(request):
    return render(request, 'space_soft/650w.html')
# -------------------------------------------------------

def battery(request):
    return render(request, 'space_soft/ESS.html')
# -------------------------------------------------------
def battery1(request):
    return render(request, 'space_soft/200ah.html')

def battery2(request):
    return render(request, 'space_soft/300ah.html')

def battery3(request):
    return render(request, 'space_soft/336ah.html')

def battery4(request):
    return render(request, 'space_soft/600ah.html')
#-----------------------------------------------------


def inverter(request):
    return render(request, 'space_soft/inverter.html')
# -------------------------------------------------------
def inverter1(request):
    return render(request, 'space_soft/6.2kva.html')
def inverter2(request):
    return render(request, 'space_soft/2kva.html')
def inverter3(request):
    return render(request, 'space_soft/10kva.html')
def inverter4(request):
    return render(request, 'space_soft/3kva.html')
#-----------------------------------------------------


def potfolio(request):
    return render(request, 'space_soft/portfolio.html')

def about(request):
    return render(request, 'space_soft/about.html')


#--------------------------------------------------------------------------------------

def course(request):
    initial_data = {}
    selected_course = request.GET.get('course')
    if selected_course:
        initial_data['course'] = selected_course


    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            email = cd['email']
            contact = cd['contact']
            address = cd['address']
            course = cd['course']
            msg = cd['message']

            message = f"""
            \nFrom: {name} 
            \nEmail: {email}
            \nContact: {contact}
            \nAddress: {address}
            \nCourse: {course}
            \nMessage: \n\n{msg}
            """
            try:
                send_with_diffrent_smtp(
                    subject = f"Course Intrest: {name} for {course}",
                    body=message,
                    to=["career@spacesoftintegrals.com"],
                    user="career@spacesoftintegrals.com",
                    password= "001_career",
                )

                course_db = Course_Intrest(
                    name = name,
                    course = course,
                    email = email,
                    contact = contact,
                    address = address,
                    message = msg
                )
                course_db.save()


                messages.success(request, "Sent Successfully")
                return redirect('career_dev')
                # return HttpRequest(message)
            except BadHeaderError:
                messages.error(request, "Invalid header found.")
            except Exception as e:
                messages.error(request, f"An error occured: {e}")
    else:
        form = CourseForm()
    return render(request, 'space_soft/contact.html', dict(form=form, selected_form = "course", course = selected_course))


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            email = cd['email']
            contact = cd['contact']
            address = cd['address']
            msg = cd['message']

            message = f"""
            \nFrom: {name} 
            \nEmail: {email}
            \nContact: {contact}
            \nAddress: {address}
            \nMessage: \n\n{msg}
            """


            try:
                send_mail(
                    subject = f"Contacted by {name}",
                    message=message, 
                    from_email="info@spacesoftintegrals.com", 
                    recipient_list=["info@spacesoftintegrals.com "],
                    fail_silently= False
                )

                contact_db = Contact(
                    name = name,
                    email = email,
                    contact = contact,
                    address = address,
                    message = msg
                )
                contact_db.save()

                messages.success(request, "Sent Successfully")
                return redirect('home')
            except BadHeaderError:
                messages.error(request, "Invalid header found.")
            except Exception as e:
                messages.error(request, f"An error occured: {e}")
    else:
        form = ContactForm()
    
    return render(request, 'space_soft/contact.html', dict(form=form, selected_form = "contact"))


# @never_cache
def student_enrollment_view(request):
    if request.method == "POST":

        # Check required fields
        required_fields = ['full_name', 'gender', 'dob', 'email']
        for field in required_fields:
            if not request.POST.get(field):
                raise ValueError(f"{field.replace('_', ' ').title()} is required.")
        get = request.POST.get

        full_name= get('full_name')
        gender= get('gender')
        date_of_birth= get('dob')
        nationality= get('nationality')
        marital_status=get('marital_status')
        state_of_origin= get('state')
        lga= get('lga')
        religion= get('religion')

        phone_number=get('phone')
        email=get('email')
        residential_address=get('address')
        emergency_name=get('emergency_name')
        emergency_relationship= get('emergency_relationship')
        emergency_phone=get('emergency_phone')

        highest_qualification=get('qualification')
        institution=get('institution')
        graduation_year=get('graduation_year')
        field_of_study=get('field')
        relevant_skills=get('skills')

        course=get('course')
        classMode=get('class_mode', "Onsite")
        reason=get('reason')


        message = f"""
        \nHello Team,

        \nA new student has successfully registered for a course. Below are the details:
        \n* Full Name: {full_name} 
        \n* Course: {course} 
        \n* Class Mode: {classMode} 
        \n* Email: {email}
        \n* Phone: {phone_number}
        \n* Address: {residential_address}
        \n* Emergency Contact: {emergency_name}, {emergency_relationship}, {emergency_phone}
        \n* Country: {nationality}\n
        \n* Academic Qualifications: {highest_qualification}
        \n* Field of Study: {field_of_study}

        \nPlease review and follow up as necessary

        """

        msg = f"""
        \nDear {full_name},

        \nThank you for registering for our Career Development Program at SpaceSoft!

        \nHere’s a summary of your enrollment:
        \n- Course: {course}
        \n- Class Mode: {classMode}
        \n- field of study: {field_of_study}

        \nOur team will reach out to you shortly with further details about your next steps.

        \nYou can reach us:
        \n- WhatsApp: https://wa.me/2349024433383
        \n- Facebook: https://www.facebook.com/Spacesoft2017

        \nWelcome to a journey of growth and innovation!

        \nBest regards,
        \nSpaceSoft Training Team
        """


        try:

            send_with_diffrent_smtp(
                subject = f"New Resgistration: {full_name} for {course}",
                body=message,
                to=["trainee@spacesoftintegrals.com"],
                user="trainee@spacesoftintegrals.com",
                password= "001_trainee"
            )

            send_with_diffrent_smtp(
                subject = f"Registration Successful — Welcome to SpaceSoft Career Development Program!",
                body=msg,
                to=[email],
                user="trainee@spacesoftintegrals.com",
                password= "001_trainee"
            )

            # student = Student.objects.create(
            #     full_name= full_name,
            #     gender= gender,
            #     date_of_birth= date_of_birth,
            #     nationality= nationality,
            #     marital_status=marital_status,
            #     state_of_origin= state_of_origin,
            #     lga= lga,
            #     religion= religion,

            #     phone_number=phone_number,
            #     email= email,
            #     residential_address= residential_address,
            #     emergency_name= emergency_name,
            #     emergency_relationship= emergency_relationship,
            #     emergency_phone= emergency_phone,

            #     highest_qualification= highest_qualification,
            #     institution= institution,
            #     graduation_year= graduation_year,
            #     field_of_study= field_of_study,
            #     relevant_skills= relevant_skills,

            #     course = course,
            #     class_mode = classMode,
            #     reason = reason,
            # )
            # # student.save()
            messages.success(request, f"Sent Successfully")


            response = redirect('enroll_success')
            return response
        except BadHeaderError:
                messages.error(request, "Invalid header found.")
        except Exception as e:
            messages.error(request, f"An error occured: {e}")
            return render(request, 'space_soft/enrollment/enroll_form.html')

    return render(request, 'space_soft/enrollment/enroll_form.html')

def enroll_success(request):
    return render(request, 'space_soft/enrollment/enroll_success.html')
    

#------------------------------------------------------------------------------------

def bms(request):
    return render(request, 'space_soft/BMS.html')


