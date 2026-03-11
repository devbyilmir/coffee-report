import argparse
import sys

from tabulate import tabulate

from reports import REPORTS
from services.csv_reader import read_files


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="CSV files with exam preparation data",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    report_class = REPORTS.get(args.report)

    if report_class is None:
        print(f"Unknown report: {args.report}")
        sys.exit(1)

    try:
        rows = read_files(args.files)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    report = report_class()

    data = report.build(rows)

    print(
        tabulate(
            data,
            headers=["student", "median_coffee"],
            tablefmt="github",
        )
    )


if __name__ == "__main__":
    main()
