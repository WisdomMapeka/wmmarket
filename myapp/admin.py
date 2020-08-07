from django.contrib import admin
from .models import Category, Product, UserProfile, Comments, Cart, Payments, Icons

# Register your models here.

admin.site.register(Payments)
admin.site.register(Icons)


class ProductAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products       
    list_display = ('productName', 'price', 'old_price','created_at', 'updated_at', 'instock')      
    list_display_links = ('productName', 'price')      
    list_per_page = 50      
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']     
    exclude = ('created_at', 'updated_at',)  
    #  # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('productName',)}  
    # # registers your product model with the admin site 
admin.site.register(Product, ProductAdmin)  

class CategoryAdmin(admin.ModelAdmin):    
    list_display = ('category_name', 'created_at', 'updated_at',)      
    list_display_links = ('category_name',)      
    list_per_page = 20      
    ordering = ['created_at']      
    search_fields = ['category_name', 'description', 'meta_keywords', 'meta_description']      
    exclude = ('created_at', 'updated_at',)           
    prepopulated_fields = {'slug' : ('category_name',)}      
admin.site.register(Category, CategoryAdmin)

class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ('firstName', 'lastName')      
    list_display_links = ('firstName', 'lastName')      
    list_per_page = 50      
    search_fields = ['firstName', 'lastName']        
admin.site.register(UserProfile, UserProfileAdmin)  


class CommentsAdmin(admin.ModelAdmin):       
    list_display = ('comment_owner', 'comment')      
    list_display_links = ('comment_owner', 'comment')      
    list_per_page = 50      
    search_fields = ['comment_owner', 'comment']     
admin.site.register(Comments, CommentsAdmin) 


class CartAdmin(admin.ModelAdmin):      
    list_display = ('product', 'numItems', 'customer')      
    list_display_links = ('product', 'customer')      
    list_per_page = 50      
    search_fields = ['product', 'customer']     
admin.site.register(Cart, CartAdmin)   








