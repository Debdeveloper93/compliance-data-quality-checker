import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd

from src.quality_checker import generate_quality_report


def test_report_creation():

    df = pd.DataFrame({
        "issue_id": [1, 1, 2],
        "country": ["India", "India", "UK"],
        "status": ["Open", "Open", "Closed"],
        "owner": ["John", "John", "Mary"]
    })

    report = generate_quality_report(df)

    assert len(report) > 0