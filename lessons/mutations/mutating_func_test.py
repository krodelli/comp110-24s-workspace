from lessons.mutations.mutating_func import remove_first, get_and_remove_first, get_first

def test_remove_first_use_case() -> None:
    """Test basic use."""
    t: list[str] = ["cloud", "rain", "sun"]
    remove_first(t)
    assert t == ["rain", "sun"]
    

def test_get_first_use() -> None:
    t: list[str] = ["cloud", "rain", "sun"]
    ret_value: str = get_first(t)
    get_first(t)
    assert t == ["cloud", "rain", "sun"] # test does not mutate input
    assert ret_value == "cloud" # test return value is correct 


def test_get_and_return_first_use() -> None:
    t: list[str] = ["cloud", "rain", "sun"]
    ret_value: str = get_and_remove_first(t)
    assert ret_value == "cloudy"
    assert t == ["rain", "sun"]