#!/usr/bin/env python3
"""hypermedia pagination module"""
import csv
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
        """
        end_index = page_size * page
        start_index = end_index - page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the list of limited elements"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        s_index, e_index = self.index_range(page, page_size)
        data_set = self.dataset()
        return data_set[s_index:e_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Method with same args as get_page
        Returns a dictionary containing multiple key, values
        """
        dataset = self.get_page(page, page_size)
        tot_rows = len(self.dataset())
        end_range = self.index_range(page, page_size)[1]
        next_p = None if end_range >= tot_rows else page + 1
        prev_page = None if page - 1 == 0 else page - 1
        nr_pages = tot_rows / page_size
        if nr_pages % 1 != 0:
            nr_pages += 1
        new_dict = {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": next_p,
            "prev_page": prev_page,
            "total_pages": int(nr_pages),
        }
        return new_dict
