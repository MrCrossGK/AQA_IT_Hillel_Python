import pathlib


def address_assign(file_format: str):
    current_path = pathlib.Path(__file__)
    current_folder = current_path.parent
    directories = [d for d in current_folder.iterdir() if d.is_dir()]

    for fold in directories:
        if fold.name == f"{file_format}_lib":
            lib_address = fold
            # print(f"Це адреса {file_format} файлів: {lib_address}")
            files = [f for f in lib_address.iterdir() if f.suffix == f".{file_format}"]
            # for file in files:
            #     print(file)
            return files


def end_blank_remover(data):
    for elem in data:
        if elem[-1] == "":
            elem.pop()
    return data


# print(address_assign("json"))
