from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request):
    """
    DFR API VIEW
    """
    # model_data = Product.objects.all().order_by("?").first()
    instance = Product.objects.all().order_by("?").first()

    data = {}

    # if model_data:
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        # """
        # alternatively I can do the same in clean and easy way by importing model_to_dict from django.forms.models
        # """
        # data = model_to_dict(model_data, fields = ['id', 'title', 'content', 'price'])
        
    if instance:
        data = ProductSerializer(instance).data # data refers to coming data from the serializer.
    
    return Response(data)


@api_view(["POST"])
def api_home_post(request):
    """
    DFR API VIEW
    """
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data = serializer.data
        return Response(data)
    
    return Response({"invalid": "Not good data"}, status = 404)