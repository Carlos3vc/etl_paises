from datetime import datetime

def transform(data):
    """
    transformamos la data de paises
    """
    transform_data = []
    for country in data:
        nombre = country.get("name", {}).get("common", "Sin nombre")
        
        capital_list = country.get("capital", [])
        capital = capital_list[0] if capital_list else "Sin capital"

        region = country.get("region", "Sin región")
        poblacion = country.get("population", 0)

        transform_data.append((nombre, capital, region, poblacion))
    return transform_data