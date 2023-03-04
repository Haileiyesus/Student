from django import forms 
from django.forms import Form
from student_management_app.models import Courses, SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    first_name = forms.CharField(label="Family First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Family Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    family_adress = forms.CharField(label="Family Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    family_phone_no = forms.CharField(label="Family Phone Number", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    family_city = forms.CharField(label="Family City", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    relation = forms.CharField(label="Relation", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_student_name = forms.CharField(label="Student First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_student_name = forms.CharField(label="Student Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    age = forms.CharField(label="Age", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    course_list = []
    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []
    
    #For Displaying Session Years
    session_year_list = []
    try:
        session_years = SessionYearModel.objects.all()
       
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []
    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    course_id = forms.ChoiceField(label="Grade", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))



class EditStudentForm(forms.Form):
    first_name = forms.CharField(label="Family First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Family Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    family_adress = forms.CharField(label="Family Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    family_phone_no = forms.CharField(label="Family Phone Number", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    family_city = forms.CharField(label="Family City", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    relation = forms.CharField(label="Relation", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_student_name = forms.CharField(label="Student First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_student_name = forms.CharField(label="Student Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    age = forms.CharField(label="Age", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []

    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))


    