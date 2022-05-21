from django.shortcuts import render
from django.views import View
from .models import Student

def main(request):
    return render(request, 'main_window.html')

class StudentsView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "students/student_list.html", {"student_list.html": students})
