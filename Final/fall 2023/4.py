# a 

#3 Define both the models in models.py
#Here is the code for the Person and Address models in Django:

from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='addresses')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.country}"



#b. Define the AddressForm in forms.py
#The form excludes the person field since it will be set programmatically. Here’s the implementation:

from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = __all__


#c
#c. Write the create_address function
#This function takes the request as input and creates an Address object, associating it with the currently logged-in user.

from django.shortcuts import redirect
from .forms import AddressForm
from .models import Address, Person

def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address_success')
    return render(request, 'address_form.html', {'form': form})
