import pandas as pd

from src.quality_checker import (
    generate_quality_report,
    get_duplicate_records,
    get_missing_owner_records
)

# Read input file
df = pd.read_excel(
    "data/sample_issues.xlsx"
)

# Generate summary report
report = generate_quality_report(df)

# Generate exception reports
duplicate_records = get_duplicate_records(df)

missing_owner_records = get_missing_owner_records(df)

# Save summary report
with pd.ExcelWriter(
    "reports/compliance_report.xlsx"
) as writer:

    report.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    duplicate_records.to_excel(
        writer,
        sheet_name="Duplicates",
        index=False
    )

    missing_owner_records.to_excel(
        writer,
        sheet_name="Missing Owners",
        index=False
    )
    
# Save duplicate records
duplicate_records.to_excel(
    "reports/duplicate_records.xlsx",
    index=False
)

# Save missing owner records
missing_owner_records.to_excel(
    "reports/missing_owner_records.xlsx",
    index=False
)

print("\nReports generated successfully!\n")

print(report)