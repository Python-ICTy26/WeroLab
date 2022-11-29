import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    frields_list = get_friends(
        user_id,
        fields=["bdate"],
    )
    date_list = [
        friend.get("bdate", None) for friend in frields_list.items if isinstance(friend, dict)
    ]
    amount_of_friends = 0
    mutual_age = 0
    for d in date_list:
        birth = dt.datetime.strptime(d.replace(".", ""), r"%d%m%Y").date()
        amount_of_friends += 1
        age = (dt.datetime.now().date() - birth).days // 365
        mutual_age += age
    if amount_of_friends != 0:
        return mutual_age / amount_of_friends
    else:
        return None
