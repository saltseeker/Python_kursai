import os
from datetime import datetime
import time




desktop = os.path.join(os.environ['USERPROFILE'], "Desktop")
print(desktop)



folder = "naujas katalogas"
folder_path = os.path.join(desktop, folder)


if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = datetime.now().strftime("%Y-%m-%d %I_%M_%S")
filepath = os.path.join(folder_path, filename)
con_to_txt = filepath + ".txt"


with open(con_to_txt, "w") as file:
    file.write("")


file_info = os.stat(con_to_txt).st_ctime
ctime = file_info.st_ctime

print(file_info.st_size)

time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ctime))

print(time_str) 
