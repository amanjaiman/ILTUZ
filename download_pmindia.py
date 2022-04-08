import os
import wget

os.chdir("./data")
os.mkdir("pmindia")
os.chdir("./pmindia")

langs = ["as", "bn", "gu", "hi", "kn", "ml", "mni", "mr", "or", "pa", "ta", "te", "ur"]

for lang in langs:
    url = "https://data.statmt.org/pmindia/v1/parallel/pmindia.v1."+lang+"-en.tsv"
    wget.download(url)
  
files = os.listdir('.')
for file in files:
    s = file.split(".")
    os.rename(file, '.'.join([s[2], s[3]]))