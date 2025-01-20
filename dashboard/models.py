from django.db import models


# Create your models here.

def generate_staff_id():
    """
    Generates a unique staff ID in the format 'SI001', 'SI002', etc.
    """
    last_staff = Staff.objects.order_by('-staffID').first()
    if last_staff:
        last_id = last_staff.staffID 
        last_number = int(last_id[2:])  # Extract the number part
        new_number = last_number + 1
        new_id = f"SI{new_number:03d}"  # Format with leading zeros
    else:
        new_id = "SI001"  # Initial ID for the first staff member
    return new_id

class Staff(models.Model):
    staffID = models.CharField(max_length=10, primary_key=True, default=generate_staff_id)  # Generate unique staffID
    staffName = models.CharField(max_length=255)
    address= models.CharField(max_length=255) 
    telephone = models.CharField(max_length=15)   # Phone number of the shop
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=150, unique=True)  # Unique username
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.staffName

def generate_shop_id():
    """
    Generates a unique shop ID in the format 'SH001', 'SH002', etc.
    """
    last_shop = Shop.objects.order_by('-shopID').first()
    if last_shop:
        last_id = last_shop.shopID 
        last_number = int(last_id[2:])  # Extract the number part
        new_number = last_number + 1
        new_id = f"SH{new_number:03d}"  # Format with leading zeros
    else:
        new_id = "SH001"  # Initial ID for the first shop
    return new_id
      

class Shop(models.Model):
    shopID = models.CharField(max_length=10, primary_key=True, default=generate_shop_id)  # Generate unique shopID
    shopName = models.CharField(max_length=255)  # Name of the shop
    location = models.CharField(max_length=255)   # Location of the shop
    telephone = models.CharField(max_length=15)   # Phone number of the shop
    staffAssigned = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.shopName
    

    
class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=255)
    unit = models.CharField(max_length=50) # Unit of measurement

    def __str__(self):
        return self.itemName
    
def generate_sales_id():
    """
    Generates a unique sales ID in the format 'RXT000001', 'RXT000002', etc.
    """
    last_sale = Sales.objects.order_by('-salesID').first()
    if last_sale:
        last_id = last_sale.salesID 
        last_number = int(last_id[3:])  # Extract the number part
        new_number = last_number + 1
        new_id = f"RXT{new_number:06d}"  # Format with leading zeros
    else:
        new_id = "RXT000001"  # Initial ID for the first sale
    return new_id
    
class Sales(models.Model):
    salesID = models.CharField(max_length=10, primary_key=True, default=generate_sales_id)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Assuming item belongs to a specific shop
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)  # Assuming shop belongs to a specific staff member
    saleType = models.CharField(max_length=20, choices=[('stock_supplied', 'Stock Supplied'), ('stock_balance', 'Stock Balance')])
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)# Assuming staff member is the one making the sale

    def __str__(self):
        return self.salesID