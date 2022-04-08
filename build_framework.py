import os
import sys

def create_directories(lang1, lang2):
    os.chdir("./data")
    
    folder = '_'.join([lang1, lang2])
    os.mkdir(folder)
    os.chdir(folder)
    
    os.mkdir("bpe")
    os.mkdir("out")
    os.mkdir("test")
    os.mkdir("train")

def generate_yaml(lang1, lang2):
    # still in language folder
    with open("../../zsnmt.yaml.template", "r") as f:
        with open("zsnmt.yaml", "w+") as fw:
           data = f.read()
           data = data.replace("%SRC%", lang1)
           data = data.replace("%TGT%", lang2)
           data = data.replace("mnmt_template", "mnmt_zs")
           fw.write(data)

def generate_training_script():
    with open("../../train.sh.template", "r") as f:
        with open("train.sh", "w+") as fw:
           data = f.read()
           fw.write(data)
    
def generate_translate_script(lang1, lang2):
    # still in language folder
    with open("../../translate.sh.template", "r") as f:
        with open("translate.sh", "w+") as fw:
           data = f.read()
           data = data.replace("src2tgt", lang1+"2"+lang2)
           data = data.replace("tgt2src", lang2+"2"+lang1)
           fw.write(data)
           
def main(lang1, lang2):
    create_directories(lang1, lang2)
    generate_yaml(lang1, lang2)
    generate_training_script()
    generate_translate_script(lang1, lang2)
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: build_framework.py <lang1> <lang2>")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])

# TODO: make callable from cmd with args