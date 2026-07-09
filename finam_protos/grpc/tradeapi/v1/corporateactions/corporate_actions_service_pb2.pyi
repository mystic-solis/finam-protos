from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from grpc.gateway.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.type import decimal_pb2 as _decimal_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BondEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[BondEventType]
    COUPON: _ClassVar[BondEventType]
    AMORTIZATION: _ClassVar[BondEventType]
    OFFER: _ClassVar[BondEventType]

class ConvertationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVTYPE_UNKNOWN: _ClassVar[ConvertationType]
    BUYBACK: _ClassVar[ConvertationType]
    CALL_OPTION_EXERCISED: _ClassVar[ConvertationType]
    DRAWINGS: _ClassVar[ConvertationType]
    DRAWINGS_BY_LOTTERY: _ClassVar[ConvertationType]
    EARLY_CONVERSION: _ClassVar[ConvertationType]
    MATURITY: _ClassVar[ConvertationType]
    ORDINARY: _ClassVar[ConvertationType]
    PUT_OPTION_EXERCISED: _ClassVar[ConvertationType]
    TENDER_OFFER: _ClassVar[ConvertationType]

class SortDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASC: _ClassVar[SortDirection]
    DESC: _ClassVar[SortDirection]
UNSPECIFIED: BondEventType
COUPON: BondEventType
AMORTIZATION: BondEventType
OFFER: BondEventType
CONVTYPE_UNKNOWN: ConvertationType
BUYBACK: ConvertationType
CALL_OPTION_EXERCISED: ConvertationType
DRAWINGS: ConvertationType
DRAWINGS_BY_LOTTERY: ConvertationType
EARLY_CONVERSION: ConvertationType
MATURITY: ConvertationType
ORDINARY: ConvertationType
PUT_OPTION_EXERCISED: ConvertationType
TENDER_OFFER: ConvertationType
ASC: SortDirection
DESC: SortDirection

