# SPERF Assignment II

## CONTENTS

<!-- TOC -->

- [SPERF Assignment II](#sperf-assignment-ii)
    - [CONTENTS](#contents)
    - [REQUIREMENTS](#requirements)
    - [CONFIGURE](#configure)
    - [RUN SIMULATOR](#run-simulator)
    - [RUN MODEL](#run-model)
    - [RUN ANALYSIS](#run-analysis)

<!-- /TOC -->

## REQUIREMENTS

- Python 3
- Pip
- Rscript

## CONFIGURE

- `pip install -r requirements.txt`

## RUN SIMULATOR

- `python run.py`

## RUN MODEL

- `python model/model.py`

## RUN ANALYSIS

- `Rscript analyse/analyse.r`

If `dev.copy2pdf` throws an error, comment out all occurrences of that function in the `main` section of `analyse/analyse.r`.

The script assumes the working directory (set via `setwd()`) is the one that contains this readme.
