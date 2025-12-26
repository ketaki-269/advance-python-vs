#23-12-25
#module ,package , library 
# collection of module - package
# collection of package library 


import numpy as np
import pandas as pd

#set random seed for reproducibility
np.random.seed(42)
# with the help of random we can generate data
#42 its is a psedo algorithms
# 42 when we share data between multiple user seed(42) is use that shared data will same, as number 42 - kabhi na chnage hone vala segment to represent kerta hai 
# Its random.seed(42) is a universal code to create reproducibility

#generate sample data
num_records = 500

order_ids =np.arange(1001,1001 + num_records)
dates = pd.date_range(starts="2023-01-01",periods=num_records, freq="D")
#freq="D" -  this repersent the  data type of date , date range pandas ka function hai kyuki ye numpy ke pass nhi hai 
ages=np.random.randint(18,65,num_records)
genders=np.random_choice(["Male","Female"],num_records)
cities = np.random.choice(["New York","Los Angeles","Chicago","Houston","Miami"],num_records)
product_categories = np.random.choic(["Electronics","Clothing","Home & Kitchen ","Beauty","Sports"],num_records)
quantities = np.random.randint(1,12,num_records)
unit_prices = np.random.randint(1,500,num_records)
total_sales=quantities * unit_prices
payments_methods = np.random.choice({"Credit Card","Paypal","Debit Card","Cash"},num_records)


# Create DataFrame
df_eds = pd.DataFrame({
    "Order ID": order_ids,
    "Date": dates,
    "Age": ages,
    "Gender": genders,
    "City": cities,
    "Category": product_categories,
    "Quantity": quantities,
    "Unit Price": unit_prices,
    "Total Sales": total_sales,
    "Payment Method": payments_methods
})

print(df.head())
eds_file_path = "C:/python_libraries/sales_data_csv"
df_eds.to_csv(eds_file_path, index = False)

eds_file_path


#create dataframe