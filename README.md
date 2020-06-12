# ecDNA-Analytics

Web platform that integrates the metaDetect and ecSeg  tools with respective visualizations for the purpose of extrachromosomal DNA analysis.

## Tools

### metaDetect

(<https://github.com/MihirBafna/MetaDetect>)
metaDetect is a platform for identifying metaphase spreads in a population of cells from whole slide images (experimental)

### ecSeg

(<https://github.com/UCRajkumar/ecSeg>)
ecSeg is a platform designed to identify extrachromosomal DNA (ecDNA) from metaphase images stained with DAPI and FISH probes (Rajkumar, U. iScience 2019)

## Installation

NOTE THAT THIS APP IS IN DEVELOPMENTAL STAGE

1. Clone this repository into a local folder of your choice

2. Navigate into repository and set up a virtual environment (conda is recommended)
    * Using conda:
    ```bash
    conda env create -f environment.yml
    source activate env 
    ```
    * Using pip:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Recursively install all dependencies into your virtual environment (requirements.txt is provided)
    * Using Conda:  
        <sub>Skip this step</sub>
    
    * Using pip:
    ```bash
     pip install -r requirements.txt
     ```

       
4. Setup flask developmental server

    ```bash
    export FLASK_ENV=run.py
    export FLASK_APP=development
    ```

## Usage

Whenever starting up the server, do the following:

1. Activate your virtual environment
    * Using Conda:  
   ```bash
   source activate env 
   ```
    * Using pip:
    ```bash
    source env/bin/activate
    ```

2. Run application

    ```bash
    flask run
    ```

3. Developmental server will be running on ```localhost:5000``` in your web browser

4. Once done using application, deactivate your virtual environment with either ```deactivate``` or ```conda deactivate```

