import pytest
import pandas as pd

from site_slotting_new import algorithm
from site_slotting_new import data_cleaning


def test_preprocess_df1():
    file = "data/anonymized_spring24_sites_data.csv"
    cleaned_data = data_cleaning.preprocess_df(file)
    print(cleaned_data.columns)
    assert cleaned_data.shape[1] <= 18


def test_preprocess_df2():
    file = "data/anonymized_spring24_sites_data.csv"
    cleaned_data = data_cleaning.preprocess_df(file)
    assert cleaned_data.shape[1] == 18
