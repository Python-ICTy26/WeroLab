import dataclasses
import math
import time
import typing as tp

from vkapi import session
from vkapi.config import VK_CONFIG
from vkapi.exceptions import APIError

QueryParams = tp.Optional[tp.Dict[str, tp.Union[str, int]]]


@dataclasses.dataclass(frozen=True)
class FriendsResponse:
    count: int
    items: tp.Union[tp.List[int], tp.List[tp.Dict[str, tp.Any]]]


def get_friends(
    user_id: int,
    count: int = 5000,
    offset: int = 0,
    fields: tp.Optional[tp.List[str]] = None,
) -> FriendsResponse:
    query_params = {
        "user_id": user_id,
        "count": count,
        "offset": offset,
        "fields": fields,
    }

    response = session.get("friends.get", **query_params)
    response_data = response.json()["response"]
    return FriendsResponse(**response_data)


class MutualFriends(tp.TypedDict):
    id: int
    common_friends: tp.List[int]
    common_count: int


def get_mutual(
    source_uid: tp.Optional[int] = None,
    target_uid: tp.Optional[int] = None,
    target_uids: tp.Optional[tp.List[int]] = None,
    order: str = "",
    count: tp.Optional[int] = None,
    offset: int = 0,
    progress=None,
) -> tp.Union[tp.List[int], tp.List[MutualFriends]]:
    query_params = {
        "source_uid": source_uid,
        "target_uid": target_uid,
        "target_uids": target_uids,
        "order": order,
        "count": count,
        "offset": offset,
        "progress": progress,
    }
    limit = VK_CONFIG["target_limit"]
    number = len(count) / limit
    count = math.ceil(number)

    mutual_list = []
    count = 0
    start = 0
    time.time()
    for i in range(count):
        response = session.get("friends.getMutual", **query_params)
        if response.status_code == 200:
            response_data = response.json()["response"]
            mutual_list.extend(response_data)
        parm = query_params["offset"]
        parm += VK_CONFIG["target_limit"]
        count += 1

        requests_time = time.time() - start
        if requests_time < 1 and count >= 3:
            time.sleep(1 - requests_time)
            start = time.time()
            count = 0
    friends = [MutualFriends(**item) for item in mutual_list]
    return friends
