import csv
import json
import pandas as pd
import numpy as np
import os

def clean_csv(csvFilePath):
  df = pd.read_csv(csvFilePath)
  column_name_map = {
    "ProductID": "product_id",
    "ProductName" : "product_name",
    "ProductBrand": "product_branch",
    'Gender': "gender",
    "Price (INR)": "sell_price",
    "NumImages": "images_count",
    "Description": "description",
    "PrimaryColor": "primary_color"
  }
  df.rename(columns=column_name_map, inplace=True)
  df.to_csv('products_clean.temp.csv', index=False)

def csv_to_json(csvFilePath, jsonFilePath):
  jsonArray = []

  with open(csvFilePath, encoding='utf-8') as csvFile:
    csvReader = csv.DictReader(csvFile)
    
    for row in csvReader:
      jsonArray.append(row)

  with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
    jsonString = json.dumps(jsonArray, indent=4)
    jsonFile.write(jsonString)
    
  os.remove('products_clean.temp.csv')

csvFilePath = 'products.csv'
jsonFilePath = 'products.json'
clean_csv('products.csv')
csv_to_json('products_clean.temp.csv', jsonFilePath)

