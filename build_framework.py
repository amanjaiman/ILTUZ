import os

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

def generate_training_script(lang1, lang2):
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

# TODO: make callable from cmd with args