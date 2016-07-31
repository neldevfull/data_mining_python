class Column:
    """It is a column on DataTable
    This class contains information of a column and
    to validation a data according to the data type set in the constructor.

    Attributes:
        name: name of column
        kind: type of data (varchar, bigint, numeric and etc)
        description: description of column
    """

    def __init__(self, name, kind, description):
        """Constructor

        Args:
            name: name of column
            kind: type of data (varchar, int, date, and etc)
            description: description of column
        """

        self._name = name
        self._kind = kind
        self._description = description