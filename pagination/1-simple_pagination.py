#!/usr/bin/env python3
"""
Simple pagination module.
"""

import csv
from typing import List, Optional
from 0-simple_helper_function import index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Load dataset once and cache it."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)
            self.__dataset = data[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Returns the requested page of the dataset.
        Uses index_range for pagination.

        Args:
            page (int): Page number, 1-indexed.
            page_size (int): Number of items per page.

        Returns:
            List of rows of the dataset for that page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]
