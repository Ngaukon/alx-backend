#!/usr/bin/env python3
"""Pagination helper function for calculating index ranges.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end index for items on a specific page.
    
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    
    Returns:
        Tuple[int, int]: A tuple containing the start and end indices 
                         for the items on the specified page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
