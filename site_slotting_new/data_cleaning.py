import pandas as pd


def preprocess_df(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    relevant_features = [
        "Email Address",
        "Name",
        "Castlemont",
        "Montera",
        "DeJean",
        "DCA",
        "Rudsdale",
        "Longfellow",
        "SquashDrive",
        "John Henry",
        "Life Academy",
        "CC Member",
        "Exec",
        "Spanish Speaker",
        "Can Drive",
        "Has Car",
        "Gender",
        "Site Leader",
    ]
    # Select columns that contain a feature
    relevant_columns = [
        col
        for col in df.columns
        if any(feature in col for feature in relevant_features)
    ]

    # Create a new DataFrame with only the relevant columns
    pre_processed_df = df[relevant_columns]

    return pre_processed_df
