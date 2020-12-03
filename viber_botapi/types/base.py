from typing import Optional

from botapi import ModelMeta, SerializableModel
from botapi.types import TypedList


class ViberModel(SerializableModel, metaclass=ModelMeta):
    @property
    def min_api_version(self) -> int:
        return 1

    def serialize(
        self,
        data_to_update: Optional[dict] = None,
        add_min_api_ver: Optional[bool] = None
    ) -> dict:
        serialized_obj = {}
        if add_min_api_ver is True:
            serialized_obj['min_api_version'] = self.min_api_version
        aliases = getattr(self, '_aliases', {})
        for field in getattr(self, '_fields', set()):
            value = getattr(self, field)
            if value is None:
                continue
            serialized_value = self._serialize_value(value, add_min_api_ver)
            serialized_obj[aliases.get(field, field)] = serialized_value
            if add_min_api_ver is True and type(serialized_value) == dict:
                serialized_obj['min_api_version'] = max(
                    serialized_obj.get('min_api_version', 1),
                    serialized_value.pop('min_api_version', 1)
                )
        if data_to_update is not None:
            serialized_obj.update(data_to_update)
        return serialized_obj

    @staticmethod
    def _serialize_value(value, add_min_api_ver: Optional[bool] = None):
        if type(value) == TypedList:
            return [i.serialize() if isinstance(i, SerializableModel) else i
                    for i in value]
        elif isinstance(value, ViberModel):
            return value.serialize(add_min_api_ver=add_min_api_ver)
        else:
            return value
