from column import Column
from relationship import Relationship


class DataTable:
    """It is a table data.
    This class represents a transparency portal data table.
    It must be able to validate inserted rows according to the columns that have.
    The inserted rows are recorded in it.
    """

    def __init__(self, name):
        """Constructor

        Args:
            name: name of table

        Attributes:
            name: name of table
            columns: list of columns
            data: list of data
        """

        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def add_column(self, name, kind, description):
        column = Column(name, kind, description)
        self.columns.append(column)
        return column

    def add_references(self, name, to, on):
        """Create a reference this table to other table

        Args:
            name: name of relationship
            to: instance of table pointed
            on: instance column in which there is the relationship
        """

        relationship = Relationship(name, self, to, on)
        self.references.append(relationship)

    def add_referenced(self, name, by, on):
        """Create a reference to another table that points to this

            Args:
                name: name of relationship
                by: instance of table that points to this
                on: instance column which there is the relationship
        """

        relationship = Relationship(name, by, self, on)
        self.referenced.append(relationship)

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

    @property
    def references(self):
        return self._references

    @property
    def referenced(self):
        return self._referenced