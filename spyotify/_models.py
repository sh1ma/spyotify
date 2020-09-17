from __future__ import annotations

from typing import Dict, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel
from pydantic.generics import GenericModel


class Album(BaseModel):
    album_type: str
    artists: List[ArtistSimplified]
    available_markets: List[str]
    copyrights: List[Copyright]
    external_ids: Dict
    external_urls: Dict
    genres: List[str]
    href: str
    id: str
    images: List[Image]
    label: str
    name: str
    popularity: int
    release_date: str
    release_date_precision: str
    restrictions: Dict
    tracks: Paging
    type: str
    uri: str


class AlbumSimplified(BaseModel):
    album_type: str
    artists: List[ArtistSimplified]
    available_markets: List[str]
    external_urls: Dict
    href: str
    id: str
    images: List[Image]
    name: str
    type: str
    uri: str
    album_group: Optional[str] = None


class Artist(BaseModel):
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


class ArtistSimplified(BaseModel):
    external_urls: Dict
    href: str
    id: str
    name: str
    type: str
    uri: str


class AudioFeatures(BaseModel):
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


class Category(BaseModel):
    href: str
    icons: List
    id: str
    name: str


class Context(BaseModel):
    type: str
    href: str
    external_urls: Dict
    uri: str


class Copyright(BaseModel):
    text: str
    type: str


class Cursor(BaseModel):
    after: str


class Disallows(BaseModel):
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


class Error(BaseModel):
    status: int
    message: str


class PlayerError(BaseModel):
    status: int
    message: str
    reason: str


class Followers(BaseModel):
    href: str
    total: int


class Image(BaseModel):
    height: int
    url: str
    width: int


class PlayHistory(BaseModel):
    track: TrackSimplified
    played_at: str  # datetime
    context: Context


class Playlist(BaseModel):
    collaborative: bool
    external_urls: Dict
    followers: Followers
    href: str
    id: str
    images: List[Image]
    name: str
    owner: User
    snapshot_id: str
    tracks: Paging
    type: str
    uri: str
    description: Optional[str] = None
    public: Optional[bool] = None


class PlaylistSimplified(BaseModel):
    collaborative: bool
    external_urls: Dict
    href: str
    id: str
    images: List[Image]
    name: str
    owner: User
    snapshot_id = str
    tracks: Paging
    type: str
    uri: str
    description: Optional[str] = None
    public: Optional[bool] = None


class PlayListTrack(BaseModel):
    is_local: bool
    track: Union[Track, Episode]
    added_at: Optional[str] = None  # datetime
    added_by: Optional[User] = None


class Recommendations(BaseModel):
    seeds: List
    tracks: List[TrackSimplified]


class RecommendationsSeed(BaseModel):
    afterFilteringSize: int
    afterRelinkingSize: int
    id: str
    initialPoolSize: int
    type: str
    href: Optional[str] = None


class SavedTrack(BaseModel):
    added_at: str  # datetime
    track: Track


class SavedAlbum(BaseModel):
    added_at: str  # datetime
    album: Album


class SavedShow(BaseModel):
    added_at: str  # datetime
    album: Show


class Track(BaseModel):
    album: AlbumSimplified
    artists: List[ArtistSimplified]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: dict
    external_urls: dict
    href: str
    id: str
    is_playable: bool
    linked_from: TrackLink
    restrictions: Dict
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str
    is_local: bool


class TrackSimplified(BaseModel):
    artists: List[ArtistSimplified]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_urls: Dict
    href: str
    id: str
    is_playable: bool
    linked_from: TrackLink
    restrictions: str
    name: str
    preview_url: str
    track_number: int
    type: str
    uri: str
    is_local: bool


class TrackLink(BaseModel):
    external_urls: Dict
    href: str
    id: str
    type: str
    uri: str


class Episode(BaseModel):
    description: str
    duration_ms: int
    explicit: bool
    external_urls: Dict
    href: str
    id: str
    images: List[Image]
    is_externally_hosted: bool
    is_playable: bool
    language: str
    languages: List[str]
    name: str
    release_date: str
    release_date_precision: str
    resume_point: ResumePoint
    show: ShowSimplified
    type: str
    uri: str
    audio_preview_url: Optional[str] = None


class EpisodeSimplified(BaseModel):
    description: str
    duration_ms: int
    explicit: bool
    external_urls: Dict
    href: str
    id: str
    images: List[Image]
    is_externally_hosted: bool
    is_playable: bool
    language: str
    languages: List[str]
    name: str
    release_date: str
    release_date_precision: str
    resume_point: ResumePoint
    type: str
    uri: str
    audio_preview_url: Optional[str] = None


class ResumePoint(BaseModel):
    fully_played: bool
    resume_position_ms: int


class Show(BaseModel):
    available_markets: List[str]
    copyrights: List[Copyright]
    description: str
    explicit: bool
    episodes: Paging
    external_urls: Dict
    href: str
    id: str
    images: List[Image]
    languages: List[str]
    media_type: str
    name: str
    publisher: str
    type: str
    uri: str
    is_externally_hosted: Optional[bool] = None


class ShowSimplified(BaseModel):
    available_markets: List[str]
    copyrights: List[Copyright]
    description: str
    explicit: bool
    episodes: Paging
    external_urls: Dict
    href: str
    id: str
    images: List[Image]
    languages: List[str]
    media_type: str
    name: str
    publisher: str
    type: str
    uri: str
    is_externally_hosted: Optional[bool] = None


class User(BaseModel):
    external_urls: Dict
    followers: Followers
    href: str
    id: str
    images: List[Image]
    type: str
    uri: str
    display_name: Optional[str] = None


T = TypeVar("T")  # pylint: disable=invalid-name


class Paging(GenericModel, Generic[T]):
    href: str
    items: List[T]
    limit: int
    offset: int
    total: int
    previous: Optional[str] = None
    next: Optional[str] = None


class CursorBasedPaging(GenericModel, Generic[T]):
    href: str
    items: List[T]
    limit: int
    cusor: Dict
    total: int
    next: Optional[str] = None


AlbumSimplified.update_forward_refs()
