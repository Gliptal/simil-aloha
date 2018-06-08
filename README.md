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
    - [KNOWN ISSUES](#known-issues)

<!-- /TOC -->

## REQUIREMENTS

- Python 3 (as `python3`)
- Pip (as `pip3`)
- Rscript

## CONFIGURE

`make configure`

- `pip3 install -r requirements.txt`

## RUN SIMULATOR

`make simulate`

- `python3 run.py`

## RUN MODEL

`make model`

- `python3 model/model.py`

## RUN ANALYSIS

`make analyse`

- `Rscript analyse/analyse.r`

## KNOWN ISSUES

- Rscript assumes the working directory (set via `setwd()`) is the one that contains this readme.

- If using RStudio, uncomment all `dev.copy2pdf()` occurrences to generate `.pdf` versions of the graphs in `.\graphs`.
