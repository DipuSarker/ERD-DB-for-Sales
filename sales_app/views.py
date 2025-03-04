from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Customer, Category, Product, Invoice, InvoiceProduct
from django.core.serializers import serialize
from django.db.models import Avg, Max, Min, Sum, Count, Q

def home(request):
    # Update,create
    try:
        created, updated = Product.objects.update_or_create(
            name='Mango',
            defaults={
                'price':666,
                'unit':'per piece',
                'img_url':'https://www.google.com',
                'category_id':1,
                'user_id':1
            }
        )
        if created:
            message = 'Product created successfully'
        else:
            message = 'Product updated successfully'
            
        return JsonResponse({'message': message})
        
    except Exception:
        return JsonResponse({'message': 'Product not found'})
    # updated
    # try:
    #     product = Product.objects.get(id=22)
        
    #     product.name = 'Depseek'
    #     product.price = 5000
    #     product.unit = 'per hour'
        
    #     product.save()
    #     return JsonResponse({'message': 'Product updated successfully'})
    # except Exception:
    #     return JsonResponse({'message': 'Product not found'})
    
    # delete product
    # try:
    #     del_product = Product.objects.get(id=25)
    #     del_product.delete()
    #     return JsonResponse({'message': 'Product deleted successfully'})
    # except Exception:
    #     return JsonResponse({'message': 'Product not found'})
    # new_product = Product.objects.create(
    #     name='OPEN aI',
    #     price=500,
    #     unit='per user',
    #     img_url='https://www.google.com',
    #     category_id=1,
    #     user_id=1
    # )
    # return JsonResponse({'message': 'Product created successfully', 'id': new_product.id})
    # products = (
    #     Product(name='OPEN aI',price=500,unit='per user',img_url='https://www.google.com', category_id=1,user_id=1),
    #     Product(name='OPEN aI',price=500,unit='per user',img_url='https://www.google.com', category_id=1,user_id=1),
    #     Product(name='OPEN aI',price=500,unit='per user',img_url='https://www.google.com', category_id=1,user_id=1),
    #     Product(name='OPEN aI',price=500,unit='per user',img_url='https://www.google.com', category_id=1,user_id=1)
    # )
    # Product.objects.bulk_create(products)
    # return JsonResponse({'message': 'All Products created successfully'})







    # res1 = Product.objects.filter(name__contains='PP').values()
    # res1 = Product.objects.filter(name__icontains='pp').values()
    # res1 = Product.objects.filter(name__startswith='P').values()
    # res1 = Product.objects.filter(name__endswith='r').values()
    # res1 = Product.objects.filter(Q(name__endswith='r') | Q(name__startswith='P')).values()
    #Range operator
    # res1 = Product.objects.filter(price__range=(700,1000)).values()
    # Membership operator(In)
    # res1 = Product.objects.filter(price__in=(100,200,300)).values()
    # Membership operator(Not In)
    # res1 = Product.objects.exclude(price__in=(100,200,300)).values()
    # or
    # res1 = Product.objects.exclude(price__range=(100,200,300)).values()
    
    # return JsonResponse({'data': list(res1)})

# def home(request):
#     customers = Customer.objects.all()
#     result = customers.values()
#     return JsonResponse({'data': list(result)})

# def home(request):
#     # customers = Customer.objects.all().values()
#     customers = Customer.objects.all().values('id', 'name', 'email')
#     return JsonResponse({'data': list(customers)})  

# def home(request):
#     customers = Customer.objects.all()
#     result = serialize('json', customers, fields=('name', 'email'))
#     return JsonResponse({'data': result})

# import json
# def home(request):
#     customers = Customer.objects.all()
#     data = serialize('json', customers)
#     return JsonResponse({'res': json.loads(data)})

# fetch single customer
# def home(request):
#     customer = Customer.objects.get(id=1)
#     return JsonResponse({'id': customer.id, 'name': customer.name})

