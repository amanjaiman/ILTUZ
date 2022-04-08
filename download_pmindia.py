import os
import sys
import wget

def main(langs):
    os.mkdir('data')
    os.chdir("./data")
    os.mkdir("pmindia")
    os.chdir("./pmindia")

    for lang in langs:
        url = "https://data.statmt.org/pmindia/v1/parallel/pmindia.v1."+lang+"-en.tsv"
        wget.download(url)
    
    files = os.listdir('.')
    for file in files:
        s = file.split(".")
        os.rename(file, '.'.join([s[2], s[3]]))
        
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 14:
        print("Usage: download_pmindia.py all | <lang1> <lang2> ... <langN>")
        sys.exit(1)
    
    if sys.argv[1] == "all":
        langs = ["as", "bn", "gu", "hi", "kn", "ml", "mni", "mr", "or", "pa", "ta", "te", "ur"]
    else:
        langs = sys.argv[1:]
        
    main(langs)