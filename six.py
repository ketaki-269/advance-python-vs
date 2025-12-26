#24-12-25
import numpy as np
import pandas as pd

np.random.seed(42)

num_records = 500

# Generate data
order_ids = np.arange(1001, 1001 + num_records)

dates = pd.date_range(start="2023-01-01", periods=num_records, freq="D")

ages = np.random.randint(18, 65, num_records)

gender = np.random.choice(["Male", "Female"], num_records)

cities = np.random.choice(["New York", "Los Angeles", "Chicago"], num_records)

product_categories = np.random.choice(["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Sports"],num_records)

quantities = np.random.randint(1, 10, num_records)

unit_prices = np.random.randint(10, 500, num_records)

total_sales = quantities * unit_prices
payment_method = np.random.choice(["Credit Card", "PayPal", "Debit Card", "Cash"],num_records)

# Create DataFrame
df_eds = pd.DataFrame({
    "Order ID": order_ids,
    "Date": dates,
    "Age": ages,
    "Gender": gender,
    "City": cities,
    "Category": product_categories,
    "Quantity": quantities,
    "Unit Price": unit_prices,
    "Total Sales": total_sales,
    "Payment Method": payment_method
})

print(df_eds.head())
#save to csv 
eds_file_path = "C:/python_libraries/sales_data_csv"
df_eds.to_csv(eds_file_path, index = False)
#return file path
eds_file_path