from django.db import models

# Create your models here.

from django.db import models
from student_class.models import Student_Class
from teacher.models import Teacher
# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    syllabus = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    prerequisites = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trimester = models.PositiveSmallIntegerField()
    course_head = models.CharField(max_length=100)
    enrollment_limit = models.IntegerField()
    classes = models.ManyToManyField(Student_Class, related_name='courses')
    def __str__(self):
        return self.name
[11:14 AM] Agnes Auma Kamondi
from django.db import models
from student_class.models import Student_Class
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    id = models.AutoField(primary_key=True)
    code = models.PositiveSmallIntegerField(unique=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField()
    guardian_phone_number = models.CharField(max_length=15)
    guardian_name = models.CharField(max_length=100)
    class_enrolled = models.ForeignKey(Student_Class, on_delete=models.SET_NULL, null=True, related_name='students')
    picture = models.ImageField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
[11:14 AM] Agnes Auma Kamondi
from django.db import models
from teacher.models import Teacher
# Create your models here.
class Student_Class(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    school_year = models.IntegerField()
    capacity = models.IntegerField()
    room_number = models.IntegerField()
    specialty = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
[11:14 AM] Agnes Auma Kamondi
from django.db import models
# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    education_level = models.CharField(max_length=100)
    subject_specialization = models.CharField(max_length=100)
    bank_account_number = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField()
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
[11:15 AM] Agnes Auma Kamondi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
    
