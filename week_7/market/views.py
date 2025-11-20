from django.http import JsonResponse
from .models import Market_Product
import json


def get_product(request):
    # print(request.method)
    if request.method == "GET":
        category = request.GET.get("category")

        all_products = Market_Product.objects.all().values()
        return JsonResponse({"message": "Get product Successful", "products": list(all_products)})
    else:
        return JsonResponse({"message": "You are using the wrong method"}, status=405)


def create_product(request):
    if request.method == "POST":
        incoming_data = request.body.decode()
        to_dict = json.loads(incoming_data)

        Market_Product.objects.create(
            name=to_dict["name"],
            category=to_dict["category"],
            price=to_dict["price"],
            stock=to_dict["stock"],
            description=to_dict["description"],
            is_available=to_dict["is_available"],
        )

        return JsonResponse({"message": "Product created successful"}, status=201)
    else:
        return JsonResponse({"message": "You are using the wrong method"}, status=405)


def update_product(request, id):
    if request.method == "PUT":
        try:
            existing_product = Market_Product.objects.get(id=id)
        except Market_Product.DoesNotExist:
            return JsonResponse({"message": "What You are looking for does nor exist"}, status=404)

        incoming_data = request.body.decode()
        to_dict = json.loads(incoming_data)

        existing_product.name = to_dict["name"]
        existing_product.category = to_dict["category"]
        existing_product.price = to_dict["price"]
        existing_product.stock = to_dict["stock"]
        existing_product.description = to_dict["description"]

        return JsonResponse({"message": "Product update successful"})
    else:
        return JsonResponse({"message": "You are using the wrong method"}, status=405)


def delete_product(request, id):
    if request.method == "DELETE":
        try:
            existing_product = Market_Product.objects.get(id=id)
        except Market_Product.DoesNotExist:
            return JsonResponse({"message": "What You are looking for does nor exist"}, status=404)

        existing_product.delete()

        return JsonResponse(data=None, safe=False, status=204)
    else:
        return JsonResponse({"message": "You are using the wrong method"}, status=405)
