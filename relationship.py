class Relationship:
    """ This class represents a relationship between DataType.

    All information that identifier a relantionship between tables.
    In which column it exists, where it comes from and where it goes.
    """

    def __init__(self, name, _from, to, on):
        """Constructor

        Args and attributes:
            name: name of relationship
            from: table it comes from
            to: table where it goes
            on: instance of column, where exist
        """

        self._name = name
        self._from = _from
        self._to = to
        self._on = on