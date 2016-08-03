from decimal import Decimal
from exception import InvalidDatatype


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
        self._is_pk = False

    def __str__(self):
        return 'Column: {} | {} | {}'.format(self.name, self.kind, self.description)

    def _validate(cls, kind, data):
        cls._validate_kind(kind)

        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True

    validate = classmethod(_validate)

    @staticmethod
    def _validate_kind(kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise InvalidDatatype

    # Getters

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def description(self):
        return self._description


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=None):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = 'Column: {} | {} | {}'.format(self.name, self.kind, self.description)
        return '{} - {}'.format('PK', _str)

    @property
    def is_pk(self):
        return self._is_pk