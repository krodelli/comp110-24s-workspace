from lessons.quiz3prac import remove_first_even , find_even

def test_remove_first_even_use_case() -> None:
    words: list[str] = ["Kate", "Dog"]
    remove_first_even(words)
    assert words == ["Dog"]

def test_find_even_use() -> None:
    list_test: list[str] = ["Hello", "Kate" , "Hi"]
    assert find_even(list_test) == "Kate"

