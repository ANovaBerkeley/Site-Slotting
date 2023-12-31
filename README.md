# Site Slotting

This code is meant to slot old members into sites given a .csv file of their preferences. To do this, we take advantage of OpenAI's GPT models. Our results may (actually they probably will) be incorrect on the first pass, so the Sites Officer should look over and revise the output generated by this code. ALSO, this code will cost about $0.10 to run once, so keep that in mind before running multiple trials.

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

## New Members (`Not doing anymore`)

Given `M` new members, each of the `M` members will rank their top 5 sites. Our input should be a `.csv` file of this data, in which the form should have the same format as old members.

## TO RUN CODE

To run the code, type this in your terminal:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

then proceed to run `usage.ipynb` on your own `.csv` file. Some data cleaning may be necessary.
