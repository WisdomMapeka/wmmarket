from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your models here.
class Icons(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True, unique=True)
    picture = models.ImageField(upload_to='icons', blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'icons'

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank = True, null = True, unique=True)
    discription = models.TextField(blank = True, null = True)
    picture = models.ImageField(upload_to='uploads/categories', blank = True, null = True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True,
        help_text='Unique value for product page URL, created from name.')
    is_active = models.BooleanField(default=True, blank = True, null = True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,  
        help_text='Comma-delimited set of SEO keywords for meta tag', blank = True, null = True)
    meta_description = models.CharField("Meta Description", max_length=255,
        help_text='Content for description meta tag', blank = True, null = True)    
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)      
    updated_at = models.DateTimeField(auto_now=True, blank = True, null = True) 

    class Meta:           
        db_table = 'categories'           
        ordering = ['-created_at']          
        verbose_name_plural = 'Categories'                  

   
    def get_absolute_url(self):
        return 'category_list/%s/' % self.slug         

    def __str__(self):
        return self.category_name


class Product(models.Model):
    productName = models.CharField(max_length = 200, blank = True, null = True)
    productShortDescription = models.CharField(max_length = 300, blank = True, null = True)
    productFullDescription = models.TextField(blank = True, null = True)
    category = models.ForeignKey(Category, blank = True, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9,decimal_places=2, blank = True, null = True)       
    old_price = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True,default=0.00) 
    discount = models.CharField(max_length=20, default=0)
    weight = models.CharField(max_length=20, default=0)
    instock = models.IntegerField( default=0)
    slug = models.SlugField(max_length=255, unique=True, 
        help_text='Unique value for product page URL, created from name.', blank = True, null = True)      
    brand = models.CharField(max_length=50, blank = True, null = True)       
    sku = models.CharField(max_length=50, blank = True, null = True) 
    is_active = models.BooleanField(default=True)      
    is_bestseller = models.BooleanField(default=False)      
    is_featured = models.BooleanField(default=False)      
    meta_keywords = models.CharField(max_length=255, 
        help_text='Comma-delimited set of SEO keywords for meta tag', blank = True, null = True)      
    meta_description = models.CharField(max_length=255,   
        help_text='Content for description meta tag', blank = True, null = True)     
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)     
    picture = models.ImageField(upload_to = 'uploads/products', blank = True, null = True)
    rates = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
        )
    ratings = models.CharField(max_length = 1, choices = rates, blank = True, null = True)

     
                   
       

    class Meta:           
        db_table = 'products'           
        ordering = ['-created_at']      
 
  
    def __str__(self, no_name="No Name"):
        self.no_name = no_name
        if not self.productName:
            return no_name 
        else:
            return self.productName           

      
    def get_absolute_url(self):          
         return ('products', (), { 'product_slug': self.slug }) 


    def sale_price(self):
        if self.old_price > self.price:
            return self.price          
        else:                
            return None

    def delete(self):
        self.picture.url.delete()
        return None


class UserProfile(models.Model):
    firstName = models.CharField(max_length=200, blank = True, null = True)
    lastName = models.CharField(max_length=200, blank = True, null = True)
    city = models.CharField(max_length=100, blank = True, null = True)
    state = models.CharField(max_length=100, blank = True, null = True)
    phoneCalls = models.CharField(max_length=30, blank = True, null = True)
    phoneWhatsapp = models.CharField(max_length=30, blank = True, null = True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    repeat_password = models.CharField(max_length=200)
    email_verified = models.IntegerField(1, blank = True, null = True)
    registrationDate = models.DateTimeField(auto_now_add = True)
    verification_code = models.CharField(max_length=100, blank = True, null = True)
    ip = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return self.firstName

    class Meta:
        db_table = 'userprofile'




class Comments(models.Model):
    comment_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank = True, null = True)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comments'


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    numItems = models.IntegerField(default=0, blank = True, null = True)
    total  = models.IntegerField(default=0, blank = True, null = True)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.cartID

    class Meta:
        db_table='cart'


class Payments(models.Model):
    paymentID = models.IntegerField(unique=True)
    pay_options = (
        ('VISA','VISA'),
        ('Ecocash','Ecocash'),
        ('One Money','One Money'),
        ('TeleCash','TeleCash')
        )
    payment_methods = models.CharField(max_length=30 ,choices=pay_options)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.paymentID

    class Meta:
        db_table = 'payments'


class Transaction(models.Model):
    transctionID = models.IntegerField(unique=True)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    TransctionDate = models.DateTimeField(auto_now_add=True)
    Fullfiled = models.IntegerField()
    discount = models.CharField(max_length=100, blank = True, null = True)
    payment_details = models.ForeignKey(Payments, on_delete=models.CASCADE)
    sell_details = models.ForeignKey(Cart, on_delete=models.CASCADE)


    def __str__(self):
        return self.transctionID

    class Meta:
        db_table='transaction'
