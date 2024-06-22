def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []

            for cat in file.readlines():
                try:
                    cats.append(
                        {
                            "id": cat.split(",")[0],
                            "name": cat.split(",")[1],
                            "age": int(cat.split(",")[2].strip()),
                        }
                    )
                except IndexError:
                    continue

            return cats

    except FileNotFoundError:
        return []


cats_info = get_cats_info("cats.txt")
print(cats_info)
