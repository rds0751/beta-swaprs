from django.forms import ModelForm, Select, Textarea, TextInput
from .models import Product, Wish, Category

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'image1', 'image2', 'image3', 'location', 'ty_pe')
        categories = Category.objects.filter(title=True)
        categories = (
                   ('mixed', 'Mixed (i.e. some color or grayscale, some black and white)'),
                   ('color_grayscale', 'Color / Grayscale'),
                   ('black_and_white', 'Black and White only'),
                   )
        widgets = {'category': Select(choices=categories),
        'description': Textarea(attrs={'rows': 5, 'class': 'form-control', 'placeholder': 'Item Description'}),
        }

    

class WishForm(ModelForm):
	class Meta:
		model = Wish
		fields = ('location','ty_pe','keywords','category')
		categories = (
                   ('mixed', 'Mixed (i.e. some color or grayscale, some black and white)'),
                   ('color_grayscale', 'Color / Grayscale'),
                   ('black_and_white', 'Black and White only'),
                   )
		widgets = {'category': Select(choices=categories),
        }
        
