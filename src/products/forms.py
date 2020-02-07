from django.forms import ModelForm

from .models import Product, ProductImage, Wish

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image1', 'image2', 'image3', 'location', 'ty_pe')

class WishForm(ModelForm):
	class meta:
		model = Wish
		fields = ('location','ty_pe','keywords','category')
        
        
class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image', 'featured_image', )
