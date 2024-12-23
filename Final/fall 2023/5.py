a. Process of creating and connecting "products app" to the main app
1.Create the "products" app:
Run the following command in the terminal:

python manage.py startapp products
This creates a new folder products inside the project directory.

2.Register the app in settings.py:
Open dJcrudview/settings.py and add 'products' to the INSTALLED_APPS list:

INSTALLED_APPS = [
    ...
    'products',
]
3.Define URLs for the "products" app:

Inside the products app, create a file named urls.py if it doesn’t already exist.
Add routes for the app in products/urls.py:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products-index'),  # Example view
]


4. Create a View:

Define a simple view in products/views.py:
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Products App!")
5.Connect "products" app to the main app's URLs:

Open the main app's urls.py file (dJcrudview/urls.py) and include the products app’s URLs:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),  # Include products app
]




# b

b. Process of uploading media in a model and configuring Django admin
1. Set up media configuration:

In the main app’s settings.py, add the following configuration for media files:
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
2. Update main urls.py to serve media:

Add the following code to dJcrudview/urls.py:
from django.conf import settings
from django.conf.urls.static import static


3.Create the Product Model:

In products/models.py, define a model with a media field:
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/images/')
    description = models.TextField()

    def __str__(self):
        return self.name
4.Make and apply migrations:
Run the following commands in the terminal:

python manage.py makemigrations
python manage.py migrate

5.Register the model in Django Admin:

Open products/admin.py and register the Product model:
from django.contrib import admin
from .models import Product

admin.site.register(Product)

6.Upload media through the Django admin:

Start the server using:
python manage.py runserver