import pandas as pd


def generate_quality_report(df):

    total_rows = len(df)

    duplicate_issue_ids = df["issue_id"].duplicated().sum()

    missing_issue_ids = df["issue_id"].isna().sum()

    missing_country = df["country"].isna().sum()

    missing_owner = df["owner"].isna().sum()

    open_count = (df["status"] == "Open").sum()

    closed_count = (df["status"] == "Closed").sum()

    report = {
        "Metric": [
            "Total Rows",
            "Duplicate Issue IDs",
            "Missing Issue IDs",
            "Missing Countries",
            "Missing Owners",
            "Open Issues",
            "Closed Issues"
        ],
        "Value": [
            total_rows,
            duplicate_issue_ids,
            missing_issue_ids,
            missing_country,
            missing_owner,
            open_count,
            closed_count
        ]
    }

    return pd.DataFrame(report)


def get_duplicate_records(df):
    return df[df["issue_id"].duplicated(keep=False)]


def get_missing_owner_records(df):
    return df[df["owner"].isna()]