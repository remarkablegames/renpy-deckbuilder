init python:
    def find(collection: list, predicate: dict):
        """
        Iterate over elements of collection, returning the first element predicate returns truthy for.
        """
        key = next(iter(predicate))
        value = next(iter(predicate.values()))
        return next((item for item in collection if getattr(item, key) == value), None)
