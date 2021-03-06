from typing import Any, Dict, List


class AbstractAsyncSettingsRepository:

    async def get_one(self, setting_name: str) -> Any:
        raise NotImplementedError

    async def set_one(self, setting_name: str, setting_value: Any) -> None:
        raise NotImplementedError

    async def get_many(self, setting_names: List[str]) -> Dict[str, Any]:
        raise NotImplementedError

    async def set_many(self, settings: Dict[str, Any]) -> None:
        raise NotImplementedError

    async def get_all(self) -> Dict[str, Any]:
        raise NotImplementedError

    async def set_all(self, settings: Dict[str, Any]) -> None:
        raise NotImplementedError


class AbstractSyncSettingsRepository:

    def get_one(self, setting_name: str) -> Any:
        raise NotImplementedError

    def set_one(self, setting_name: str, setting_value: Any) -> None:
        raise NotImplementedError

    def get_many(self, setting_names: List[str]) -> Dict[str, Any]:
        raise NotImplementedError

    def set_many(self, settings: Dict[str, Any]) -> None:
        raise NotImplementedError

    def get_all(self) -> Dict[str, Any]:
        raise NotImplementedError

    def set_all(self, settings: Dict[str, Any]) -> None:
        raise NotImplementedError
