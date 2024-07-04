from abc import ABC, abstractmethod


class BaseFaker(ABC):
    _base_fake_data = None

    @classmethod
    @abstractmethod
    def fake(cls, **base_fake_data): ...

    @classmethod
    @abstractmethod
    def fake_many(cls, count: int = 10):
        return [cls.fake() for _ in range(count)]

    @classmethod
    @abstractmethod
    def _fake_attribute(cls, attribute, fallback):
        if cls._base_fake_data is None:
            return

        if attribute in cls._base_fake_data:
            return cls._base_fake_data[attribute]
        else:
            return fallback
