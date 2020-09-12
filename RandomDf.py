from datetime import datetime, timedelta
import pandas as pd
import random
import string


class RandomDataFrame(pd.DataFrame):
    """
    Insert Doc String Here. Sup Dude
    """
    def __init__(self, gen_rdf=False, nrows=10, ncols=3, col_dict=None,
        date_range=None, **kwargs):
        super().__init__(**kwargs)
        self.col_type_dict = {
            'int': self.gen_int_col,
            'str': self.gen_str_col,
            'date': self.gen_date_col,
        }
        self.default_date_range = (datetime.now().date() - timedelta(days=7), datetime.now().date())
        if not date_range:
            self.date_range = self.default_date_range

        if gen_rdf:
            self.gen_random_df(nrows, ncols, col_dict, date_range)

    def random_string(self):
        """
        Genearte a random string of characters of lenght 4.
        """
        r_string = random.choice(string.ascii_letters)
        for x in range(4):
             r_string += random.choice(string.ascii_letters)
        return r_string

    def gen_int_col(self, nrows, **kwargs):
        """
        Generate a list of length n of random integers between 1000 and 9999.
        """
        return [random.randint(1000, 9999) for x in range(nrows)]

    def gen_str_col(self, nrows, **kwargs):
        """
        Generate a list of length n of random strings using the random_string
        method.
        """
        return [self.random_string() for x in range(nrows)]

    def gen_date_col(self, nrows, date_range, **kwargs):
        """
        Genearte a list of length n of random dates with a specified range.
        """
        start, end = date_range
        n_days = (end - start).days + 1
        dates = [end - timedelta(days=x) for x in range(n_days)]
        random_dates = [random.choice(dates) for x in range(nrows)]

        return random_dates

    def gen_random_df(self, nrows=10, ncols=3, col_dict=None, date_range=None):
        """
        Generate a random DataFrame where nrows and ncols are the number of rows
        and columns desired. col_dict speficifes the column names and types. If
        col_dict is not specified, the column names will default to colx where x
        is an integet, and col types will be random.

        col_dict is a dict with column names as keys and column types as values.

        The col types available are listed in the col_type_dict.

        Each col type is assigned a generating fucntion in self.col_type_dict in
        the init.
        """

        if not date_range:
            date_range = self.default_date_range

        if not col_dict:
            col_dict = {
                f'col_{x}': random.choice(list(self.col_type_dict.keys())) for x in range(ncols)
                }

        else:
            for tpe in col_dict.values():
                if tpe not in self.col_type_dict:
                    m = f'"{tpe}" not in col_type_dict'
                    raise NotImplementedError(m)

        kwargs = {
            'nrows': nrows,
            'ncols': ncols,
            'date_range': date_range
        }
        for col_name, col_type in col_dict.items():
            self[col_name] = self.col_type_dict[col_type](**kwargs)

    def add_random_columns(self, col_dict):
        """
        Add a random column(s) to the DataFrame specified by the col_dict.
        """
        for col_name, col_type in col_dict.items():
            self[col_name] = self.col_type_dict[col_type](len(self))

    def add_foo_columns(self, num_cols=1):
        """
        Add num_cols amount of foo columns
        """

        for i in num_cols:
            self['foo_{}'.format(i)] = 'foo'

    
