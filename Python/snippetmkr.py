import os

with open ("file") as i:
    with open ("temp", "w") as o:
        for l in i:
            o.write("\"%s\",\n" % l[:-1])
        
os.remove("file")
os.rename("temp", "file")