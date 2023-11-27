from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BooleanResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CO2(_message.Message):
    __slots__ = ["co2", "timestamp"]
    CO2_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    co2: float
    timestamp: float
    def __init__(self, co2: _Optional[float] = ..., timestamp: _Optional[float] = ...) -> None: ...

class Humidity(_message.Message):
    __slots__ = ["humidity", "temperature", "timestamp"]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    humidity: float
    temperature: float
    timestamp: float
    def __init__(self, temperature: _Optional[float] = ..., humidity: _Optional[float] = ..., timestamp: _Optional[float] = ...) -> None: ...

class Pollution(_message.Message):
    __slots__ = ["pollution", "timestamp"]
    POLLUTION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    pollution: float
    timestamp: float
    def __init__(self, pollution: _Optional[float] = ..., timestamp: _Optional[float] = ...) -> None: ...
