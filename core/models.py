from django.db import models

#feedproduct  model
class FeedProduct(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2)
    minimum_stock = models.PositiveIntegerField()
    def __str__(self):
        return self.product_name

#supplier Model
class Supplier(models.Model):
    supplier_name = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.supplier_name

#Inventory Model
class Inventory(models.Model):
    product = models.OneToOneField(FeedProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    updated_at = models.DateTimeField(auto_now=True)

#purchase model
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete = models.PROTECT)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    purchase_date = models.DateField()

#sales model
class Sale(models.Model):
    product = models.ForeignKey(FeedProduct, on_delete = models.PROTECT)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10,decimal_places=2)
    total_amount = models.DecimalField(max_digits=12,decimal_places=2)
    sale_date = models.DateField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"
    