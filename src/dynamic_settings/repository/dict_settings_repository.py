from typing import Any, Dict, List

from dynamic_settings.logging import logger
from .abstract_settings_repository import AbstractSyncSettingsRepository


class DictSettingsRepository(AbstractSyncSettingsRepository):

    def __init__(self) -> None:
        self._settings = {}

        logger.debug("Creating instance")

    def get_one(self, setting_name: str) -> Any:
        logger.debug(f"Requested setting {setting_name}")
        return self._settings.get(setting_name)

    def set_one(self, setting_name: str, setting_value: Any) -> None:
        logger.debug(f"Setting {setting_name} is set to {setting_value}")
        self._settings[setting_name] = setting_value

    def get_many(self, setting_names: List[str]) -> Dict[str, Any]:
        logger.debug(f"Requested settings: {setting_names}")
        settings = {}
        for name in setting_names:
            settings[name] = self._settings.get(name)
        return settings

    def set_many(self, settings: Dict[str, Any]) -> None:
        logger.debug("Set many settings is requested")
        self._settings.update(settings)

    def get_all(self) -> Dict[str, Any]:
        logger.debug("All settings are requested")
        settings = self._settings.copy()
        return settings

    def set_all(self, settings: Dict[str, Any]) -> None:
        logger.debug("Set all settings is requested")
        self._settings = settings.copy()
