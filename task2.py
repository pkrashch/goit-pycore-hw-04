def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                cleaned_line = line.strip()
                if not cleaned_line: #for empty lines
                    continue
                try:
                    cat_id, cat_name, age = cleaned_line.split(',')
                except ValueError:
                    # Additional validation. Skipping incorrect lines
                    print(f"Попередження: Некоректний формат даних у рядку: '{cleaned_line}'. Пропущено.")
                    continue
                #Create dictionary with cat's data
                cat_dict = {
                    "id": cat_id,
                    "name": cat_name,
                    "age": age
                }
                #add dictionary to final list
                cats_info.append(cat_dict)
    except FileNotFoundError:
        return []
    return cats_info