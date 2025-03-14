import requests
import csv

# Fetch all available products from the API
all_products_url = "https://endoflife.date/api/all.json"
try:
    response = requests.get(all_products_url, timeout=10)
    response.raise_for_status()  # Raise an error if the request was unsuccessful
    products = response.json()  # List of all available products
except requests.RequestException as e:
    print(f"Error fetching product list: {e}")
    products = []  # Default to empty list if request fails

# CSV file
csv_filename = "eol_data.csv"

# CSV Header
header = ["product", "cycle", "eol", "latest"]

# Open CSV file for writing
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header row

    # Search for data for each product
    for product in products:
        url = f"https://endoflife.date/api/{product}.json"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()  # Parse the response

            for item in data:
                cycle = item.get("cycle", "N/A")  # If no cycle use N/A
                eol = item.get("eol", "N/A")
                latest = item.get("latest", "N/A")
                writer.writerow([product, cycle, eol, latest])  # Write data to CSV

        except requests.RequestException as e:
            print(f"Error fetching data for {product}: {e}")
