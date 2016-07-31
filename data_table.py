from column import Column


class DataTable:
    """It is a table data.
    This class represents a transparency portal data table.
    It must be able to validate inserted rows according to the columns that have.
    The inserted rows are recorded in it.

    Attributes:
        name: Name of table
        columns: list of columns
        data: list of data
    """
    def __init__(self, name):
        """Constructor

        Args:
            name: Name of table
        """
        self._name = name
        self._columns = []
        self._data = []

    def add_column(self, name, kind, description):
        column = Column(name, kind, description)
        self._columns.append(column)
        return column

    # Getters

    @property
    def name(self):
        return self._name

    @property
    def columns(self):
        return self._columns


    @property
    def data(self):
        return self._data
