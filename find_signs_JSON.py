import json
import os
import csv


def find_signs(path_to_fully_images, labels_to_find, save_csv_directory='output', load_json_file_directory='annotations'):
    print("""
    1 - Znajdź znaki z listy
    2 - Stwórz liste z etykietami
    0 - Powrót
    """)
    path_to_annotations = os.path.join(path_to_fully_images, load_json_file_directory)  # wybranie folderu z plikami JSON
    files_list = os.listdir(path_to_annotations)
    images = []
    label_list = []
    respond = input("Wybierz: ")
    while respond != "0":
        if respond == "1":
            for label_of_sign in labels_to_find:
                with open(f'{save_csv_directory}/imagelist_label_{label_of_sign}.csv', mode="w", newline="") as csv_file:
                    i = 1
                    new_row = csv.writer(
                        csv_file,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL
                        )
                    for file_ in files_list:
                        i += 1
                        json_file = os.path.join(path_to_annotations, file_)
                        print(f"{i}/{len(files_list)} [{len(images)} found]")
                        with open(json_file, "r") as f:
                            steam = json.load(f)
                            objects = steam['objects']
                            for properties in objects:
                                label = properties["label"]
                                if label == label_of_sign and file_ not in images:
                                    file_ = file_[:-5]
                                    images.append(file_)
                                    new_row.writerow([file_])
                                    print("FILE", file_)
                                    break
                respond = "0"
                print("Number of images with choosen sign: ", len(images))
                print(f"CSV file with image name has been save as 'imagelist_{label_of_sign}.csv'")
        elif respond == "2":
            with open(f'{save_csv_directory}/label_list.csv', mode="w", newline="") as csv_file:
                i = 1
                new_row = csv.writer(
                    csv_file,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL
                    )
                for file_ in files_list:
                    i += 1
                    json_file = os.path.join(path_to_annotations, file_)
                    print(f"{i} / {len(files_list)}")
                    with open(json_file, "r") as f:
                        steam = json.load(f)
                        objects = steam['objects']
                        for properties in objects:
                            label = properties["label"]
                            if label in label_list:
                                pass
                            else:
                                label_list.append(label)
                                new_row.writerow([label])
                                print("New label", label)
            respond = "0"
            print("Number of lables: ", len(label_list))
            print("CSV file with labels has been save as 'labellist.csv'")
        else:
            pass
    print("Found all json files")
    print("Done!")
