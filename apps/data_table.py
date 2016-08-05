from apps.column import Column
from apps.relationship import Relationship
from apps.exception import InvalidDatatype


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

    def add_column(self, name, kind, description=''):
        self._validate_kind(kind)
        column = Column(name, kind, description=description)
        self.columns.append(column)
        return column

    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception('InvalidDatatype')

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

    def _get_name(self):
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

    # Setters

    def _set_name(self, name):
        self._name = name

    # Deletters

    def _del_name(self):
        raise AttributeError('Not allowed delete name attribute')

    name = property(_get_name, _set_name, _del_name)