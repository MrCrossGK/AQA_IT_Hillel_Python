import pathlib
import os


def address_assign(file_format: str) -> list:
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


def mod_addr_assign(file_format: str) -> list:
    adr_list = []
    current_path = pathlib.Path(__file__).parent.parent

    for item in os.walk(str(current_path)):
        path_to_folder, folders, files = item
        adr_list += [(pathlib.Path(path_to_folder, file_name)) for file_name in files if file_name.endswith(f".{file_format}")]
    return adr_list


def final_addr_assign(file_format: str) -> list:  # GPT best variant
    current_path = pathlib.Path(__file__).parent.parent
    return list(current_path.rglob(f"*.{file_format}"))


print(address_assign("csv"))
print(mod_addr_assign("csv"))
print(final_addr_assign("csv"))

