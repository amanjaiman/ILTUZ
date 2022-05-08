# ILTUZ
 
 ## Description
 Todo
 
 Currently broken for local work, refer to the [Google Colab notebook](https://colab.research.google.com/drive/13Htu7-8Bz0hLnkiJ3givQfTJCgpi5RCk?usp=sharing) for usage.

 ## Usage
 1. Download the PMIndia Dataset
 
    `
    python download_pmindia.py all
    `

    *Note: In case this doesn't work because the statmt website is down, I have also made the data available here: [drive link to zip]*
    *Download to ./data/pmindia then run `unzip pmindia.zip`*
    
 2. Generate necessary directories and files for your language pair
 
    `
    python build_framework.py hi mni
    `
 3. Create datasets for your language pair
  
    `
    python create_datasets.py hi mni 5000 1000
    `
 
 4. Go into the new directory that was created
   
    `
    cd data/hi_mni
    `

 5. Train the model
  
    `
    ./train.sh
    `
 6. Evaluate the zero-shot performance on your language pair
 
    `
    ./translate.sh
    `
