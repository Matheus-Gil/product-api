from fastapi import status

BASE_URL = "/products"

def test_get_all_products(test_client):
    response = test_client.get(f"{BASE_URL}/")

    assert response.status_code == status.HTTP_200_OK

def test_create_product(test_client):
    response = test_client.post(
        f"{BASE_URL}/",
        json={
            "name": "RTX 3000",
            "price": 2000,
            "category": "COMPONENTS",
            "subcategory": "GPU",
            "manufacturer": "NVIDIA",
            "stock": 5
        }
    )

    print(response.json())
    assert response.status_code == status.HTTP_201_CREATED

def test_find_product_by_id(test_client):
    response = test_client.get(f"{BASE_URL}/1")
    assert response.status_code == status.HTTP_200_OK