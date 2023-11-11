import numpy as np
import pandas as pd
from random import randint
from random import random


def randomized_matching(
    site_preferences: pd.DataFrame,
    df_site_leader_col_index: int,
    df_site_col_indices: tuple,
    num_pairings: int = 1,
    num_iterations: int = 10000,
) -> list:
    """
    Implements a randomized matching algorithm for pairing items based on preferences.
    This function takes in member preferences, a dictionary specifying the preferences of
    items. The function then generates pairings between items randomly and evaluates
    their scores based on preferences. The pairings are sorted by score, and the top pairings
    are returned.

    Args:
        site_preferences (pd.DataFrame): A DataFrame representing member preferences where
            rows represent items and columns represent their preferences.
        df_site_leader_col_index (int): The index of the column which tells us whether a member
            is a site leader or not.
        num_pairings (int, optional): The number of pairings to generate. Defaults to 1.
        num_iterations (int, optional): The number of iterations for generating pairings.
            Defaults to 1000.

    Returns:
        list: A list of tuples containing dictionaries representing pairings and their corresponding
            scores. Each tuple consists of a pairing dictionary and its score. The list is sorted by
            score, and the top pairings are returned.
    """

    pairing_list = []  # [(pairing dict, score), ..]
    choices = site_preferences.columns[df_site_col_indices[0] : df_site_col_indices[1]]
    for _ in range(num_iterations):
        pass
    return


def score() -> int:
    return
