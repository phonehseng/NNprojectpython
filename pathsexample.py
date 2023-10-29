import os
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)

pageobjectspath = os.path.join(dir_path, "pageobjects")
print(pageobjectspath)

resourcepath = os.path.join(dir_path, "resources")
print(resourcepath)