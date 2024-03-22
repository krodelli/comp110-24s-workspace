from lessons.quiz3prac import remove_first_even

def test_remove_first_even_use_case() -> None:
    words: list[str] = ["Kate", "Dog"]
    remove_first_even(words)
    assert words == ["Dog"]

