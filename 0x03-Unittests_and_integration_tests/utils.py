#!/usr/bin/env python3
"""
Utility functions for working with nested mappings.
"""

from typing import Mapping, Any, Tuple


def access_nested_map(nested_map: Mapping, path: Tuple) -> Any:
    """
    Access a nested map using a sequence of keys.

    Args:
        nested_map (Mapping): A nested dictionary-like object.
        path (Tuple): A sequence of keys representing the path to traverse.

    Returns:
        Any: The value found at the specified path.

    Raises:
        KeyError: If a key in the path does not exist in the map.
    """
    current = nested_map
    for key in path:
        current = current[key]
    return current
