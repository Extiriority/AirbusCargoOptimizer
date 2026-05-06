from nicegui import ui
from src.views.app_page import APP_NAME, create_app

create_app()
ui.run(title=APP_NAME)