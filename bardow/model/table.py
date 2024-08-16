import pandas as pd
from typing import Self, Set
from dataclasses import dataclass

from bardow.model import variable


@dataclass
class Table:
    variables: Set[variable.Variable]
    data: pd.DataFrame

    @classmethod
    def read_table_from_pdf(cls, pdf) -> Self:
        pass

    @classmethod
    def read_table_from_csv(cls, csv) -> Self:
        pass

    @classmethod
    def read_table_from_excel(cls, excel) -> Self:
        pass

    @classmethod
    def read_table_from_json(cls, json) -> Self:
        pass

    @classmethod
    def read_table_from_dataframe(cls, df) -> Self:
        pass

    def lookup(self, input_variables: Set[variable.Known],
               only_return: Set[variable.Variable] = None):
        if only_return is None:
            only_return = self.variables
        return

    def interpolate(self):
        pass
