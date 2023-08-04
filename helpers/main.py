from openpyxl import load_workbook
import xml.etree.ElementTree as ET
import re


def get_data_from_workbook(filename: str):
    wb = load_workbook(filename)
    worksheet = wb.worksheets[0]
    data = []
    for col in worksheet.rows:
        category, name, brand, vendor, size, model, gender, body = col
        data.append(
            {
                "category": category.value,
                "name": name.value,
                "brand": brand.value,
                "vendor": vendor.value,
                "size": size.value,
                "model": model.value,
                "gender": gender.value,
                "body": body.value,
            }
        )
    return data


def format_price(price: int):
    price = f"{price:_}".replace("_", " ")
    return f"{price} UZS"


def remove_html_from_text(text: str):
    pattern = re.compile('<.*?>')
    result = re.sub(pattern, '', text)
    return result





