from base_plugin import BasePlugin, MenuItemData, MenuItemType


__id__ = "report_helper"
__name__ = "Report Helper"
__description__ = "Помощник для подготовки жалоб"
__author__ = "Nikita"
__version__ = "1.0.0"
__app_version__ = ">=13.1.1"
__sdk_version__ = ">=1.4.4.3"


class ReportHelperPlugin(BasePlugin):

    def on_plugin_load(self):
        self.add_menu_item(
            MenuItemData(
                menu_type=MenuItemType.PROFILE_ACTION_MENU,
                text="Подготовить жалобу",
                on_click=self.prepare_report,
                priority=10
            )
        )

    def prepare_report(self, context):
        user = context.get("user")

        if not user:
            self.logger.warning("Пользователь не найден")
            return

        self.logger.info(
            f"Подготовка жалобы для пользователя ID: {user.id}"
        )
        self.logger.info(
            "Проверь наличие нарушения и доказательства перед отправкой."
        )
