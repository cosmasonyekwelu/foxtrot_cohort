from django.http import JsonResponse


# ====== SAMPLE PRODUCT DATA (List of Dicts) ====== #
market_product = [
    {
        "id": 1,
        "name": "Wireless Mouse",
        "category": "Electronics",
        "price": 29.99,
        "stock": 120,
        "description": "A smooth and responsive wireless mouse."
    },
    {
        "id": 2,
        "name": "Laptop Backpack",
        "category": "Accessories",
        "price": 49.99,
        "stock": 80,
        "description": "Water-resistant backpack with padded laptop compartment."
    },
    {
        "id": 3,
        "name": "Bluetooth Speaker",
        "category": "Electronics",
        "price": 59.99,
        "stock": 40,
        "description": "Portable speaker with rich bass and long battery life."
    },
    {
        "id": 4,
        "name": "Running Sneakers",
        "category": "Fashion",
        "price": 89.99,
        "stock": 50,
        "description": "Lightweight running shoes designed for comfort and speed."
    },
    {
        "id": 5,
        "name": "Smart Watch",
        "category": "Electronics",
        "price": 129.99,
        "stock": 35,
        "description": "Touchscreen smartwatch with fitness tracking features."
    },
    {
        "id": 6,
        "name": "Office Chair",
        "category": "Furniture",
        "price": 199.99,
        "stock": 20,
        "description": "Ergonomic office chair with lumbar support."
    },
]


# ====== VIEW: GET ALL PRODUCTS ====== #
def get_product(request):
    return JsonResponse(
        {
            "message": "Get Products Successful",
            "products": market_product
        },
    )
