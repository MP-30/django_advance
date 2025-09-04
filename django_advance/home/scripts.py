class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default='IN')
    def __str__(self):
        return self.brand_name
    
class Products(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    
    
brand = Brand.objects.get(id='3')

Products(product_name="Macbook", brand= Brand.objects.get(id='4'))
# or
Products.objects.create(product_name="Soap", brand = brand)