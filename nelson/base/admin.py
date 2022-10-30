from django.contrib import admin
from .models import Category, Product, ProductPhoto, HomeBanner, Furniture, DiscountBanner, Advantages, Review, Brands
from .models import Contact, Subscribe, WriteUs, Blog, BlogBanner, AboutBanner, About, Team, FaqBanner, Faq, ShopBanner
from .models import ContactBanner


admin.site.register(Category)
admin.site.register(HomeBanner)
admin.site.register(Furniture)
admin.site.register(DiscountBanner)
admin.site.register(Advantages)
admin.site.register(Review)
admin.site.register(Brands)
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(WriteUs)
admin.site.register(Blog)
admin.site.register(BlogBanner)
admin.site.register(About)
admin.site.register(AboutBanner)
admin.site.register(Team)
admin.site.register(Faq)
admin.site.register(FaqBanner)
admin.site.register(ContactBanner)
admin.site.register(ShopBanner)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('title', ), }


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_filter = ('product', )

