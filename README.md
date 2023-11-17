# Site Slotting

This code is meant to do two things:

1. Put old members into sites given a .csv file of their preferences.
2. Place new members into sites given a .csv file of their preferences, taking into account old members already being placed at a site a couple of weeks ago.

## Old Members

Given `N` old members, each of the `N` members will rank their top 5 sites. Our input should be a `.csv` file of this data, in which the form should have columns `NAME`, `SITE #1`, ..., `SITE #i`, and rows `PERSON 1`, ..., `PERSON N`.

### Example

NOTE: Our data is not JSON, this is just an easy way to see the structure of data.

```json
row = {'Jacob Aldrich':
    {'Site #1': None},
    {'Site #2': 1},
    {'Site #3': 3},
    ...
    {'Site #i': 2}
}
```

## New Members

Given `M` new members, each of the `M` members will rank their top 5 sites. Our input should be a `.csv` file of this data, in which the form should have the same format as old members.

## TO RUN

To run the code, type this in your terminal:

```bash
python -m venv venv
scource venv/bin/activate
pip install -r requirements.txt
```

then proceed to run the notebook.ipynb or algorithm.py on your own data sets. Some data cleaning may be necessary.

TODO:

1. Create Google Form with site slotting questions
2. Look at CSV created from the form
3. Use CSV to create code to place members at sites rigorously
4. Profit??
