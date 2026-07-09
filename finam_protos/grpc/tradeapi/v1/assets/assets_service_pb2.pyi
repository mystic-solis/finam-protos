import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.type import date_pb2 as _date_pb2
from google.type import decimal_pb2 as _decimal_pb2
from google.type import interval_pb2 as _interval_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from grpc.gateway.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[PriceType]
    POSITIVE: _ClassVar[PriceType]
    NON_NEGATIVE: _ClassVar[PriceType]
    ANY: _ClassVar[PriceType]
UNKNOWN: PriceType
POSITIVE: PriceType
NON_NEGATIVE: PriceType
ANY: PriceType

class ExchangesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExchangesResponse(_message.Message):
    __slots__ = ("exchanges",)
    EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    exchanges: _containers.RepeatedCompositeFieldContainer[Exchange]
    def __init__(self, exchanges: _Optional[_Iterable[_Union[Exchange, _Mapping]]] = ...) -> None: ...

class AssetsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssetsResponse(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ...) -> None: ...

class AllAssetsRequest(_message.Message):
    __slots__ = ("cursor", "only_active", "only_disabled")
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ONLY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ONLY_DISABLED_FIELD_NUMBER: _ClassVar[int]
    cursor: int
    only_active: bool
    only_disabled: bool
    def __init__(self, cursor: _Optional[int] = ..., only_active: bool = ..., only_disabled: bool = ...) -> None: ...

class AllAssetsResponse(_message.Message):
    __slots__ = ("assets", "next_cursor")
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    next_cursor: int
    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ..., next_cursor: _Optional[int] = ...) -> None: ...

