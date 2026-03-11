from collections import defaultdict
from statistics import median

from reports.base import BaseReport


class MedianCoffeeReport(BaseReport):

    def build(self, rows: list[dict]) -> list[tuple]:
        students: dict[str, list[int]] = defaultdict(list)

        for row in rows:
            student = row["student"]
            coffee = int(row["coffee_spent"])

            students[student].append(coffee)

        result = []

        for student, values in students.items():
            result.append((student, int(median(values))))

        result.sort(key=lambda x: x[1], reverse=True)

        return result