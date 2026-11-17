from src.visualization_project.interactions.selection import intersect_selections


def test_no_active_filters():
    assert intersect_selections() == set()


def test_selections_intersect():
    assert intersect_selections({"a", "b"}, {"b", "c"}) == {"b"}


def test_empty_selection_matches_nothing():
    assert intersect_selections({"a", "b"}, set()) == set()