class GetAssetRequest(_message.Message):
    __slots__ = ("symbol", "account_id")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    account_id: str
    def __init__(self, symbol: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetAssetResponse(_message.Message):
    __slots__ = ("board", "id", "ticker", "mic", "isin", "type", "name", "decimals", "min_step", "lot_size", "expiration_date", "quote_currency", "future_details", "option_details", "bond_details")
    class FutureDetails(_message.Message):
        __slots__ = ("expiration_date", "contract_size")
        EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_SIZE_FIELD_NUMBER: _ClassVar[int]
        expiration_date: _timestamp_pb2.Timestamp
        contract_size: _decimal_pb2.Decimal
        def __init__(self, expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contract_size: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...
    class OptionDetails(_message.Message):
        __slots__ = ("expiration_date", "contract_size", "strike")
        EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_SIZE_FIELD_NUMBER: _ClassVar[int]
        STRIKE_FIELD_NUMBER: _ClassVar[int]
        expiration_date: _timestamp_pb2.Timestamp
        contract_size: _decimal_pb2.Decimal
        strike: _decimal_pb2.Decimal
        def __init__(self, expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contract_size: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., strike: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...
    class BondDetails(_message.Message):
        __slots__ = ("bond_face_value", "currency")
        BOND_FACE_VALUE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        bond_face_value: _decimal_pb2.Decimal
        currency: str
        def __init__(self, bond_face_value: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., currency: _Optional[str] = ...) -> None: ...
    BOARD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    MIN_STEP_FIELD_NUMBER: _ClassVar[int]
    LOT_SIZE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    FUTURE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    OPTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BOND_DETAILS_FIELD_NUMBER: _ClassVar[int]
    board: str
    id: str
    ticker: str
    mic: str
    isin: str
    type: str
    name: str
    decimals: int
    min_step: int
    lot_size: _decimal_pb2.Decimal
    expiration_date: _date_pb2.Date
    quote_currency: str
    future_details: GetAssetResponse.FutureDetails
    option_details: GetAssetResponse.OptionDetails
    bond_details: GetAssetResponse.BondDetails
    def __init__(self, board: _Optional[str] = ..., id: _Optional[str] = ..., ticker: _Optional[str] = ..., mic: _Optional[str] = ..., isin: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., decimals: _Optional[int] = ..., min_step: _Optional[int] = ..., lot_size: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., expiration_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., quote_currency: _Optional[str] = ..., future_details: _Optional[_Union[GetAssetResponse.FutureDetails, _Mapping]] = ..., option_details: _Optional[_Union[GetAssetResponse.OptionDetails, _Mapping]] = ..., bond_details: _Optional[_Union[GetAssetResponse.BondDetails, _Mapping]] = ...) -> None: ...

class GetAssetParamsRequest(_message.Message):
    __slots__ = ("symbol", "account_id")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    account_id: str
    def __init__(self, symbol: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetAssetParamsResponse(_message.Message):
    __slots__ = ("symbol", "account_id", "tradeable", "longable", "shortable", "long_risk_rate", "long_collateral", "short_risk_rate", "short_collateral", "long_initial_margin", "short_initial_margin", "is_tradable", "price_type")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TRADEABLE_FIELD_NUMBER: _ClassVar[int]
    LONGABLE_FIELD_NUMBER: _ClassVar[int]
    SHORTABLE_FIELD_NUMBER: _ClassVar[int]
    LONG_RISK_RATE_FIELD_NUMBER: _ClassVar[int]
    LONG_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    SHORT_RISK_RATE_FIELD_NUMBER: _ClassVar[int]
    SHORT_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    LONG_INITIAL_MARGIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_INITIAL_MARGIN_FIELD_NUMBER: _ClassVar[int]
    IS_TRADABLE_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    account_id: str
    tradeable: bool
    longable: Longable
    shortable: Shortable
    long_risk_rate: _decimal_pb2.Decimal
    long_collateral: _money_pb2.Money
    short_risk_rate: _decimal_pb2.Decimal
    short_collateral: _money_pb2.Money
    long_initial_margin: _money_pb2.Money
    short_initial_margin: _money_pb2.Money
    is_tradable: _wrappers_pb2.BoolValue
    price_type: PriceType
    def __init__(self, symbol: _Optional[str] = ..., account_id: _Optional[str] = ..., tradeable: bool = ..., longable: _Optional[_Union[Longable, _Mapping]] = ..., shortable: _Optional[_Union[Shortable, _Mapping]] = ..., long_risk_rate: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., long_collateral: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., short_risk_rate: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., short_collateral: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., long_initial_margin: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., short_initial_margin: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., is_tradable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., price_type: _Optional[_Union[PriceType, str]] = ...) -> None: ...

class OptionsChainRequest(_message.Message):
    __slots__ = ("underlying_symbol", "root", "expiration_date")
    UNDERLYING_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    underlying_symbol: str
    root: str
    expiration_date: _date_pb2.Date
    def __init__(self, underlying_symbol: _Optional[str] = ..., root: _Optional[str] = ..., expiration_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class OptionsChainResponse(_message.Message):
    __slots__ = ("symbol", "options")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    options: _containers.RepeatedCompositeFieldContainer[Option]
    def __init__(self, symbol: _Optional[str] = ..., options: _Optional[_Iterable[_Union[Option, _Mapping]]] = ...) -> None: ...

class ScheduleRequest(_message.Message):
    __slots__ = ("symbol",)
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    def __init__(self, symbol: _Optional[str] = ...) -> None: ...

class ScheduleResponse(_message.Message):
    __slots__ = ("symbol", "sessions")
    class Sessions(_message.Message):
        __slots__ = ("type", "interval")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_FIELD_NUMBER: _ClassVar[int]
        type: str
        interval: _interval_pb2.Interval
        def __init__(self, type: _Optional[str] = ..., interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ...) -> None: ...
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    sessions: _containers.RepeatedCompositeFieldContainer[ScheduleResponse.Sessions]
    def __init__(self, symbol: _Optional[str] = ..., sessions: _Optional[_Iterable[_Union[ScheduleResponse.Sessions, _Mapping]]] = ...) -> None: ...

class ClockRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClockResponse(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Exchange(_message.Message):
    __slots__ = ("mic", "name")
    MIC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    mic: str
    name: str
    def __init__(self, mic: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Asset(_message.Message):
    __slots__ = ("symbol", "id", "ticker", "mic", "isin", "type", "name", "is_archived")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    id: str
    ticker: str
    mic: str
    isin: str
    type: str
    name: str
    is_archived: bool
    def __init__(self, symbol: _Optional[str] = ..., id: _Optional[str] = ..., ticker: _Optional[str] = ..., mic: _Optional[str] = ..., isin: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., is_archived: bool = ...) -> None: ...

class Option(_message.Message):
    __slots__ = ("symbol", "type", "contract_size", "trade_first_day", "trade_last_day", "strike", "multiplier", "expiration_first_day", "expiration_last_day")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Option.Type]
        TYPE_CALL: _ClassVar[Option.Type]
        TYPE_PUT: _ClassVar[Option.Type]
    TYPE_UNSPECIFIED: Option.Type
    TYPE_CALL: Option.Type
    TYPE_PUT: Option.Type
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SIZE_FIELD_NUMBER: _ClassVar[int]
    TRADE_FIRST_DAY_FIELD_NUMBER: _ClassVar[int]
    TRADE_LAST_DAY_FIELD_NUMBER: _ClassVar[int]
    STRIKE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIRST_DAY_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_LAST_DAY_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    type: Option.Type
    contract_size: _decimal_pb2.Decimal
    trade_first_day: _date_pb2.Date
    trade_last_day: _date_pb2.Date
    strike: _decimal_pb2.Decimal
    multiplier: _decimal_pb2.Decimal
    expiration_first_day: _date_pb2.Date
    expiration_last_day: _date_pb2.Date
    def __init__(self, symbol: _Optional[str] = ..., type: _Optional[_Union[Option.Type, str]] = ..., contract_size: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., trade_first_day: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., trade_last_day: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., strike: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., multiplier: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., expiration_first_day: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., expiration_last_day: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class Longable(_message.Message):
    __slots__ = ("value", "halted_days")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_AVAILABLE: _ClassVar[Longable.Status]
        AVAILABLE: _ClassVar[Longable.Status]
        ACCOUNT_NOT_APPROVED: _ClassVar[Longable.Status]
    NOT_AVAILABLE: Longable.Status
    AVAILABLE: Longable.Status
    ACCOUNT_NOT_APPROVED: Longable.Status
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HALTED_DAYS_FIELD_NUMBER: _ClassVar[int]
    value: Longable.Status
    halted_days: int
    def __init__(self, value: _Optional[_Union[Longable.Status, str]] = ..., halted_days: _Optional[int] = ...) -> None: ...

class Shortable(_message.Message):
    __slots__ = ("value", "halted_days")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_AVAILABLE: _ClassVar[Shortable.Status]
        AVAILABLE: _ClassVar[Shortable.Status]
        HTB: _ClassVar[Shortable.Status]
        ACCOUNT_NOT_APPROVED: _ClassVar[Shortable.Status]
        AVAILABLE_STRATEGY: _ClassVar[Shortable.Status]
    NOT_AVAILABLE: Shortable.Status
    AVAILABLE: Shortable.Status
    HTB: Shortable.Status
    ACCOUNT_NOT_APPROVED: Shortable.Status
    AVAILABLE_STRATEGY: Shortable.Status
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HALTED_DAYS_FIELD_NUMBER: _ClassVar[int]
    value: Shortable.Status
    halted_days: int
    def __init__(self, value: _Optional[_Union[Shortable.Status, str]] = ..., halted_days: _Optional[int] = ...) -> None: ...

class GetConstituentsRequest(_message.Message):
    __slots__ = ("symbol", "cursor")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    cursor: int
    def __init__(self, symbol: _Optional[str] = ..., cursor: _Optional[int] = ...) -> None: ...

class GetConstituentsResponse(_message.Message):
    __slots__ = ("constituents", "next_cursor")
    CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    constituents: _containers.RepeatedCompositeFieldContainer[Constituents]
    next_cursor: int
    def __init__(self, constituents: _Optional[_Iterable[_Union[Constituents, _Mapping]]] = ..., next_cursor: _Optional[int] = ...) -> None: ...

class Constituents(_message.Message):
    __slots__ = ("symbol", "name", "sector", "sub_sector", "cik", "index_inclusion_date")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    SUB_SECTOR_FIELD_NUMBER: _ClassVar[int]
    CIK_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCLUSION_DATE_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    name: str
    sector: str
    sub_sector: str
    cik: str
    index_inclusion_date: _date_pb2.Date
    def __init__(self, symbol: _Optional[str] = ..., name: _Optional[str] = ..., sector: _Optional[str] = ..., sub_sector: _Optional[str] = ..., cik: _Optional[str] = ..., index_inclusion_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...
