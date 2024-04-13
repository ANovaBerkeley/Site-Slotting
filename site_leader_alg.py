# each person has their own rankings of the sites (some NaN)

# maybe we can distribute drivers, site leaders, cc members, and spanish speakers first?'
# then we can assign others

import pandas as pd
import ast
import re

class Site:
    def __init__(self, name, is_spanish_speaking):
        self.name = name
        self.is_spanish_speaking = is_spanish_speaking
        
        self.people = []
        self.num_spanish_speaking_people = 0
        self.has_site_leader = False
        self.has_driver = False
        self.has_CC = False

df = pd.read_csv("data/anonymized_data_features.csv")

# convert "1st" to int 1, "2nd" to int 2, etc.
def convert_str_to_int(value):
    if isinstance(value, str):
        return int(value[:-2])
    return value

site_choices = df.columns.tolist()[3:18]
for col in site_choices:
    df[col] = df[col].apply(convert_str_to_int)

# create sites
sites = []
site_name_to_site = {}
school_name_to_sites = {} # {"DCA": [Site object, Site object]}
site_names = df.columns.tolist()[3:18]
pattern = r'\[(.*)\]'
for site_name in site_names:
    is_spanish_speaking = "Spanish" in site_name
    site = Site(site_name, is_spanish_speaking)
    sites.append(site)
    site_name_to_site[site_name] = site
    school_name = re.findall(pattern, site_name)[0]
    if school_name not in school_name_to_sites:
        school_name_to_sites[school_name] = []
    school_name_to_sites[school_name].append(site)

# assign all site leaders to their sites
# assume that site leaders must be matched to the site/s indicated in the "Site Leader" column
site_leaders = df[df["Site Leader"].map(lambda x: x != "False")]
def assign_site_leaders(row):
    """
    Assign site leaders to their site indicated in the column "Site Leader"
    """
    name = row["Name"]
    is_CC = row["CC"]
    is_driver = row["Driver"]
    is_spanish_speaking = row["Spanish Speaking"]
    site_names = ast.literal_eval(row["Site Leader"])

    for site_name in site_names:
        site = site_name_to_site[site_name]
        site.has_site_leader = True
        site.people.append(name)

        # update site attributes
        if is_CC:
            site.has_CC = True
            
        if is_driver:
            site.has_driver = True

        if is_spanish_speaking:
            site.num_spanish_speaking_people += 1

df.apply(assign_site_leaders, axis=1)
        

drivers = df[df["Driver"]]

def assign(row):
    """
    Greedy algorithm approach. 
    
    Try assigning people to their first choice.
    If the site is full (already 5 people) provide their second choice.

    CC members matched to one site fulfill the CC requirement of another site with the same school.
    
    """
    name = row["Name"]
    is_site_leader = row["Site Leader"]
    is_CC = row["CC"]
    is_driver = row["Driver"]

    # get the site preferences of a person
    site_choices = row.values.tolist()[3:18]

    # map column indices to site names
    i_to_site_name = {}
    for i, site in enumerate(site_choices):
        i_to_site_name[i+3] = site

    # get column indices and preferences of chosen sites for a person
    # example: [(3,1)] <- the site with the 3rd column index is the 1st choice for a person 
    indices_of_chosen_sites = []
    for i, preference in enumerate(site_choices):
        if isinstance(site, int):
            indices_of_chosen_sites.append((i+3, preference))

    # sort indices_of_chosen_sites by the lowest preferences
    sorted_indices_of_chosen_sites = sorted(indices_of_chosen_sites, lambda x: x[1])

    # iterate over column indices of preferred sites, starting from 1st choice
    matched = False
    for i,j in sorted_indices_of_chosen_sites:
        site_name = i_to_site_name[i]
        site = site_name_to_site[site_name] # get Site object of that site

        # check if the site is full
        # site is full
        if len(site.people) == 5:
            # go to next preferred option
            continue
        else:
            # site is not full

            # check site priorities
            if site.has_site_leader and is_site_leader:
                # go to another site that doesn't already have a site leader
                continue

            if site.has_CC and is_CC:
                # go to another site that doesn't already have a site leader

                continue

            # update site attributes
            if is_site_leader:
                site.has_site_leader = True
            
            if is_CC:
                site.has_CC = True

                # satisfy the CC requirement of the other site of the same school as well
                pattern = r'\[(.*)\]'
                school_name = re.findall(pattern, site_name)[0]
                sites_of_same_school = school_name_to_sites[school_name]

                for s in sites_of_same_school:
                    s.has_site_leader = True
            
            if is_driver:
                site.has_driver = True

            # add person to site
            site.people.append(name)
            
            matched = True
    
    # check that a person was matched
    # if a person was not matched, I would recommend ens
    assert matched, "A person wasn't matched to any of their choices"
        
        
            


    pass


def confirm_sites():
    """
    Confirm that all sites have at least one CC, one driver, one Site Leader, not overfilled etc.
    """
    pass
