from django.db import models


# Create your models here.


class Staff(models.Model):
    staffID = models.AutoField(primary_key=True)
    staffName = models.CharField(max_length=255)
    address= models.CharField(max_length=255) 
    telephone = models.CharField(max_length=15)   # Phone number of the shop
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=150, unique=True)  # Unique username
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.staffName

class Shop(models.Model):
    shopID = models.AutoField(primary_key=True)  # Auto-incrementing ID
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
    
class Sales(models.Model):
    salesID = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Assuming item belongs to a specific shop
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)  # Assuming shop belongs to a specific staff member
    saleType = models.CharField(max_length=20, choices=[('stock_supplied', 'Stock Supplied'), ('stock_balance', 'Stock Balance')])
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)# Assuming staff member is the one making the sale

    def __str__(self):
        return self.salesID