from django.shortcuts import render, HttpResponse, redirect, get_object_or_404


def wishlist(request):
    return render(request, 'wishlist.html')


def wishlist_add(request):
    pass


def wishlist_remove(request):
    pass
