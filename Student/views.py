from distutils.command.build_scripts import first_line_re
from tkinter import FIRST
from django.shortcuts import redirect, render ,HttpResponse
from Student.models import Nrs ,Lkg, Ukg, First , Second ,Third ,Fourth , Fifth , Sixth , Seventh ,Eight ,Nineth ,Tenth , Eleventh ,Twelth
# Create your views here.

# for main page index
def index(request) :

    context={
        'iterator' : range(-2,13) 
    }
    return render(request , "index.html" ,context)

# for class_view
def class_view(request,standard) :

    # class_data = standard.objects.all()
    if standard == "Nrs" :
        class_data = Nrs.objects.all()
        # searching logic
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Nrs.objects.filter(name__icontains=st_name)
    elif standard == "Ukg" :
        class_data = Ukg.objects.all()
        # searching logic
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Ukg.objects.filter(name__icontains=st_name)
    elif standard == "Lkg" :
        class_data = Lkg.objects.all()
        # searching logic
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Lkg.objects.filter(name__icontains=st_name)    
    elif standard == "1" :
        class_data = First.objects.all()
        # searching logic
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = First.objects.filter(name__icontains=st_name)
    elif standard == "2" :
        class_data = Second.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Second.objects.filter(name__icontains=st_name)
    elif standard == "3" :
        class_data = Third.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Third.objects.filter(name__icontains=st_name)
    elif standard == "4" :
        class_data = Fourth.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Fourth.objects.filter(name__icontains=st_name)
    elif standard == "5" :
        class_data = Fifth.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Fifth.objects.filter(name__icontains=st_name)
    elif standard == "6" :
        class_data = Sixth.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Sixth.objects.filter(name__icontains=st_name)
    elif standard == "7" :
        class_data = Seventh.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Seventh.objects.filter(name__icontains=st_name)
    elif standard == "8" :
        class_data = Eight.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Eight.objects.filter(name__icontains=st_name)
    elif standard == "9" :
        class_data = Nineth.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Nineth.objects.filter(name__icontains=st_name)
    elif standard == "10" :
        class_data = Tenth.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Tenth.objects.filter(name__icontains=st_name)
    elif standard == "11" :
        class_data = Eleventh.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                    class_data = Eleventh.objects.filter(name__icontains=st_name)
    else :
        class_data = Twelth.objects.all()
        if request.method == "POST" :
            st_name =  request.POST.get('stu_name')
            if st_name != None :
                class_data = Twelth.objects.filter(name__icontains=st_name)

    class_data = {
        'class_data' : class_data,
        'std' : standard
    }
    return render(request , "class_view.html",class_data)

# for student_profile
def student_profile(request,standard,rollno) :

    if standard == "Nrs" :
        student_data = Nrs.objects.get(rollno=rollno)
    elif standard == "Ukg" :
        student_data = Ukg.objects.get(rollno=rollno)
    elif standard == "Lkg" :
        student_data = Lkg.objects.get(rollno=rollno)
    elif standard == "1" :
        student_data = First.objects.get(rollno=rollno)
    elif standard == "2" :
        student_data = Second.objects.get(rollno=rollno)
    elif standard == "3" :
        student_data = Third.objects.get(rollno=rollno)
    elif standard == "4" :
        student_data = Fourth.objects.get(rollno=rollno)
    elif standard == "5" :
        student_data = Fifth.objects.get(rollno=rollno)
    elif standard == "6" :
        student_data = Sixth.objects.get(rollno=rollno)
    elif standard == "7" :
        student_data = Seventh.objects.get(rollno=rollno)
    elif standard == "8" :
        student_data = Eight.objects.get(rollno=rollno)
    elif standard == "9" :
        student_data = Nineth.objects.get(rollno=rollno)
    elif standard == "10" :
        student_data = Tenth.objects.get(rollno=rollno)
    elif standard == "11" :
        student_data = Eleventh.objects.get(rollno=rollno)
    else  :
        student_data = Twelth.objects.get(rollno=rollno)
    # dict
    student = {
        'student_data' : student_data 
    }
    return render(request , "student_profile.html",student)

# Admi form
def admi_form(request,standard) : 
    if standard == "Nrs" :
        std = standard
        standard = Nrs
    elif standard == "Ukg" :
        std = standard
        standard = Ukg
    elif standard == "Lkg" :
        std = standard
        standard = Lkg
    elif standard == "1" :
        std = standard
        standard = First
    elif standard == "2" :
        std = standard
        standard = Second
    elif standard == "3" :
        std = standard
        standard = Third
    elif standard == "4" :
        std = standard
        standard = Fourth
    elif standard == "5" :
        std = standard
        standard = Fifth
    elif standard == "6" :
        std = standard
        standard = Sixth
    elif standard == "7" :
        std = standard
        standard = Seventh
    elif standard == "8" :
        std = standard
        standard = Eight
    elif standard == "9" :
        std = standard
        standard = Nineth
    else  :
        std = standard
        standard = Tenth
    if request.method == "POST" :
        # student details
        if request.POST.get('std') == "" or request.POST.get('rollno') == "" or request.POST.get('total_school_fees') == "" or request.POST.get('total_school_fees_paid') == "" or request.POST.get('total_bus_fees') == "" or request.POST.get('total_school_fees_paid') == "":
            return redirect(f"/admi_form/{std}")
        
        name = request.POST.get('name')
        std = request.POST.get('std')
        register_no = request.POST.get('register_no')
        master_no = request.POST.get('master_no')
        rollno = request.POST.get('rollno')
        udise_no = request.POST.get('udise_no')
        aadhar_no = request.POST.get('aadhar_no')
        mobile_no = request.POST.get('mobile_no')
        admission_date = request.POST.get('admission_date')
        # school fees
        total_school_fees = request.POST.get('total_school_fees')
        total_school_fees_paid = request.POST.get('total_school_fees_paid')
        date_of_school_fees_paid = request.POST.get('date_of_school_fees_paid')
        total_school_fees_remain = str(int(total_school_fees)-int(total_school_fees_paid))
        # bus fees
        total_bus_fees = request.POST.get('total_bus_fees')
        total_bus_fees_paid = request.POST.get('total_bus_fees_paid')
        date_of_bus_fees_paid = request.POST.get('date_of_bus_fees_paid')
        total_bus_fees_remain = str(int(total_bus_fees)-int(total_bus_fees_paid))
        # other details
        bonafide_taken = request.POST.get('bonafide_taken')
        note = request.POST.get('note')

        data = standard(name=name,std=std,register_no=register_no,master_no=master_no,rollno=rollno,udise_no=udise_no,aadhar_no=aadhar_no,mobile_no=mobile_no,admission_date=admission_date,total_school_fees=total_school_fees,total_school_fees_paid=total_school_fees_paid,date_of_school_fees_paid=date_of_school_fees_paid,total_school_fees_remain=total_school_fees_remain,total_bus_fees=total_bus_fees,total_bus_fees_paid=total_bus_fees_paid,date_of_bus_fees_paid=date_of_bus_fees_paid,total_bus_fees_remain=total_bus_fees_remain,bonafide_taken=bonafide_taken,note=note)
        data.save()

        # after submiting form redirected to the class view
        return redirect("/")
        
    admi = {
        "std" : std
    } 
    return render(request , "admi_form.html", admi)