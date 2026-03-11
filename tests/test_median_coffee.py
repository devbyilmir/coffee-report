from reports.median_coffee import MedianCoffeeReport


def test_median_coffee_report():
    rows = [
        {"student": "ваня", "coffee_spent": "100"},
        {"student": "ваня", "coffee_spent": "200"},
        {"student": "кира", "coffee_spent": "300"},
        {"student": "кира", "coffee_spent": "500"},
    ]

    report = MedianCoffeeReport()
    result = report.build(rows)

    assert ("кира", 400) in result
    assert ("ваня", 150) in result


def test_report_sorted_desc():
    rows = [
        {"student": "a", "coffee_spent": "100"},
        {"student": "a", "coffee_spent": "200"},
        {"student": "b", "coffee_spent": "500"},
        {"student": "b", "coffee_spent": "600"},
    ]

    report = MedianCoffeeReport()
    result = report.build(rows)

    assert result[0][0] == "b"
