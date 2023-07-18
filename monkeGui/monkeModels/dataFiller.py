import dataModels


def create_role(json):
    roles = []
    for role in json:
        roles.append(dataModels.Role(role))

    return roles
