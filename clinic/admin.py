from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails



# Django Admin Configurations for Doctor Model
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

# Django Admin Configurations for Patient Model
class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

# Django Admin Configurations for Appointment Model
class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)


# Django Admin Configurations for PatientDischargeDetails Model
class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
