class Column:
    """It is a column on DataTable
    This class contains information of a column and
    to validation a data according to the data type set in the constructor.

    Attributes:
        name: Name of column
        kind: Type of data (varchar, bigint, numeric and etc)
        description: Description of column
    """
    def __init__(self, name, kind, description):
        """Constructor

        Args:
            name: Name of column
            kind: Type of data (varchar, int, date, and etc)
            description: Description of column
        """
        self._name = name
        self._kind = kind
        self._description = description