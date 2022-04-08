# ILTUZ
 
 ## Description
 Todo

 ## Usage
 1. Download the PMIndia Dataset
 
    `
    python download_pmindia.py all
    `
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