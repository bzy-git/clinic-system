from django.db import models
from django.contrib.auth.models import User


departments=[('Cardiologist','Cardiologist'),
('Outpatient Department', 'Outpatient Department'),
('Radiology Department', 'Radiology Department'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

#Doctor's Details 
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) # One-to-one relationship field with User model, representing the associated user for the doctor
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)  # Image field for storing doctor's profile picture
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50, choices=departments, default='Cardiologist')
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name # Property method to get the full name of the associated user
    
    @property
    def get_id(self):
        return self.user.id  # Property method to get the ID of the associated user
    
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)  # String representation of the doctor, showing first name and department


#Patient's Details 
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)   # One-to-one relationship field with User model, representing the associated user for the patient
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True) # Image field for storing patient's profile picture
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):       
        return self.user.first_name+" "+self.user.last_name # Property method to get the full name of the associated user
    

    @property
    def get_id(self):
        return self.user.id   # Property method to get the ID of the associated user


    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")" # String representation of the patient, showing first name and symptoms. 
    

#Appoinment Details
class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)  # Field to store the patient ID as a positive integer.
    doctorId=models.PositiveIntegerField(null=True) # Field to store the doctor ID as a positive integer.
    patientName=models.CharField(max_length=40,null=True)  # Field to store the patient name as a character field with a maximum length of 40 characters.
    doctorName=models.CharField(max_length=40,null=True)  # Field to store the doctor name as a character field with a maximum length of 40 characters
    appointmentDate=models.DateField(auto_now=True)  # Field to store the appointment date as a date field, automatically set to the current date and time.
    description=models.TextField(max_length=500)  # Field to store the description of the appointment as a text field with a maximum length of 500 characters
    status=models.BooleanField(default=False) # Field to store the status of the appointment as a boolean field.



#Patient Discharge  Details 
class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)   # Field to store the patient ID as a positive integer, allows null values
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True) # Field to store the symptoms reported by the patient as a character field with a maximum length of 100 characters, allows null values

    admitDate=models.DateField(null=False) # Field to store the admission date of the patient as a date field.
    releaseDate=models.DateField(null=False) # Field to store the discharge date of the patient as a date field.
    daySpent=models.PositiveIntegerField(null=False) # Field to store the number of days spent by the patient in the hospital. 

    roomCharge=models.PositiveIntegerField(null=False)   #Field to store the room charges for the patient as a positive integer field
    medicineCost=models.PositiveIntegerField(null=False) #Field to store the medicine costs for the patient as a positive integer field
    doctorFee=models.PositiveIntegerField(null=False) #Field to store the doctor's fee for the patient as a positive integer field.
    OtherCharge=models.PositiveIntegerField(null=False)  #Field to store other charges for the patient as a positive integer field.
    total=models.PositiveIntegerField(null=False, default=0)  #Field to store the total charges for the patient as a positive integer field.

    def save(self, *args, **kwargs):
        # Calculate total charges
        self.total = self.roomCharge * self.daySpent + self.medicineCost + self.doctorFee + self.OtherCharge
        super(PatientDischargeDetails, self).save(*args, **kwargs)


