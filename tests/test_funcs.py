from efa import EFADay, funcs


def test_get_efa_days():
    start_time = "2024-03-01 07:00:00+00:00"
    end_time = "2024-03-06 23:30:00+00:00"
    expected = [
        EFADay("2024-03-01"),
        EFADay("2024-03-02"),
        EFADay("2024-03-03"),
        EFADay("2024-03-04"),
        EFADay("2024-03-05"),
        EFADay("2024-03-06"),
        EFADay("2024-03-07"),
    ]
    assert funcs.get_efa_days(start_time, end_time) == expected


def test_get_efa_dates_single_day():
    efa_date = EFADay("2024-03-01")
    expected = [efa_date]
    assert funcs.get_efa_days(efa_date.start_time, efa_date.end_time) == expected
