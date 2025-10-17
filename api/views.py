from django.http import JsonResponse
import requests
from datetime import datetime, timezone

def me(request):
    try:
        # Fetch cat fact from API
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        cat_fact = response.json().get("fact", "No fact available 🐱")
    except Exception as e:
        cat_fact = "Could not fetch cat fact 🐱"

    data = {
        "status": "success",
        "user": {
            "email": "usmanjoseph2121@gmail.com",
            "name": "Usman Joseph",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JsonResponse(data)
