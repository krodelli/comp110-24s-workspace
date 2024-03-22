"""Some functions for my garden plan!"""

__author__ = "730466512"


def add_by_kind(by_kind: dict[str, list[str]], kind: str, plant: str) -> None:
    """Mutates input dictionary to sort plants by kind."""
    if kind in by_kind: 
        by_kind[kind].append(plant)
    else:
        by_kind[kind] = [plant]


def add_by_date(by_date: dict[str, list[str]], date: str, plant: str) -> None:
    """Sorts by date."""
    if date in by_date:
        by_date[date].append(plant)
    else:
        by_date[date] = [plant]


def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], kind: str, date: str) -> str:
    """Searches through both dictionaries and returns list."""
    plants_list: list[str] = []
    if kind in by_kind and date in by_date:
        for plant in by_kind[kind]:
            if plant in by_date[date]:
                plants_list.append(plant)
        if plants_list:
            return f"{kind}s to plant in {date}: {plants_list}"
        else: 
            return f"No {kind}s to plant in {date}."
    else:
        return "Invalid kind or date."