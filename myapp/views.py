from django.shortcuts import render, get_object_or_404
from . models import Category, Product, UserProfile, Comments, Cart, Payments, Transaction, Icons
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    categories = Category.objects.all()
    shopping_cart = Icons.objects.get(name='shopping-cart')
    arrow_down = Icons.objects.get(name='arrow-down')
    try:
        cat1 = categories[:1].get()
    except Exception as e:
        pass

    try:
        cat2 = categories[1:2].get()
    except Exception as e:
        pass

    try:
        cat3 = categories[2:3].get()
    except Exception as e:
        pass
    
    
    try:
        cat4 = categories[3:4].get()
    except Exception as e:
        pass
    
    try:
        cat5 = categories[4:5].get()
    except Exception as e:
        pass
    
    try:
        cat6 = categories[5:6].get()
    except Exception as e:
        pass
    
    try:
        cat7 = categories[6:7].get()
    except Exception as e:
        pass
    
    try:
        cat8 = categories[7:8].get()
    except Exception as e:
        pass
    
    try:
        cat9 = categories[8:9].get()
    except Exception as e:
        pass
    
    try:
        cat10 = categories[9:10].get()
    except Exception as e:
        pass
    
    
    try:
        cat11 = categories[10:11].get()
    except Exception as e:
        pass

    try:
        cat12 = categories[11:12].get()
    except Exception as e:
        pass
    
    try:
        cat13 = categories[12:13].get()
    except Exception as e:
        pass
    
    try:
        cat14 = categories[13:14].get()
    except Exception as e:
        pass
    
    try:
        cat15 = categories[14:15].get()
    except Exception as e:
        pass
    
    try:
        cat16 = categories[15:16].get()
    except Exception as e:
        pass
    
    try:
        cat17 = categories[16:17].get()
    except Exception as e:
        pass
    
    try:
        cat18 = categories[17:18].get()
    except Exception as e:
        pass
    
    try:
        cat19 = categories[18:19].get()
    except Exception as e:
        pass
    
    try:
        cat20 = categories[19:20].get()
    except Exception as e:
        pass

    try:
        cat21 = categories[20:21].get()
    except Exception as e:
         pass
    

    products = Product.objects.all()
    return render(request, 'myapp/index.html', locals())



# def myview(request, cate):
#     category = Categories.objects.get(category_name=cate)
#     return render(request, 'myapp/product_list.html', {'category':category})
'''
-product_details = details of a product
-category_list = list of categories
-product_list_with_same_category - self explanatory
-searched-products - products from seach results 
'''

# def products(request, product_slug):
#     catego = Category.objects.get(slug = category_slug)
#     products_with_same_category = Category.product_set.all()
#     return render(request, 'myapp/product_list.html', {'category':products_with_same_category})


def product_list_with_same_category(request, category_slug):
    category  = get_object_or_404(Category,  slug = category_slug)
    
    categories = Category.objects.all()

    try:
        cat1 = categories[:1].get()
    except Exception as e:
        pass

    try:
        cat2 = categories[1:2].get()
    except Exception as e:
        pass

    try:
        cat3 = categories[2:3].get()
    except Exception as e:
        pass
    
    
    try:
        cat4 = categories[3:4].get()
    except Exception as e:
        pass
    
    try:
        cat5 = categories[4:5].get()
    except Exception as e:
        pass
    
    try:
        cat6 = categories[5:6].get()
    except Exception as e:
        pass
    
    try:
        cat7 = categories[6:7].get()
    except Exception as e:
        pass
    
    try:
        cat8 = categories[7:8].get()
    except Exception as e:
        pass
    
    try:
        cat9 = categories[8:9].get()
    except Exception as e:
        pass
    
    try:
        cat10 = categories[9:10].get()
    except Exception as e:
        pass
    
    
    try:
        cat11 = categories[10:11].get()
    except Exception as e:
        pass

    try:
        cat12 = categories[11:12].get()
    except Exception as e:
        pass
    
    try:
        cat13 = categories[12:13].get()
    except Exception as e:
        pass
    
    try:
        cat14 = categories[13:14].get()
    except Exception as e:
        pass
    
    try:
        cat15 = categories[14:15].get()
    except Exception as e:
        pass
    
    try:
        cat16 = categories[15:16].get()
    except Exception as e:
        pass
    
    try:
        cat17 = categories[16:17].get()
    except Exception as e:
        pass
    
    try:
        cat18 = categories[17:18].get()
    except Exception as e:
        pass
    
    try:
        cat19 = categories[18:19].get()
    except Exception as e:
        pass
    
    try:
        cat20 = categories[19:20].get()
    except Exception as e:
        pass

    try:
        cat21 = categories[20:21].get()
    except Exception as e:
         pass

    return render(request, 'myapp/product_list.html', locals())

def sign_up(request):
    print(request.POST)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        state = request.POST['state']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']

        if first_name:
            print('great')
            if last_name:
                print('great')
                if email:
                    print('great')
                    if password:
                        print('great')
                        if repeatpassword:
                            print('great')
                            return render(request, 'registration/signup_account.html', {'message':message})
                        else:
                            message = "This Field cannot be empty"
                            return render(request, 'registration/signup_account.html', {'message':message})
    else:
        return render(request, 'registration/signup_account.html')

# def arts_and_carts(request):
#     return render(request, 'myapp/arts-and-carts.html')

# def automotive(request, cate):
#     catego = Categories.objects.get(category_name=cate)
#     return render(request, 'myapp/automotive.html', {'cate':cate})

# def baby_wear(request):
#     return render(request, 'myapp/baby_wear.html')

# def beauty_products(request):
#     return render(request, 'myapp/beauty_products.html')

# def books(request):
#     return render(request, 'myapp/books.html')

# def computers(request):
#     return render(request, 'myapp/computers.html')

# def electronics(request):
#     return render(request, 'myapp/electronics.html')

# def women(request):
#     return render(request, 'myapp/women.html')

# def men(request):
#     return render(request, 'myapp/men.html')

# def girl(request):
#     return render(request, 'myapp/girl.html')

# def girl(request):
#     return render(request, 'myapp/girl.html')

# def health(request):
#     return render(request, 'myapp/health.html')

# def home_products(request):
#     return render(request, 'myapp/home_products.html')

# def industrial(request):
#     return render(request, 'myapp/industrial.html')

# def agro_products(request):
#     return render(request, 'myapp/agro_products.html')

# def food(request):
#     return render(request, 'myapp/food.html')

# def animals(request):
#     return render(request, 'myapp/animals.html')

# def services(request):
#     return render(request, 'myapp/services.html')

# def cars(request):
#     return render(request, 'myapp/cars.html')

# def games(request):
#     return render(request, 'myapp/games.html')