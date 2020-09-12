from dataclasses import dataclass
from typing import Dict, Generic, List, Optional, TypeVar, Union


@dataclass
class AlbumSimplified:
    album_type: str
    artists: List  # ArtistSimplified
    available_markets: List[str]
    external_urls: Dict
    href: str
    id: str
    images: List
    name: str
    type: str
    uri: str
    album_group: Optional[str] = None


Entity = Union[AlbumSimplified]


@dataclass
class Paging:
    href: str
    items: List[Entity]
    limit: int
    offset: int
    total: int
    previous: Optional[str] = None
    next: Optional[str] = None
