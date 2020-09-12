from typing import List

from apywrapper import Apy, get

from ._models import AlbumSimplified, Paging


class Spotify(Apy):
    def __init__(self, token: str, host: str = "https://api.spotify.com/v1") -> None:
        super().__init__(host, headers={"Authorization": f"Bearer {token}"})

    @get("/artists/{id}/albums")
    def get_artists_albums(self, album_id: str) -> Paging:
        return {"id": album_id}
