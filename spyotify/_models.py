from dataclasses import dataclass
from typing import Dict, Generic, List, Optional, TypeVar, Union


@dataclass
class Album:
    album_type: str
    artists: List["ArtistSimplified"]
    available_markets: List[str]
    copyrights: List["Copyright"]
    external_ids: Dict
    external_urls: Dict
    genres: List[str]
    href: str
    id: str
    images: List["Image"]
    label: str
    name: str
    popularity: int
    release_date: str
    release_date_precision: str
    restrictions: Dict
    tracks: "Paging"
    type: str
    uri: str


@dataclass
class AlbumSimplified:
    album_type: str
    artists: List["ArtistSimplified"]
    available_markets: List[str]
    external_urls: Dict
    href: str
    id: str
    images: List["Image"]
    name: str
    type: str
    uri: str
    album_group: Optional[str] = None


@dataclass
class Artist:
    external_urls: Dict
    followers: Dict
    genres: List[str]
    href: str
    id: str
    images: List
    name: str
    popularity: int
    type: str
    uri: str


@dataclass
class ArtistSimplified:
    external_urls: Dict
    href: str
    id: str
    name: str
    type: str
    uri: str


@dataclass
class AudioFeatures:
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: int
    energy: float
    id: str
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    speechiness: float
    tempo: float
    time_signature: int
    track_href: str
    type: str
    uri: str
    valence: float


@dataclass
class Category:
    href: str
    icons: List
    id: str
    name: str


@dataclass
class Context:
    type: str
    href: str
    external_urls: Dict
    uri: str


@dataclass
class Copyright:
    text: str
    type: str


@dataclass
class Cursor:
    after: str


@dataclass
class Disallows:
    interrupting_playback: bool
    pausing: bool
    resuming: bool
    seeking: bool
    skipping_next: bool
    skipping_prev: bool
    toggling_repeat_context: bool
    toggling_shuffle: bool
    toggling_repeat_track: bool
    transferring_playback: bool


@dataclass
class Error:
    status: int
    message: str


@dataclass
class PlayerError:
    status: int
    message: str
    reason: str


@dataclass
class Followers:
    href: str
    total: int


@dataclass
class Image:
    height: int
    url: str
    width: int


@dataclass
class PlayHistory:
    track: "TrackSimplified"
    played_at: str  # datetime
    context: "Context"


@dataclass
class Playlist:
    collaborative: bool
    external_urls: Dict
    followers: "Followers"
    href: str
    id: str
    images: List["Image"]
    name: str
    owner: "User"
    snapshot_id: str
    tracks: "Paging"
    type: str
    uri: str
    description: Optional[str] = None
    public: Optional[bool] = None


@dataclass
class PlaylistSimplified:
    collaborative: bool
    external_urls: Dict
    href: str
    id: str
    images: List["Image"]
    name: str
    owner: "User"
    snapshot_id = str
    tracks: "Paging"
    type: str
    uri: str
    description: Optional[str] = None
    public: Optional[bool] = None


@dataclass
class PlayListTrack:
    is_local: bool
    track: Union["Track", "Episode"]
    added_at: Optional[str] = None  # datetime
    added_by: Optional["User"] = None


@dataclass
class Recommendations:
    seeds: List
    tracks: List["TrackSimplified"]


@dataclass
class RecommendationsSeed:
    afterFilteringSize: int
    afterRelinkingSize: int
    id: str
    initialPoolSize: int
    type: str
    href: Optional[str] = None


@dataclass
class SavedTrack:
    added_at: str  # datetime
    track: "Track"


@dataclass
class SavedAlbum:
    added_at: str  # datetime
    album: "Album"


@dataclass
class SavedShow:
    added_at: str  # datetime
    album: "Show"


@dataclass
class Track:
    album: "AlbumSimplified"
    artists: List["ArtistSimplified"]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: dict
    external_urls: dict
    href: str
    id: str
    is_playable: bool
    linked_from: "LinkedTrack"
    restrictions: Dict
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str
    is_local: bool


@dataclass
class TrackSimplified:
    artists: List["ArtistSimplified"]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_urls: Dict
    href: str
    id: str
    is_playable: bool
    linked_from: "LinkedTrack"
    restrictions: str
    name: str
    preview_url: str
    track_number: int
    type: str
    uri: str
    is_local: bool


@dataclass
class TrackLink:
    external_urls: Dict
    href: str
    id: str
    type: str
    uri: str


@dataclass
class Episode:
    description: str
    duration_ms: int
    explicit: bool
    external_urls: Dict
    href: str
    id: str
    images: List["Image"]
    is_externally_hosted: bool
    is_playable: bool
    language: str
    languages: List[str]
    name: str
    release_date: str
    release_date_precision: str
    resume_point: "ResumePoint"
    show: "ShowSimplified"
    type: str
    uri: str
    audio_preview_url: Optional[str] = None


@dataclass
class EpisodeSimplified:
    description: str
    duration_ms: int
    explicit: bool
    external_urls: Dict
    href: str
    id: str
    images: List["Image"]
    is_externally_hosted: bool
    is_playable: bool
    language: str
    languages: List[str]
    name: str
    release_date: str
    release_date_precision: str
    resume_point: "ResumePoint"
    type: str
    uri: str
    audio_preview_url: Optional[str] = None


@dataclass
class ResumePoint:
    fully_played: bool
    resume_position_ms: int


@dataclass
class Show:
    available_markets: List[str]
    copyrights: List["Copyright"]
    description: str
    explicit: bool
    episodes: "Paging"
    external_urls: Dict
    href: str
    id: str
    images: List["Image"]
    languages: List[str]
    media_type: str
    name: str
    publisher: str
    type: str
    uri: str
    is_externally_hosted: Optional[bool] = None


@dataclass
class ShowSimplified:
    available_markets: List[str]
    copyrights: List["Copyright"]
    description: str
    explicit: bool
    episodes: "Paging"
    external_urls: Dict
    href: str
    id: str
    images: List["Image"]
    languages: List[str]
    media_type: str
    name: str
    publisher: str
    type: str
    uri: str
    is_externally_hosted: Optional[bool] = None


@dataclass
class User:
    external_urls: Dict
    followers: "Followers"
    href: str
    id: str
    images: List["Image"]
    type: str
    uri: str
    display_name: Optional[str] = None


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


@dataclass
class CursorBasedPaging:
    href: str
    items: List[Entity]
    limit: int
    cusor: Dict
    total: int
    next: Optional[str] = None
