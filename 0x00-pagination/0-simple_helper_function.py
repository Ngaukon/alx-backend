#!/usr/bin/env python3
"""Pagination for helper functions
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index ranges from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
