import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from grpc.gateway.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportForm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_FORM_UNKNOWN: _ClassVar[ReportForm]
    REPORT_FORM_SHORT: _ClassVar[ReportForm]
    REPORT_FORM_LONG: _ClassVar[ReportForm]

class ReportCreationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_FOUND: _ClassVar[ReportCreationStatus]
    PENDING: _ClassVar[ReportCreationStatus]
    IN_PROGRESS: _ClassVar[ReportCreationStatus]
    SUCCESS: _ClassVar[ReportCreationStatus]
    ERROR: _ClassVar[ReportCreationStatus]
REPORT_FORM_UNKNOWN: ReportForm
REPORT_FORM_SHORT: ReportForm
REPORT_FORM_LONG: ReportForm
NOT_FOUND: ReportCreationStatus
PENDING: ReportCreationStatus
IN_PROGRESS: ReportCreationStatus
SUCCESS: ReportCreationStatus
ERROR: ReportCreationStatus

class CreateAccountReportRequest(_message.Message):
    __slots__ = ("date_range", "report_form", "account_id")
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    REPORT_FORM_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    date_range: DateRange
    report_form: ReportForm
    account_id: int
    def __init__(self, date_range: _Optional[_Union[DateRange, _Mapping]] = ..., report_form: _Optional[_Union[ReportForm, str]] = ..., account_id: _Optional[int] = ...) -> None: ...

class CreateAccountReportResponse(_message.Message):
    __slots__ = ("report_id",)
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    report_id: str
    def __init__(self, report_id: _Optional[str] = ...) -> None: ...

class GetAccountReportInfoRequest(_message.Message):
    __slots__ = ("report_id",)
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    report_id: str
    def __init__(self, report_id: _Optional[str] = ...) -> None: ...

class GetAccountReportInfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: AccountReportInfo
    def __init__(self, info: _Optional[_Union[AccountReportInfo, _Mapping]] = ...) -> None: ...

class SubscribeAccountReportInfoRequest(_message.Message):
    __slots__ = ("report_id",)
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    report_id: str
    def __init__(self, report_id: _Optional[str] = ...) -> None: ...

class SubscribeAccountReportInfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: AccountReportInfo
    def __init__(self, info: _Optional[_Union[AccountReportInfo, _Mapping]] = ...) -> None: ...

class AccountReportInfo(_message.Message):
    __slots__ = ("report_id", "status", "date_range", "report_form", "account_id", "url")
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    REPORT_FORM_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    report_id: str
    status: ReportCreationStatus
    date_range: DateRange
    report_form: ReportForm
    account_id: int
    url: _wrappers_pb2.StringValue
    def __init__(self, report_id: _Optional[str] = ..., status: _Optional[_Union[ReportCreationStatus, str]] = ..., date_range: _Optional[_Union[DateRange, _Mapping]] = ..., report_form: _Optional[_Union[ReportForm, str]] = ..., account_id: _Optional[int] = ..., url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class DateRange(_message.Message):
    __slots__ = ("date_begin", "date_end")
    DATE_BEGIN_FIELD_NUMBER: _ClassVar[int]
    DATE_END_FIELD_NUMBER: _ClassVar[int]
    date_begin: _timestamp_pb2.Timestamp
    date_end: _timestamp_pb2.Timestamp
    def __init__(self, date_begin: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
