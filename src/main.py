#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd

# ~~~   DEFINES ~~~

FDA_CERTIFIED_PATH = "dataset/beginner.csv"
CENSUS_DATA_PATH =  "dataset/sc-est2019-agesex-civ.csv"

# ~~~   SETUP   ~~~

def init():
    """ Intitialization setup for the program"""

    global FDA_CERTIFIED_PATH 
    global CENSUS_DATA_PATH

    # Find the path to dataset and normalize for POSIX or Windows
    script_dir = os.getcwd()
    FDA_CERTIFIED_PATH = os.path.normcase(os.path.normcase(os.path.join(script_dir, FDA_CERTIFIED_PATH)))
    CENSUS_DATA_PATH = os.path.normcase(os.path.normcase(os.path.join(script_dir, CENSUS_DATA_PATH)))


# ~~~   DATA   ~~~

def csv_to_dataframe(filepath: str) -> pd.DataFrame:
    """ Cleaner helper method"""
    return pd.read_csv(filepath)

# ~~~ MAIN PROGRAM ~~~

def main():
    """ Main program """

    # Do the setup work first
    init()

    fda_certified_df = csv_to_dataframe(FDA_CERTIFIED_PATH)
    census_df = csv_to_dataframe(CENSUS_DATA_PATH)

    print(fda_certified_df)
    print(census_df)

    return 0

if __name__ == "__main__":
    main()