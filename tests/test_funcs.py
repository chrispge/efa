from efa import EFADay, funcs


def test_get_efa_days():
    start_time = "2024-03-01 07:00:00+00:00"
    end_time = "2024-03-06 23:30:00+00:00"
    result = funcs.get_efa_days(start_time, end_time)
    assert result == [
        EFADay("2024-03-01"),
        EFADay("2024-03-02"),
        EFADay("2024-03-03"),
        EFADay("2024-03-04"),
        EFADay("2024-03-05"),
        EFADay("2024-03-06"),
        EFADay("2024-03-07"),
    ]
