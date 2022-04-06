from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choise import state_choices, price_choices, bedroom_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    contex = {'listing': listing}

    return render(request, 'listings/listing.html', contex)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
