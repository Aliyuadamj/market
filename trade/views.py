from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from trade.models import Product,Category

from .forms import ProductForm

def products(request):
    products = Product.objects.all()
    if request.method == "POST":
        data = request.POST
        form = ProductForm(data)
        if form.is_valid():
            obj = form.save()
            product_form = ProductForm()
            return render(request, "trade/products.html", context={
                "products": products,
                "product_form": product_form,
                "message": "Product Submitted successfully"
            })
        else:
            return render(request, "trade/products.html", context={
                "products": products,
                "product_form": product_form,
            })
    product_form = ProductForm()
    return render(request, "trade/products.html", context={
        "products": products,
        "product_form": product_form
    })

def product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "trade/product.html", context={
        "product": product
    })

def categorys(request):
    categorys = Category.objects.all()
    return render(request, "trade/categorys.html", context={
        "categorys":categorys})

def category(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, "trade/category.html", context={
        "category":category} )





# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#         return render(request, "name.html", {"form": form})


#     if form.is_valid():
#         subject = form.cleaned_data["subject"]
#         message = form.cleaned_data["message"]
#         sender = form.cleaned_data["sender"]
#         cc_myself = form.cleaned_data["cc_myself"]
#         recipients = ["info@example.com"]
#     if cc_myself:
#         recipients.append(sender)
#         send_mail(subject, message, sender, recipients)
#         return HttpResponseRedirect("/thanks/")