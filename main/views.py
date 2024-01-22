from django.shortcuts import render, redirect



# Create your views here.
def index(request):
    return render(request, 'index.html')
def adminhome(request):
    return render(request, 'adminhome.html')
def adminviewschedule(request):
    return render(request, 'adminviewschedule.html')
def adminnavbar(request):
    return render(request, 'adminnavbar.html')
def adminmanageschedule(request):
    return render(request, 'adminmanageschedule.html')
def admincurriculumview(request):
    return render(request, 'admincurriculumview.html')
def adminfacultyloading(request):
    return render(request, 'adminfacultyloading.html')
def adminfacultyinformation(request):
    return render(request, 'adminfacultyinformation.html')
def adminsystemconfig(request):
    return render(request, 'adminsystemconfig.html')
def adminaddcurriculum(request):
    return render(request, 'adminaddcurriculum.html')
def adminviewclass(request):
    return render(request, 'adminviewclass.html')
def forgot_password(request):
    return render(request, 'forgot_password.html')
def adduser(request):
    return render(request, 'adduser.html')
def navbar(request):
    return render(request, 'navbar.html')
def staffnavbar(request):
    return render(request, 'staffnavbar.html')
def staffhome(request):
    return render(request, 'staffhome.html')
def staffaddcurriculum(request):
    return render(request, 'staffaddcurriculum.html')
def staffcurriculumview(request):
    return render(request, 'staffcurriculumview.html')
def staffviewclass(request):
    return render(request, 'staffviewclass.html')
def staffviewschedule(request):
    return render(request, 'staffviewschedule.html')
def faculty_loading(request):
    return render(request, 'faculty_loading.html')
def curriculum_view(request):
    return render(request, 'curriculum_view.html')
def manage_curriculumyear(request):
    return render(request, 'manage_curriculumyear.html')
def home(request):
    return render(request, 'home.html', {'current_page': 'home'})
def view_schedule(request):
    return render(request, 'view_schedule.html', {'current_page': 'view_schedule'})
def manage_schedule(request):
    return render(request, 'manage_schedule.html', {'current_page': 'manage_schedule'})
def curriculum_addcurriculum(request):
    return render(request, 'curriculum_addcurriculum.html', {'current_page': 'curriculum_program'})
def system_configuration(request):
    return render(request, 'system_configuration.html', {'current_page': 'system_configuration'})
def faculty_information(request):
    return render(request, 'faculty_information.html', {'current_page': 'faculty_information'})
def view_class(request):
    return render(request, 'view_class.html', {'current_page': 'view_schedule'})
def view_faculty(request):
    return render(request, 'view_faculty.html', {'current_page': 'view_schedule'})
def view_room(request):
    return render(request, 'view_room.html', {'current_page': 'view_schedule'})
def manage_academicyear(request):
    return render(request, 'manage_academicyear.html', {'current_page': 'system_configuration'})
def manage_semester(request):
    return render(request, 'manage_semester.html', {'current_page': 'system_configuration'})
def manage_course(request):
    return render(request, 'manage_course.html', {'current_page': 'system_configuration'})
def manage_yearlevel(request):
    return render(request, 'manage_yearlevel.html', {'current_page': 'system_configuration'})
def manage_section(request):
    return render(request, 'manage_section.html', {'current_page': 'system_configuration'})
def manage_class(request):
    return render(request, 'manage_class.html', {'current_page': 'system_configuration'})
def manage_facultyloading(request):
    return render(request, 'manage_facultyloading.html', {'current_page': 'system_configuration'})
def manage_facility(request):
    return render(request, 'manage_facility.html', {'current_page': 'manage_facility'})
def curriculum_program(request):
    return render(request, 'curriculum_program.html', {'current_page': 'curriculum_program'})

