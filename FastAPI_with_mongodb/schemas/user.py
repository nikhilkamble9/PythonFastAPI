def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "plotno": item["plotno"],
        "address": item["address"],
        "city": item["city"],
        "state": item["state"],
        "country": item["country"],
        "pincode": item["pincode"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
