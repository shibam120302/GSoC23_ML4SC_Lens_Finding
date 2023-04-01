import pandas as pd
import os

data = pd.read_csv("classifications.csv")

fnames = os.listdir("image")
fnames.sort()

for i in range(0,len(data["ID"])):
    if data["is_lens"][i] == 0:
        id = str(data["ID"][i])
        os.replace("image/imageEUC_VIS-"+id+".fits.jpg","no_ring/imageEUC_VIS-"+id+".jpg")

