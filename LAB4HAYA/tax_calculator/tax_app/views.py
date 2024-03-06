from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Define the tax rate
tax_rate = 0.15

def default(request):
    return HttpResponse("<h1>This is a site to calculate tax.</h1>")

def calculate_tax(request, number):
    total_price = float(number) * (1 + tax_rate)
    return HttpResponse(f"<h1>Total price after 15% tax: {total_price}</h1>")

def tax_rate_view(request):
    return render(request, "tax_rate.html", {"tax_rate": tax_rate})
