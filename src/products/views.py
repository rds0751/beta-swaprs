import os
from itertools import chain
from mimetypes import guess_type

from django.conf import settings
from wsgiref.util import FileWrapper
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.shortcuts import render, Http404, HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import slugify


from src.cart.models import Cart

from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm

def check_product(user, product):
    try:
        if product in user.userpurchase.products.all():
            return True
        else:
            return False
    except:
        return False


def download_product(request, slug, filename):
    product = Product.objects.get(slug=slug)


    if product in request.user.userpurchase.products.all():
        product_file = str(product.download)
        file_path = os.path.join(settings.PROTECTED_UPLOADS, product_file)
        wrapper = FileWrapper(file(file_path))
        response = HttpResponse(wrapper, content_type=guess_type(product_file))
        response['Content-Diposition'] = 'attachment;filename=%s' %filename
        response['Content-Type'] = ''
        response['X-SendFile'] = file_path
        return response
    else:
        raise Http404
        
    #return render_to_response("products/single.html", locals(), context_instance=RequestContext(request))



def list_all(request):
    products = Product.objects.filter(active=True)
    context = {
        "products": products,
    }
    return render(request, "products/all.html", context)

def add_product(request):
    
    form = ProductForm(request.POST or None)
        
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.slug = slugify(form.cleaned_data['title'])
        product.active = True
        product.save()
        return HttpResponseRedirect('/products/%s'%(product.slug))
    
    context = {
        "form": form,
    }

    return render(request, "products/edit.html",context)

def add_wish(request):
    
    form = WishForm(request.POST or None)
        
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect('/products/%s'%(product.slug))
    
    context = {
        "form": form,
    }

    return render(request, "products/edit.html",context)



def edit_product(request, slug):
    instance = Product.objects.get(slug=slug) #this is the product instance
    if request.user == instance.user:
        form = ProductForm(request.POST or None, instance=instance)
        
        if form.is_valid():
            product_edit = form.save(commit=False)
            
            product_edit.save()
        
        context = {"form": form}
        return render(request, "products/edit.html", context)
    else:
        raise Http404


def edit_wish(request, slug):
    instance = Wish.objects.get(slug=slug) #this is the product instance
    if request.user == instance.user:
        form = WishForm(request.POST or None, instance=instance)
        
        if form.is_valid():
            product_edit = form.save(commit=False)
            
            product_edit.save()
        
        context = {"form": form}
        return render(request, "products/edit.html", context)
    else:
        raise Http404

    

def single(request, slug):
    product = Product.objects.get(slug=slug)
    image1 = product.image1
    categories = product.category_set.all()
    if request.user==product.user:
        edit = True
    else:
        edit = False
    related = []
    if len(categories) >= 1: 
        for category in categories:
            products_category = category.products.all()
            for item in products_category:
                if not item == product:
                    related.append(item)
        
    
    
    
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        for item in cart.cartitem_set.all():
            if item.product == product:
                in_cart = True
    except:
        in_cart = False

    
    context = {
        "product": product,
        "categories": categories,
        "edit": edit,
        "images": image1,
    }
    
    
    return render(request,  "products/single.html", context)



def search(request):
    try:
        q = request.GET.get('q', '')
    except:
        q = False
    
    if q:
        query = q
    
    product_queryset = Product.objects.filter(
        Q(title__icontains=q)|
        Q(description__icontains=q)
    )
    category_queryset = Category.objects.filter(
        Q(title__icontains=q)|
        Q(description__icontains=q)
    )

    
    results = list(chain(product_queryset, category_queryset))

    context = {
        "results": results
    }
        
    return render(request, "products/search.html", context)


def category_single(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except:
        raise Http404   
    
    products = category.products.all()
    
    related = []
    for item in products:
        product_categories = item.category_set.all()
        for single_category in product_categories:
            if not single_category == category:
                related.append(single_category)
    
    context = {
        "category": category,
        "products": products,
        "related": related
    }
    return render(request, "products/category.html", context)
    