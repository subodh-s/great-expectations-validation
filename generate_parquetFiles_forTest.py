import pandas as pd


data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Sana", "vi", "Megha", "To", "Anjali"],
    "DepartmentName": ["HR", "", "Finance", "Marketing", "Sales"],
    "Salary": [55000.78, 62000.23, 48000, 51000, 67000]
}

df = pd.DataFrame(data)
df.to_parquet("./bulk_csv/test_employees_2.parquet", index=False)
