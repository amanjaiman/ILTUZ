import os
import pandas as pd
import sys

os.chdir("./data/pmindia")

def create_datasets(args):
    lang1, lang2, train_N, test_N = args
    languages = [lang1, lang2]
    
    path = "../"+'_'.join(languages)
    
    lang_dfs = {}
    for lang in languages:
        df = pd.read_csv(lang+"-en.tsv", sep="\t", header=None)
        df = df.set_index(0)
        df.columns = [lang]

        lang_dfs[lang] = df
        
    joint_df = lang_dfs[languages[0]].join(lang_dfs[languages[1]], on=0).dropna().sample(test_N, random_state=1)
    
    # test data, lang1 <-> lang2
    l1, l2 = joint_df.columns
    l1data = joint_df[l1].tolist()
    l2data = joint_df[l2].tolist()

    with open(path+"test/data."+l1+"2"+l2, 'w+') as f:
        f.write('\n'.join(l1data))

    with open(path+"test/data."+l2+"2"+l1, 'w+') as f:
        f.write('\n'.join(l2data))
    
    # train and test data, eng <-> lang
    for lang in languages:
        df = pd.read_csv(lang+"-en.tsv", sep='\t', header=None)
        df = df.sample(train_N+test_N, random_state=1)
        df_dict = {"train": df.iloc[:train_N, :], "test": df.iloc[train_N:, :]}
        
        for k in df_dict.keys():
            en = df_dict[k][0].tolist()
            ind = df_dict[k][1].tolist()

            with open(path+str(k)+"/data.en2"+lang, "w+") as f:
                f.write('\n'.join(en))
            
            with open(path+str(k)+"/data."+lang+"2en", "w+") as f:
                f.write('\n'.join(ind))
                
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: create_datasets.py <lang1> <lang2> <train_N> <test_N>")
        sys.exit(1)
    
    create_datasets(sys.argv[1:])