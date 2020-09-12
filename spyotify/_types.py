from typing import Dict, Generic, Protocol, TypeVar, Union

T = TypeVar("T")


class EntityType(Protocol):
    # pylint: disable=too-few-public-methods
    """
    Entity Object Type
    """
    __dataclass_fields__: Dict
