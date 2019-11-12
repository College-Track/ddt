Development Data Tool
==============================

A collection of scripts to automate the generation and updating of the Development Data Tool.

### Prerequisites

```
python 3.7
conda 4.7.12
```


### Installing
Clone the repository and switch to the created ddt directory
```
git clone https://github.com/College-Track/ddt
cd ddt
```

* For any time after initial install just run the second command
```
conda env create -f environment.yml
conda activate ddt
```

Copy the example .env file
```
cp .env.example .env
```

Make sure you update the following values in the newly created .env
```
SF_TOKEN=<your salesforce token>
SF_USERNAME=<your salesforce username>
SF_PASS=<your salesforce password>
```

### Run scripts

``` 
python3 src/main.py
```


### Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download, generate, or clean data
    │   │   └── load_data.py <- functions to load data from Salesforce
    |   |   |
    |   |   └── prep_data.py <- function to clean/prep data 
    |   |
    │   │
    │   ├── helpers       <- Scripts to turn raw data into features for modeling
    │   │   └── helpers.py
    │   │
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
