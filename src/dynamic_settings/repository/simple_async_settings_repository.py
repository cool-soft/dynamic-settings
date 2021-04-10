import logging
from typing import Any, Dict

from dynamic_settings.repository.async_settings_repository import AsyncSettingsRepository


class SimpleAsyncSettingsRepository(AsyncSettingsRepository):

    def __init__(self) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.debug("Creating instance")

        self._settings = {}

    async def get_one(self, setting_name: str) -> Any:
        self._logger.debug(f"Requested setting {setting_name}")
        return self._settings.get(setting_name)

    async def set_one(self, setting_name: str, setting_value: Any) -> None:
        self._logger.debug(f"Setting {setting_name} is set to {setting_value}")
        self._settings[setting_name] = setting_value

    async def get_all(self) -> Dict[str, Any]:
        self._logger.debug(f"All settings are requested")
        settings = self._settings.copy()
        return settings

    async def set_all(self, settings: Dict[str, Any]) -> None:
        self._logger.debug(f"Set all settings is requested")
        self._settings = settings.copy()