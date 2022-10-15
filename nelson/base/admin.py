from django.contrib import admin
from .models import Category, Product, ProductPhoto, HomeBanner, Furniture, DiscountBanner, Advantages, Review, Brands
from .models import Contact, Subscribe


admin.site.register(Category)
admin.site.register(HomeBanner)
admin.site.register(Furniture)
admin.site.register(DiscountBanner)
admin.site.register(Advantages)
admin.site.register(Review)
admin.site.register(Brands)
admin.site.register(Contact)
admin.site.register(Subscribe)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('title', ), }


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_filter = ('product', )

