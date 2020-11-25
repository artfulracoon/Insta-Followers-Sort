import os
import time
import webbrowser


def alphanumerical_sort(name):
    text = open(name, "r", encoding="utf8")
    lines = sorted(text.readlines())
    text.close()
    sorteded = open(name, "w", encoding="utf8")
    for word in lines:
        sorteded.write(word)
    sorteded.close()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def data_to_text(name):
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break

        contents.append(line)
    file = open(name, "w", encoding="utf8")
    for i in contents:
        file.write(i)
        file.write("\n")
    file.close()


path = os.getcwd()

if os.name == 'nt':
    path = path + r"\InstaSort"
else:
    path += r"/InstaSort"

try:
    os.mkdir(path)
except FileExistsError:
    print("InstaSort folder on " + path + " exists. Continuing.\n")
folder_path = path
if os.name == 'nt':
    path = path + r"\sorted"
else:
    path += r"/sorted"
try:
    os.mkdir(path)
except FileExistsError:
    print("Sorted folder in InstaSort exists. Continuing.\n")
folder_path_sorted = path

os.chdir(folder_path)

print("\nPlease enter ACCOUNTS FOLLOWING YOU data here: \n\nhttps://www.instagram.com/accounts/access_tool/accounts_following_you \n\nPRESS ENTER TWO TIMES AFTER PASTING CONTENTS! \n\nOpening in browser...")
time.sleep(1.5)
webbrowser.open(
    'https://www.instagram.com/accounts/access_tool/accounts_following_you', new=1, autoraise=True)
data_to_text("followers.txt")
clear()
print("Input successful. Generating input for ACCOUNTS YOU FOLLOW.\n")
time.sleep(1.5)
print("\nPlease enter ACCOUNTS YOU FOLLOW data here: \n\nhttps://www.instagram.com/accounts/access_tool/accounts_you_follow \n\nPRESS ENTER TWO TIMES AFTER PASTING CONTENTS! \n\nOpening in browser...")
time.sleep(1.5)
webbrowser.open(
    'https://www.instagram.com/accounts/access_tool/accounts_you_follow', new=1, autoraise=True)
data_to_text("following.txt")
clear()
print("Input successful. Continuing...\n")
time.sleep(1.5)

alphanumerical_sort(r"followers.txt")
alphanumerical_sort(r"following.txt")
print("Sorted alpahnumeritically. Rewrote files.\n")

followers = open(
    r"followers.txt", "r", encoding="utf8")
following = open(
    r"following.txt", "r", encoding="utf8")

followers_sorted = open(
    r"sorted.txt", "w", encoding="utf8")

for line_following in following:
    followers.seek(0)
    for line_followers in followers:
        if line_following == line_followers:
            break
    else:
        followers_sorted.write(line_following)

followers_sorted.close()

if not os.path.exists(folder_path_sorted):
    os.mkdir(folder_path_sorted)

if os.name == 'nt':
    path_to_move = folder_path_sorted + r"\sorted.txt"
else:
    path_to_move = folder_path_sorted + r"/sorted.txt"


try:
    os.rename("sorted.txt", path_to_move)
except FileExistsError:
    os.chdir(folder_path_sorted)
    os.remove("sorted.txt")
    os.chdir(folder_path)
    os.rename("sorted.txt", path_to_move)

input("Finished successfully.\n\nYou can find the output folder here:\n\n" + str(folder_path) +
      "\n\nInside the InstaSort folder, you can find the following and followers lists and a folder named sorted.\n\n"
      "Check the sorted folder to find a list of who does not follow you back.\n\n"
      "YOU CAN NOW CLOSE THIS WINDOW.")
