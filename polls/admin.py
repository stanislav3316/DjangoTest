from django.contrib import admin

# Register your models here.


from .models import Question, Student, Course

admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Course)
