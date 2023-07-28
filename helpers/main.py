from openpyxl import load_workbook


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
