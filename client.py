import requests

def get_product_data_by_id(product_id):
    url = f"https://dummyjson.com/products/{product_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx HTTP status codes
        product_data = response.json()
        return product_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage:
product_id = 12  # Replace with the desired product ID
product_data = get_product_data_by_id(product_id)

if product_data:
    print("Product Data:")
    print(product_data)
else:
    print("Failed to retrieve product data.")
