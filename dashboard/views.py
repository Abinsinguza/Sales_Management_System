from django.shortcuts import render, redirect
from .models import Shop, Staff
from .forms import ShopForm, StaffForm

# Create your views here.
def index(request):
    return render(request, 'dashboard.html')

def forms_page(request):
    return render(request, 'form.html')  # Ensure 'forms.html' is in your templates folder


#Handling the shops 
def shop_page(request):
    if request.method == 'POST':
       form = ShopForm(request.POST)
       if form.is_valid():
          print("Form is valid..saving data...")
          form.save()  # Save shop to the database
          return redirect('shops')  # Redirect to shop list after saving
       else:
          print("Form is not valid...")
               #print(form.errors)
               #return render(request, 'shops.html', {'form': form,})  # Show the form again with errors if invalid
    
    shops = Shop.objects.all()
    # Query all staff members to populate the dropdown
    staff = Staff.objects.all()
   
    return render(request, 'shops.html', {'shops': shops, 'staff': staff })  # Ensure'shop.html' is in your templates folder


def register_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            print("Form is valid..saving data...")
            form.save()  # Save shop to the database
            return redirect('shops')  # Redirect to shop list after saving
        else:
            print("Form is not valid...")
            #print(form.errors)
            #return render(request, 'shops.html', {'form': form,})  # Show the form again with errors if invalid
    else:
        form = ShopForm()
    return render(request, 'shops.html', {'form': form,})

#Handling the staff
def staff_page(request):
    staff = Staff.objects.all()
    return render (request, 'staff.html',{'staff':staff})

def register_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            print("Form is valid..saving data...")
            form.save()  # Save staff to the database
            return redirect('staff')  # Redirect to a staff list page
        else:
            print("Form is not valid...")
            print(form.errors)  # Print validation errors
    else:
        form = StaffForm()
    return render(request, 'staff.html', {'form': form})

def items_page(request):
    return render(request, 'items.html')  # Ensure 'items.html' is in your templates folder

def tables_page(request):
    return render(request, 'tables.html')  # Ensure 'tables.html' is in your templates folder


    

# View to list all shops
def view_shops(request):
    shops = Shop.objects.all()
    return render(request, 'form.html', {'shops': shops})