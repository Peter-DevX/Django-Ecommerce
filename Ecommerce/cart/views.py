# from django.shortcuts import render, get_object_or_404
# from .cart import Cart
# from django.http import HttpResponse
# from store.models import Product
# from django.http import JsonResponse

# def cart_summary(request):
#     return render(request, "cart_summary.html", {})


# def cart_add(request):
#     # Get the cart
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         # get stuff
#         product_id = int(request.POST.get('product_id'))
#         # lookup product in DB
#         product = get_object_or_404(Product, id=product_id)

#         # save to session
#         cart.add(product=product)

#         cart_quantity = cart.__len__()


#         # return reesponse
#         # response = JsonResponse({'Product Name: ':product.name})
#         response = JsonResponse({'qty': cart_quantity})
    


# def cart_delete(request):
#     pass

# def cart_update(request):
#     pass















from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.http import HttpResponse
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product)
            return JsonResponse({'qty': cart.__len__()})
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid product ID'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_delete(request):
    return JsonResponse({'error': 'Not implemented'}, status=501)

def cart_update(request):
    return JsonResponse({'error': 'Not implemented'}, status=501)