# def home(request):
#     customer = Customer.objects.get(id=1)
#     customer_data = {'id': customer.id, 'name': customer.name}
#     return JsonResponse(customer_data)

# from django.forms.models import model_to_dict
# def home(request):
#     customer = Customer.objects.get(id=2)
#     return JsonResponse(model_to_dict(customer))

# def home(request):
#     customers = Customer.objects.first()
#     return JsonResponse({'name': customers.name, 'email': customers.email, 'id': customers.id})

# Filter
# def home(request):
#     #case-insensitive search
#     # customers = Customer.objects.filter(name__icontains='john').values()
#     #case-sensitive search
#     customers = Customer.objects.filter(name__contains='John').values()
#     return JsonResponse({'data': list(customers)})

# Exclude
# def home(request):
#     #case-insensitive search
#     # customers = Customer.objects.exclude(name__icontains='john').values()
#     #case-sensitive search
#     customers = Customer.objects.exclude(name__contains='John').values()
#     return JsonResponse({'data': list(customers)})

#Sorting record

# def home(request):
#     # ASC
#     # customers = Customer.objects.order_by('name').values()
#     # Desc
#     customers = Customer.objects.order_by('-name').values()
#     return JsonResponse({'data': list(customers)})

#limiting & Range

# def home(request):
#     customers = Customer.objects.all()[3:6].values()
#     return JsonResponse({'data': list(customers)})

#Counting

# def home(request):
#     customers = Customer.objects.count()
#     return JsonResponse({'customers': customers})

# Distict
# def home(request):
#     customers = Customer.objects.values('name').distinct()
#     return JsonResponse({'data': list(customers)})

# # Values Query
# def home(request):
#     customers = Customer.objects.values('name', 'email')
#     return JsonResponse({'data': list(customers)})

# # Values List Query
# def home(request):
#     customers = Customer.objects.values_list('name', flat=True)
#     return JsonResponse({'data': list(customers)})

# Chaning Query
# def home(request):
#     customers = Customer.objects.filter(name__contains='john').order_by('-created_at').values()
#     return JsonResponse({'data': list(customers)})

# Raw query
# def home(request):
#     query = "SELECT * FROM sales_app_customer where name=%s"
#     customers = Customer.objects.raw(query, ['Bob Brown'])
#     result = [{'name': customer.name, 'email': customer.email}for customer in customers]
#     return JsonResponse({'data': list(result)})


#Debugging

# def home(request):
#     customers = Customer.objects.all().values()
#     query = str(customers.query)
#     return JsonResponse({'query': query,'data': list(customers)})  

# from django.db.models import Avg, Max, Min, Sum, Count, Q

# def home(request):
#     agg = Product.objects.aggregate(
#         average_price = Avg('price'),
#         max_price = Max('price'),
#         min_price = Min('price'),
#         total_price = Sum('price'),
#         count = Count('id')
#     )
#     return JsonResponse(agg)

# def home(request):
#     agg = Product.objects.aggregate(Min('price'))
#     # return HttpResponse(agg['price__avg'])
#     return HttpResponse(agg['price__min'])

# def home(request):
    # Equal
    # products = Product.objects.filter(price=500).values()
    
    # Less than
    # products = Product.objects.filter(price__lt=500).values()
    
    # greater than
    # products = Product.objects.filter(price__gt=500).values()
    
    # less than or equal
    # products = Product.objects.filter(price__lte=500).values()
    
    # greater than or equal
    # products = Product.objects.filter(price__gte=500).values()
    # return JsonResponse({'data': list(products)})
    
    # Product combine or and Q
    # res6 = Product.objects.filter(Q(name="Laptop") | Q(price__lt = 1000) | Q(price__gt = 500)).values()
    # res6 = Product.objects.filter(Q(name="Laptop") & Q(price__lt = 2000) & Q(price__gt = 500)).values()
    # return JsonResponse({'data': list(res6)})


    
