import os
import shutil
import cv2
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--copy", action="store_true")
parser.add_argument("--resize", action="store_true")
parser.add_argument("--pic_num")
args = parser.parse_args()

src_path = "/media/kuba-ubuntu/UUI/img_mgr_3/sign_to_prepare"
dst_path = "/media/kuba-ubuntu/UUI/img_mgr_3/nosing"


def copy_only(source_path, destiny_path):
    path_direction = os.listdir(source_path)
    for direction in path_direction:
        print(direction)
        folder_direction = os.path.join(source_path, direction)
        print(folder_direction)
        for image in os.listdir(folder_direction):
            extension = image.split('.')[1]
            if extension == 'jpg':
                src_tr = os.path.join(folder_direction, image)
                print(src_tr)
                dst_tr = os.path.join(destiny_path, image)
                shutil.copyfile(src_tr, dst_tr)
            else:
                pass
    print("Copied completely!")


def copy_and_resize(source_path, destiny_path, new_height, new_width, number_of_picture=int(args.pic_num)):
    path_direction = os.listdir(source_path)
    pictures_in_src_directory = len(path_direction)
    print(pictures_in_src_directory)
    if number_of_picture is None:
        number_of_picture = pictures_in_src_directory
    else:
        pass
    i = 0
    drawn_numbers_list = []
    while i < number_of_picture:
        random_number = random.randrange(0, pictures_in_src_directory, 1)
        if random_number in drawn_numbers_list:
            continue
        else:
            drawn_numbers_list.append(random_number)
            i += 1
        image = path_direction[random_number]
        extension = image.split('.')[1]
        if extension == 'jpg':
            img = cv2.imread(os.path.join(source_path, image))
            height_img, width_img, _ = img.shape
            # Picture resizing
            img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
            cv2.imwrite(os.path.join(destiny_path, image), img)
            print(f"{i} / {number_of_picture}")
        else:
            pass
    print("Copied and resized completely!")


if args.copy:
    copy_only(src_path, dst_path)
elif args.resize:
    copy_and_resize(src_path, dst_path, 600, 800)
else:
    print("Choose some flag")
    exit()

