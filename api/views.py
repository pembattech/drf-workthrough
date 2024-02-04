from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["POST"])
def api_home(request):
    """
    DFR API VIEW
    """
    model_data = Product.objects.all().order_by("?").first()

    data = {}

    if model_data:
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        """
        alternatively I can do the same in clean and easy way by importing model_to_dict from django.forms.models
        """
        data = model_to_dict(model_data, fields = ['id', 'title', 'content', 'price'])
    
    return JsonResponse(data)
