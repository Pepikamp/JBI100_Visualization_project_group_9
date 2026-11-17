def intersect_selections(*record_id_sets):
    """Combine active selections with AND semantics.

    No arguments means no active filters. An explicitly empty selection means
    that no records match that filter.
    """
    if not record_id_sets:
        return set()
    iterator = iter(record_id_sets)
    result = set(next(iterator))
    for selection in iterator:
        result.intersection_update(selection)
    return result
