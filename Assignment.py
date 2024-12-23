
#1.Ans:
def numberCheck():
try:
user_input = input("Enter a number: ")
number = int(user_input)

if number % 2 == 0:
print(f"{number} is an even number.")
else:
print(f"{number} is an odd number.")

except ValueError:
print("Invalid input! Please enter a number.")

else:
numberCheck()

#2. Ans:
#student table
class Student(models.Model):
name = models.CharField(max_length=100)
student_id = models.IntegerField(max_length=20, unique=True)
def __str__(self):
return self.name

#form
class StudentForm(forms.ModelForm):
class Meta:
model = Student
fields = ['name', 'student_id']

#views
def student_list(request):
students = Student.objects.all()
return render(request, 'student_list.html', {'students': students})

def add_student(request):
if request.method == 'POST':
form = StudentForm(request.POST)
if form.is_valid():
form.save()
return redirect('student_list')
else:
form = StudentForm()

return render(request, 'add_student.html', {'form': form})