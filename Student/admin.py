from django.contrib import admin
from Student.models import Nrs ,Lkg, Ukg, First , Second ,Third ,Fourth , Fifth , Sixth , Seventh ,Eight ,Nineth ,Tenth , Eleventh ,Twelth
# Register your models here.

# Nrs standard
class nrsAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Nrs,nrsAdmin)

# Lkg standard
class lkgAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Lkg,lkgAdmin)

# Ukg standard
class ukgAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Ukg,ukgAdmin)

# 1st standard
class firstAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(First,firstAdmin)

# 2nd standard
class secondAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Second,secondAdmin)

# 3rd standard
class thirdAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Third,thirdAdmin)

# 4th standard
class fourthAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Fourth,fourthAdmin)

# 5th standard
class fifthAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Fifth,fifthAdmin)

# 6th standard
class sixthAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Sixth,sixthAdmin)

# 7th standard
class seventhAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Seventh,seventhAdmin)

# 8th standard
class eightAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Eight,eightAdmin)

# 9st standard
class ninethAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Nineth,ninethAdmin)

# 10st standard
class tenthAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Tenth,tenthAdmin)

# 11th standard
class eleventhAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Eleventh,eleventhAdmin)

# 12th standard
class twelthAdmin(admin.ModelAdmin) :
    list_display = ('name','father_name','mother_name','birth_date','birth_place','std','register_no','master_no','rollno','udise_no','aadhar_no','mobile_no','admission_date', 'total_school_fees','total_school_fees_paid','date_of_school_fees_paid' ,'total_school_fees_remain','total_bus_fees','total_bus_fees_paid','date_of_bus_fees_paid', 'total_bus_fees_remain','bonafide_taken' )
admin.site.register(Twelth,twelthAdmin)

