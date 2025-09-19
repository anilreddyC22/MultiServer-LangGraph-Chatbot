import requests
from langchain.tools import tool
from config.settings import WEBFLUX_SERVICE

@tool
def get_all_products() -> str:
    """
    Fetch all products.
    """
    try:
        response = requests.get(f"{WEBFLUX_SERVICE}")
        response.raise_for_status()
        products = response.json()
        if not products:
            return "No products found."
        names = [p['name'] if isinstance(p, dict) and 'name' in p else str(p) for p in products]
        return f"All products: {', '.join(names)}"
    except requests.RequestException as e:
        return f"Error fetching products: {str(e)}"

@tool
def get_products_below_price(price: float) -> str:
    """
    Fetch products below a certain price.
    """
    try:
        response = requests.get(f"{WEBFLUX_SERVICE}/filter/price/{price}")
        response.raise_for_status()
        products = response.json()
        if not products:
            return f"No products found below price {price}."
        names = [p['name'] if isinstance(p, dict) and 'name' in p else str(p) for p in products]
        return f"Products below price {price}: {', '.join(names)}"
    except requests.RequestException as e:
        return f"Error fetching products below price {price}: {str(e)}"

@tool
def get_products_by_name(name: str) -> str:
    """
    Fetch products by name.
    """
    try:
        response = requests.get(f"{WEBFLUX_SERVICE}/search/{name}")
        response.raise_for_status()
        products = response.json()
        if not products:
            return f"No products found with name '{name}'."
        
        details = []
        for p in products:
            pname = p.get("name", "Unknown")
            pdata = p.get("data", {})  # nested object
            
            price = pdata.get("price", "N/A")
            color = pdata.get("color", "N/A")
            capacity = pdata.get("capacity", "N/A")
            
            details.append(
                f"- **{pname}** (Price: {price}, Color: {color}, Capacity: {capacity})"
            )
        
        return f"Products with name '{name}':\n\n" + "\n".join(details)
    except requests.RequestException as e:
        return f"Error fetching products with name '{name}': {str(e)}"

    


webflux_tools = [get_all_products, get_products_below_price, get_products_by_name]