class GetFutureSplitsRequest(_message.Message):
    __slots__ = ("symbol", "sort_direction", "limit", "offset")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    sort_direction: SortDirection
    limit: int
    offset: int
    def __init__(self, symbol: _Optional[str] = ..., sort_direction: _Optional[_Union[SortDirection, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetFutureSplitsResponse(_message.Message):
    __slots__ = ("symbol", "pagination", "splits")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    SPLITS_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    pagination: Pagination
    splits: _containers.RepeatedCompositeFieldContainer[SplitInfo]
    def __init__(self, symbol: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ..., splits: _Optional[_Iterable[_Union[SplitInfo, _Mapping]]] = ...) -> None: ...

class GetPastSplitsRequest(_message.Message):
    __slots__ = ("symbol", "date_from", "date_to", "sort_direction", "limit", "offset")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    date_from: _date_pb2.Date
    date_to: _date_pb2.Date
    sort_direction: SortDirection
    limit: int
    offset: int
    def __init__(self, symbol: _Optional[str] = ..., date_from: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., date_to: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., sort_direction: _Optional[_Union[SortDirection, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetPastSplitsResponse(_message.Message):
    __slots__ = ("symbol", "pagination", "splits")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    SPLITS_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    pagination: Pagination
    splits: _containers.RepeatedCompositeFieldContainer[SplitInfo]
    def __init__(self, symbol: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ..., splits: _Optional[_Iterable[_Union[SplitInfo, _Mapping]]] = ...) -> None: ...

class GetFutureBondsEventsRequest(_message.Message):
    __slots__ = ("symbol", "date_from", "date_to", "sort_direction", "limit", "offset")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    date_from: _date_pb2.Date
    date_to: _date_pb2.Date
    sort_direction: SortDirection
    limit: int
    offset: int
    def __init__(self, symbol: _Optional[str] = ..., date_from: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., date_to: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., sort_direction: _Optional[_Union[SortDirection, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetFutureBondsEventsResponse(_message.Message):
    __slots__ = ("symbol", "pagination", "events")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    pagination: Pagination
    events: _containers.RepeatedCompositeFieldContainer[BondEvent]
    def __init__(self, symbol: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ..., events: _Optional[_Iterable[_Union[BondEvent, _Mapping]]] = ...) -> None: ...

class GetPastBondsEventsRequest(_message.Message):
    __slots__ = ("symbol", "date_from", "date_to", "sort_direction", "limit", "offset")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    date_from: _date_pb2.Date
    date_to: _date_pb2.Date
    sort_direction: SortDirection
    limit: int
    offset: int
    def __init__(self, symbol: _Optional[str] = ..., date_from: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., date_to: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., sort_direction: _Optional[_Union[SortDirection, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetPastBondsEventsResponse(_message.Message):
    __slots__ = ("symbol", "pagination", "events")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    pagination: Pagination
    events: _containers.RepeatedCompositeFieldContainer[BondEvent]
    def __init__(self, symbol: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ..., events: _Optional[_Iterable[_Union[BondEvent, _Mapping]]] = ...) -> None: ...

class BondEvent(_message.Message):
    __slots__ = ("date", "type", "value", "currency", "coupon_details", "amortization_details", "offer_details")
    DATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    COUPON_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AMORTIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    OFFER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    type: BondEventType
    value: _decimal_pb2.Decimal
    currency: _wrappers_pb2.StringValue
    coupon_details: CouponEventDetails
    amortization_details: AmortizationEventDetails
    offer_details: OfferEventDetails
    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., type: _Optional[_Union[BondEventType, str]] = ..., value: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., currency: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., coupon_details: _Optional[_Union[CouponEventDetails, _Mapping]] = ..., amortization_details: _Optional[_Union[AmortizationEventDetails, _Mapping]] = ..., offer_details: _Optional[_Union[OfferEventDetails, _Mapping]] = ...) -> None: ...

class CouponEventDetails(_message.Message):
    __slots__ = ("record_date", "start_date", "face_value", "value_percent")
    RECORD_DATE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    FACE_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    record_date: _date_pb2.Date
    start_date: _date_pb2.Date
    face_value: _decimal_pb2.Decimal
    value_percent: _decimal_pb2.Decimal
    def __init__(self, record_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., face_value: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., value_percent: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...

class AmortizationEventDetails(_message.Message):
    __slots__ = ("new_face_value", "initial_face_value", "amortization_percent")
    NEW_FACE_VALUE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_FACE_VALUE_FIELD_NUMBER: _ClassVar[int]
    AMORTIZATION_PERCENT_FIELD_NUMBER: _ClassVar[int]
    new_face_value: _decimal_pb2.Decimal
    initial_face_value: _decimal_pb2.Decimal
    amortization_percent: _decimal_pb2.Decimal
    def __init__(self, new_face_value: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., initial_face_value: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., amortization_percent: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...

class OfferEventDetails(_message.Message):
    __slots__ = ("offer_type", "price", "start_date", "end_date", "agent")
    OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    offer_type: _wrappers_pb2.StringValue
    price: _decimal_pb2.Decimal
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date
    agent: _wrappers_pb2.StringValue
    def __init__(self, offer_type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., price: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., agent: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class SplitInfo(_message.Message):
    __slots__ = ("exec_date", "old_ratio", "new_ratio", "new_lot", "convertation_type")
    EXEC_DATE_FIELD_NUMBER: _ClassVar[int]
    OLD_RATIO_FIELD_NUMBER: _ClassVar[int]
    NEW_RATIO_FIELD_NUMBER: _ClassVar[int]
    NEW_LOT_FIELD_NUMBER: _ClassVar[int]
    CONVERTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    exec_date: _date_pb2.Date
    old_ratio: _decimal_pb2.Decimal
    new_ratio: _decimal_pb2.Decimal
    new_lot: _wrappers_pb2.Int32Value
    convertation_type: ConvertationType
    def __init__(self, exec_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., old_ratio: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., new_ratio: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., new_lot: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., convertation_type: _Optional[_Union[ConvertationType, str]] = ...) -> None: ...

class GetFutureDividendsRequest(_message.Message):
    __slots__ = ("symbol", "sort_direction", "limit", "offset")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    sort_direction: SortDirection
    limit: int
    offset: int
    def __init__(self, symbol: _Optional[str] = ..., sort_direction: _Optional[_Union[SortDirection, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetFutureDividendsResponse(_message.Message):
    __slots__ = ("pagination", "dividends")
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDS_FIELD_NUMBER: _ClassVar[int]
    pagination: Pagination
    dividends: _containers.RepeatedCompositeFieldContainer[Dividend]
    def __init__(self, pagination: _Optional[_Union[Pagination, _Mapping]] = ..., dividends: _Optional[_Iterable[_Union[Dividend, _Mapping]]] = ...) -> None: ...

class GetPastDividendsRequest(_message.Message):
    __slots__ = ("symbol", "sort_direction", "date_from", "date_to", "limit", "offset")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    sort_direction: SortDirection
    date_from: _date_pb2.Date
    date_to: _date_pb2.Date
    limit: int
    offset: int
    def __init__(self, symbol: _Optional[str] = ..., sort_direction: _Optional[_Union[SortDirection, str]] = ..., date_from: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., date_to: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetPastDividendsResponse(_message.Message):
    __slots__ = ("pagination", "dividends")
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDS_FIELD_NUMBER: _ClassVar[int]
    pagination: Pagination
    dividends: _containers.RepeatedCompositeFieldContainer[Dividend]
    def __init__(self, pagination: _Optional[_Union[Pagination, _Mapping]] = ..., dividends: _Optional[_Iterable[_Union[Dividend, _Mapping]]] = ...) -> None: ...

class Dividend(_message.Message):
    __slots__ = ("date", "amount", "currency")
    DATE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    amount: _decimal_pb2.Decimal
    currency: str
    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., amount: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., currency: _Optional[str] = ...) -> None: ...

class Pagination(_message.Message):
    __slots__ = ("total", "limit", "offset", "has_next")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    HAS_NEXT_FIELD_NUMBER: _ClassVar[int]
    total: int
    limit: int
    offset: int
    has_next: bool
    def __init__(self, total: _Optional[int] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., has_next: bool = ...) -> None: ...
