import numpy as np
import pandas as pd
import re
from random import randint
from random import random
from tqdm import tqdm


def randomized_matching(
    site_preferences: pd.DataFrame,
    df_site_col_indices: tuple,
    num_pairings: int = 1,
    num_iterations: int = 1,
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
        num_pairings (int, optional): The number of pairings to generate. Defaults to 1.
        num_iterations (int, optional): The number of iterations for generating pairings.
            Defaults to 1000.

    Returns:
        list: A list of tuples containing dictionaries representing pairings and their corresponding
            scores. Each tuple consists of a pairing dictionary and its score. The list is sorted by
            score, and the top pairings are returned.
    """
    pairing_list = []  # [(score, pairing), ..]

    # Array of our site names
    choices = site_preferences.columns[df_site_col_indices[0] : df_site_col_indices[1]]

    # Run algorithm `num_iterations` times
    for _ in tqdm(range(num_iterations), total=num_iterations):
        pairing = [_ for i in range(len(site_preferences))]
        for i, row in site_preferences.iterrows():
            # Get member name and calculate their top 5 choices
            member, member_sites = row.loc["Name"], row[choices]
            member_top_sites = []
            for j, site in enumerate(member_sites):
                if type(site) == str:
                    place = re.search(r"\d", str(site)).group()
                    member_top_sites.append((choices[j], int(place)))
            member_top_sites = sorted(member_top_sites, key=lambda x: x[1])
            member_top_sites = [i[0] for i in member_top_sites]

            # Choose best site with 70% chance, otherwise choose random site as member pairing
            random_float = random()
            if random_float > 0.7:
                num_top_sites = len(member_top_sites) - 1
                if not num_top_sites:
                    random_int = 0
                else:
                    random_int = randint(1, num_top_sites)
                choice = member_top_sites[random_int]
            else:
                choice = member_top_sites[0]
            pairing[i] = (member, choice)

        # Score `pairing` and append to `pairing_list`
        pairing_score = score(pairing, site_preferences)
        pairing_list.append((pairing_score, pairing))

    # Sort pairing_list by scores and return `num_pairings` pairings with the lowest scores
    pairing_list = sorted(pairing_list, key=lambda x: (x[0], x[1]))
    return pairing_list[:num_pairings]


def score(pairings: list, site_preferences: list) -> int:
    """
    The scoring function for a list of pairings given a list of preferences.

    General Guidelines:
        - 5 or less people at each site
        - Equal girl/guy ratio
        - 1 CC member at each site
        - 1 Car at each site
        - Want to place each member at their most desired site

    Args:
        pairings (List): A (N, 2) list where each entry in the list is a member-site pairing.
        site_preferences (DataFrame): A DF containing each members site preferences and other
            information such as car information, gender, CC member, etc.

    Returns:
        int: The score of pairings given preferences.
    """
    return


def contains_pattern(string, pattern):
    return re.search(pattern, string) is not None


columns = [
    "Timestamp",
    "Email Address",
    "Name",
    "[DCA] Monday 3:25PM - 4:50PM",
    "[DCA] Wednesday 3:25PM - 4:50PM",
    "[Montera] Thursday 3:25PM - 5:40PM",
    "[DeJean] Monday 2:40PM - 4:20PM",
    "[DeJean] Wednesday 2:40PM - 4:20PM",
    "[King] Tuesday 3:00PM - 4:30PM",
    "[King] Thursday 3:00PM - 4:30PM",
    "[Rudsdale] Tuesday 1:35PM - 3:30PM (Spanish section)",
    "[Rudsdale] Thursday 1:35PM - 3:30PM (Spanish section)",
    "[Rudsdale] Wednesday 10:30AM - 1:00PM (Spanish section)",
    "[Longfellow] Monday 4:00PM - 5:30PM",
    "[Longfellow] Wednesday 2:00PM - 3:30PM",
    "[SquashDrive] Thursday 3:55PM - 5:35PM",
    "[John Henry] Tuesday 3:30PM - 5:30PM",
    "[John Henry] Thursday 3:30PM - 5:30PM",
]


anonymized_data = pd.read_csv("anonymized_data.csv")
anonymized_data_cleaned = anonymized_data.copy()
anonymized_data_cleaned = anonymized_data_cleaned.drop("Unnamed: 0", axis=1)
anonymized_data_cleaned = anonymized_data_cleaned.drop(
    "Please read the information above. Are you aware and do you agree with the site policies?",
    axis=1,
)
anonymized_data_cleaned = anonymized_data_cleaned.rename(
    columns={
        "Name :D": "Name",
        "Have you confirmed being a site leader with Jacob or Fernanda?": "Site Leader",
    }
)
anonymized_data_cleaned["Site Leader"] = [
    contains_pattern(str(i), r"Yes") for i in anonymized_data_cleaned["Site Leader"]
]
anonymized_data_cleaned = anonymized_data_cleaned.iloc[:, :19]
anonymized_data_cleaned = anonymized_data_cleaned[
    ~anonymized_data_cleaned["Site Leader"]
]
anonymized_data_cleaned = anonymized_data_cleaned.drop("Site Leader", axis=1)
anonymized_data_cleaned = anonymized_data_cleaned.reset_index(drop=True)

randomized_matching(anonymized_data_cleaned, [3, 17])
