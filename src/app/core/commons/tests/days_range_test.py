from core.commons.days_ranges import DaysRange


def describe_days_range_common():
    def it_should_return_value():
        days_range_value = DaysRange().get_value()

        assert days_range_value == [
            ("7 days", "7 dias"),
            ("30 days", "30 dias"),
            ("90 days", "90 dias"),
        ]
