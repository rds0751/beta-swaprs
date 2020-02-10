from django.contrib import admin

from .models import Product, Category, ProductImage, Tag, CategoryImage, Featured, Wish

class FeaturedProductsAdmin(admin.ModelAdmin):
    class Meta:
        model = Featured
        
admin.site.register(Featured, FeaturedProductsAdmin)

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage

class TagInline(admin.TabularInline):
    prepopulated_fields = {"slug": ('tag',)}
    extra = 1
    model = Tag

    
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    
    
class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('__str__', 'description', 'category', 'live_link',)
    inlines = [TagInline, ProductImageInline]
    search_fields = ['title', 'description', 'category__title', 'category__description', 'tag__tag']
    list_filter = ['timestamp', 'updated']
    list_editable = ['description',]
    prepopulated_fields = {"slug": ('title',)}
    readonly_fields = ['category', 'live_link', 'timestamp', 'updated',]
    
    class Meta:
        model = Product
       
    
    def live_link(self, obj):
        link = "<a href='/products/"+ str(obj.slug) + "/'>" + obj.title + "</a>"
        return link
    
    live_link.allow_tags = True

admin.site.register(Product, ProductAdmin)


class WishAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('__str__', 'category',)
    
    class Meta:
        model = Wish

admin.site.register(Wish, WishAdmin)


   
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    inlines = [CategoryImageInline]
    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)









