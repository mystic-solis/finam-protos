import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUsageMetricsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUsageMetricsResponse(_message.Message):
    __slots__ = ("quotas",)
    class QuotaUsage(_message.Message):
        __slots__ = ("name", "limit", "remaining", "reset_time")
        NAME_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        REMAINING_FIELD_NUMBER: _ClassVar[int]
        RESET_TIME_FIELD_NUMBER: _ClassVar[int]
        name: str
        limit: int
        remaining: int
        reset_time: _timestamp_pb2.Timestamp
        def __init__(self, name: _Optional[str] = ..., limit: _Optional[int] = ..., remaining: _Optional[int] = ..., reset_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    QUOTAS_FIELD_NUMBER: _ClassVar[int]
    quotas: _containers.RepeatedCompositeFieldContainer[GetUsageMetricsResponse.QuotaUsage]
    def __init__(self, quotas: _Optional[_Iterable[_Union[GetUsageMetricsResponse.QuotaUsage, _Mapping]]] = ...) -> None: ...
