from nicegui import ui
import monkeDAO
import json
from CompDAO import CompDAO

raiders = monkeDAO.get_raiders("SC")
boss_wings = {}
builds = []
buildButtons = []
roles = []

for i in range(1, 8):
    boss_wings[i] = monkeDAO.get_wing(i)


def show_roles(wing):
    global boss_wings
    with ui.row().classes():
        for boss in boss_wings[wing]:
            with ui.column().classes('mx-2  my-2'):
                ui.label(boss_wings[wing][boss]["boss_name"]).classes("text-center font-weight-bold text-primary")
                with ui.grid(columns=2):
                    for role in list(boss_wings[wing][boss]["roles"]):
                        role_label = ui.label(role).tooltip("Click me to add/remove this role!")
                        toggle = ui.toggle([1, 2, 3], value=2)
                        toggle.set_enabled(False)


@ui.refreshable
def refresh_builds() -> None:
    for build in builds:
        button = ui.button(build)
        button.props('inline color=blue')
        buildButtons.append(button)


def build_click(button):
    for other_button in buildButtons:
        other_button.props('inline color=blue')
    button.props('inline color=green')


def update_build(name):
    if name is not None:
        global builds
        builds = monkeDAO.get_builds("SC", raiderSelection.value)
        refresh_builds.refresh()


with ui.header():
    ui.label("ROLE SHEET 0.9 BEECHES").classes("text-center font-weight-bold text-primary").style("font-size: 200%;")
    raiderSelection = ui.select(options=list(raiders), label="select a gaymer",
                                on_change=lambda r: update_build(r.value)).classes('w-full')

with ui.tabs().classes('w-full').bind_visibility_from(raiderSelection, "value") as wings:
    w1 = ui.tab('W1')
    w2 = ui.tab('W2')
    w3 = ui.tab('W3')
    w4 = ui.tab('W4')
    w5 = ui.tab('W5')
    w6 = ui.tab('W6')
    w7 = ui.tab('W7')

with ui.row().bind_visibility_from(wings, "visible"):
    with ui.column() as buildSelection:
        refresh_builds()

    with ui.column():
        with ui.tab_panels(wings, value=w1).classes('w-half'):
            with ui.tab_panel(w1):
                show_roles(1)
            with ui.tab_panel(w2):
                show_roles(2)
            with ui.tab_panel(w3):
                show_roles(3)
            with ui.tab_panel(w4):
                show_roles(4)
            with ui.tab_panel(w5):
                show_roles(5)
            with ui.tab_panel(w6):
                show_roles(6)
            with ui.tab_panel(w7):
                show_roles(7)

ui.run()
