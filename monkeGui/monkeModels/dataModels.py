class Raider:
    def __init__(self, name):
        self.name = name
        self.builds = []
        self._added_builds = []
        self._removed_builds = []

    def add_played_build(self, build):
        self.builds.append(build)

    def add_build(self, role):
        self._added_builds.append(role)

    def remove_build(self, role):
        if role in self.builds:
            self._removed_builds.remove(role)


class Build:
    def __init__(self, name):
        self._name = name
        self.roles = []
        self.alac = False
        self.quick = False
        self.heal = False
        self._changes = {}
        self._added_roles = []
        self._removed_roles = []

    def add_role(self, role):
        self._added_roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self._removed_roles.remove(role)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._changes['name'] = value

    @property
    def alac(self):
        return self.alac

    @alac.setter
    def alac(self, value):
        self.alac = value
        self._changes['alac'] = value

    def reset_changes(self):
        self._added_roles.clear()
        self._removed_roles.clear()
        self._changes = {}

    def get_changes(self):
        return self._changes


class Boss:
    def __int__(self, name, wing, order):
        self.name = name
        self.wing = wing
        self.order = order
        self._roles = []

    def add_roles(self, role):
        self._roles.append(role)


class Role:
    def __init__(self, name):
        self._name = name
        self._changes = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._changes['name'] = value

    def reset_changes(self):
        self._changes = {}

    def get_changes(self):
        return self._changes

