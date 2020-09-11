import pandas as pd
import random
import string


class RandomDataFrame(pd.DataFrame):
    """
    Insert Doc String Here.
    """
    def __init__(self, gen_rdf=False, nrows=10, ncols=2, col_dict=None, **kwargs):
        super().__init__(**kwargs)

        self.col_fn_dict = {
            'integers': self.gen_integer_col,
            'words': self.gen_word_col
        }

        if gen_rdf:
            self.gen_random_df(nrows, ncols, col_dict)

    def random_string(self):
        """
        Genearte a random string of characters of lenght 4.
        """
        r_string = random.choice(string.ascii_letters)
        for x in range(4):
             r_string += random.choice(string.ascii_letters)
        return r_string

    def gen_integer_col(self, n):
        """
        Generate a list of lenght n of random integers between 1000 and 9999.
        """
        return [random.randint(1000, 9999) for x in range(n)]

    def gen_word_col(self, n):
        """
        Generate a list of lenght n of random strings using the random_string
        method.
        """
        return [self.random_string() for x in range(n)]

    def gen_random_df(self, nrows=10, ncols=2, col_dict=None):
        """
        Generate a random DataFrame where nrows and ncols are the number of rows
        and columns desired. col_dict speficifes the column names and types. If
        col_dict is not specified, the column names will default to colx where x
        is an integet, and col types will be random.

        col_dict is a dict with column names as keys and column types as values.

        The col types available are listed in the col_type_repository.

        Each col type is assigned a generating fucntion in self.col_fn_dict in
        the init. 
        """
        col_type_repository = ['integers', 'words']

        if not col_dict:
            col_dict = {
                f'col{x}': random.choice(col_type_repository) for x in range(ncols)
                }

        else:
            for tpe in col_dict.values():
                if tpe not in col_type_repository:
                    m = f'"{tpe}" not in col_type_repository'
                    raise NotImplementedError(m)

        for col_name, col_type in col_dict.items():
            self[col_name] = self.col_fn_dict[col_type](nrows)

    def add_random_columns(self, col_dict):
        """
        Add a random column(s) to the DataFrame specified by the col_dict.
        """
        for col_name, col_type in col_dict.items():
            self[col_name] = self.col_fn_dict[col_type](len(self))
