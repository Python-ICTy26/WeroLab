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

    count = 1
    limit = VK_CONFIG["target_limit"]
    assert isinstance(limit, int)
    if target_uids is not None:
        count = math.ceil(len(target_uids) / limit)

    list = []
    send_count = 0
    start = 0.0
    time.time()
    for i in range(count):
        response = session.get("friends.getMutual", **query_params)
        query_params["offset"] += VK_CONFIG["target_limit"]
        send_count += 1
        if response.status_code == 200:
            data = response.json()["response"]
            list.extend(data)
        request_time = time.time() - start
        if request_time < 1 and send_count >= 3:
            time.sleep(1 - request_time)
            start = time.time()
            send_count = 0
    try:
        friends = []
        for i in list:
            friends.append(i)
    except TypeError:
        return list

    return friends
