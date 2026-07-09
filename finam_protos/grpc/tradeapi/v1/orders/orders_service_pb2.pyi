import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import decimal_pb2 as _decimal_pb2
from grpc.tradeapi.v1 import side_pb2 as _side_pb2
from grpc.tradeapi.v1 import trade_pb2 as _trade_pb2
from grpc.gateway.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_TYPE_UNSPECIFIED: _ClassVar[OrderType]
    ORDER_TYPE_MARKET: _ClassVar[OrderType]
    ORDER_TYPE_LIMIT: _ClassVar[OrderType]
    ORDER_TYPE_STOP: _ClassVar[OrderType]
    ORDER_TYPE_STOP_LIMIT: _ClassVar[OrderType]
    ORDER_TYPE_MULTI_LEG: _ClassVar[OrderType]

class TimeInForce(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_IN_FORCE_UNSPECIFIED: _ClassVar[TimeInForce]
    TIME_IN_FORCE_DAY: _ClassVar[TimeInForce]
    TIME_IN_FORCE_GOOD_TILL_CANCEL: _ClassVar[TimeInForce]
    TIME_IN_FORCE_GOOD_TILL_CROSSING: _ClassVar[TimeInForce]
    TIME_IN_FORCE_EXT: _ClassVar[TimeInForce]
    TIME_IN_FORCE_ON_OPEN: _ClassVar[TimeInForce]
    TIME_IN_FORCE_ON_CLOSE: _ClassVar[TimeInForce]
    TIME_IN_FORCE_IOC: _ClassVar[TimeInForce]
    TIME_IN_FORCE_FOK: _ClassVar[TimeInForce]

class StopCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP_CONDITION_UNSPECIFIED: _ClassVar[StopCondition]
    STOP_CONDITION_LAST_UP: _ClassVar[StopCondition]
    STOP_CONDITION_LAST_DOWN: _ClassVar[StopCondition]

class OrderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_STATUS_UNSPECIFIED: _ClassVar[OrderStatus]
    ORDER_STATUS_NEW: _ClassVar[OrderStatus]
    ORDER_STATUS_PARTIALLY_FILLED: _ClassVar[OrderStatus]
    ORDER_STATUS_FILLED: _ClassVar[OrderStatus]
    ORDER_STATUS_DONE_FOR_DAY: _ClassVar[OrderStatus]
    ORDER_STATUS_CANCELED: _ClassVar[OrderStatus]
    ORDER_STATUS_REPLACED: _ClassVar[OrderStatus]
    ORDER_STATUS_PENDING_CANCEL: _ClassVar[OrderStatus]
    ORDER_STATUS_REJECTED: _ClassVar[OrderStatus]
    ORDER_STATUS_SUSPENDED: _ClassVar[OrderStatus]
    ORDER_STATUS_PENDING_NEW: _ClassVar[OrderStatus]
    ORDER_STATUS_EXPIRED: _ClassVar[OrderStatus]
    ORDER_STATUS_FAILED: _ClassVar[OrderStatus]
    ORDER_STATUS_FORWARDING: _ClassVar[OrderStatus]
    ORDER_STATUS_WAIT: _ClassVar[OrderStatus]
    ORDER_STATUS_DENIED_BY_BROKER: _ClassVar[OrderStatus]
    ORDER_STATUS_REJECTED_BY_EXCHANGE: _ClassVar[OrderStatus]
    ORDER_STATUS_WATCHING: _ClassVar[OrderStatus]
    ORDER_STATUS_EXECUTED: _ClassVar[OrderStatus]
    ORDER_STATUS_DISABLED: _ClassVar[OrderStatus]
    ORDER_STATUS_LINK_WAIT: _ClassVar[OrderStatus]
    ORDER_STATUS_SL_GUARD_TIME: _ClassVar[OrderStatus]
    ORDER_STATUS_SL_EXECUTED: _ClassVar[OrderStatus]
    ORDER_STATUS_SL_FORWARDING: _ClassVar[OrderStatus]
    ORDER_STATUS_TP_GUARD_TIME: _ClassVar[OrderStatus]
    ORDER_STATUS_TP_EXECUTED: _ClassVar[OrderStatus]
    ORDER_STATUS_TP_CORRECTION: _ClassVar[OrderStatus]
    ORDER_STATUS_TP_FORWARDING: _ClassVar[OrderStatus]
    ORDER_STATUS_TP_CORR_GUARD_TIME: _ClassVar[OrderStatus]

class ValidBefore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALID_BEFORE_UNSPECIFIED: _ClassVar[ValidBefore]
    VALID_BEFORE_END_OF_DAY: _ClassVar[ValidBefore]
    VALID_BEFORE_GOOD_TILL_CANCEL: _ClassVar[ValidBefore]
    VALID_BEFORE_GOOD_TILL_DATE: _ClassVar[ValidBefore]

class TPSpreadMeasure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TP_SPREAD_MEASURE_UNDEFINED: _ClassVar[TPSpreadMeasure]
    TP_SPREAD_MEASURE_VALUE: _ClassVar[TPSpreadMeasure]
    TP_SPREAD_MEASURE_PERCENT: _ClassVar[TPSpreadMeasure]
ORDER_TYPE_UNSPECIFIED: OrderType
ORDER_TYPE_MARKET: OrderType
ORDER_TYPE_LIMIT: OrderType
ORDER_TYPE_STOP: OrderType
ORDER_TYPE_STOP_LIMIT: OrderType
ORDER_TYPE_MULTI_LEG: OrderType
TIME_IN_FORCE_UNSPECIFIED: TimeInForce
TIME_IN_FORCE_DAY: TimeInForce
TIME_IN_FORCE_GOOD_TILL_CANCEL: TimeInForce
TIME_IN_FORCE_GOOD_TILL_CROSSING: TimeInForce
TIME_IN_FORCE_EXT: TimeInForce
TIME_IN_FORCE_ON_OPEN: TimeInForce
TIME_IN_FORCE_ON_CLOSE: TimeInForce
TIME_IN_FORCE_IOC: TimeInForce
TIME_IN_FORCE_FOK: TimeInForce
STOP_CONDITION_UNSPECIFIED: StopCondition
STOP_CONDITION_LAST_UP: StopCondition
STOP_CONDITION_LAST_DOWN: StopCondition
ORDER_STATUS_UNSPECIFIED: OrderStatus
ORDER_STATUS_NEW: OrderStatus
ORDER_STATUS_PARTIALLY_FILLED: OrderStatus
ORDER_STATUS_FILLED: OrderStatus
ORDER_STATUS_DONE_FOR_DAY: OrderStatus
ORDER_STATUS_CANCELED: OrderStatus
ORDER_STATUS_REPLACED: OrderStatus
ORDER_STATUS_PENDING_CANCEL: OrderStatus
ORDER_STATUS_REJECTED: OrderStatus
ORDER_STATUS_SUSPENDED: OrderStatus
ORDER_STATUS_PENDING_NEW: OrderStatus
ORDER_STATUS_EXPIRED: OrderStatus
ORDER_STATUS_FAILED: OrderStatus
ORDER_STATUS_FORWARDING: OrderStatus
ORDER_STATUS_WAIT: OrderStatus
ORDER_STATUS_DENIED_BY_BROKER: OrderStatus
ORDER_STATUS_REJECTED_BY_EXCHANGE: OrderStatus
ORDER_STATUS_WATCHING: OrderStatus
ORDER_STATUS_EXECUTED: OrderStatus
ORDER_STATUS_DISABLED: OrderStatus
ORDER_STATUS_LINK_WAIT: OrderStatus
ORDER_STATUS_SL_GUARD_TIME: OrderStatus
ORDER_STATUS_SL_EXECUTED: OrderStatus
ORDER_STATUS_SL_FORWARDING: OrderStatus
ORDER_STATUS_TP_GUARD_TIME: OrderStatus
ORDER_STATUS_TP_EXECUTED: OrderStatus
ORDER_STATUS_TP_CORRECTION: OrderStatus
ORDER_STATUS_TP_FORWARDING: OrderStatus
ORDER_STATUS_TP_CORR_GUARD_TIME: OrderStatus
VALID_BEFORE_UNSPECIFIED: ValidBefore
VALID_BEFORE_END_OF_DAY: ValidBefore
VALID_BEFORE_GOOD_TILL_CANCEL: ValidBefore
VALID_BEFORE_GOOD_TILL_DATE: ValidBefore
TP_SPREAD_MEASURE_UNDEFINED: TPSpreadMeasure
TP_SPREAD_MEASURE_VALUE: TPSpreadMeasure
TP_SPREAD_MEASURE_PERCENT: TPSpreadMeasure

class OrderTradeRequest(_message.Message):
    __slots__ = ("action", "data_type", "account_id")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_SUBSCRIBE: _ClassVar[OrderTradeRequest.Action]
        ACTION_UNSUBSCRIBE: _ClassVar[OrderTradeRequest.Action]
    ACTION_SUBSCRIBE: OrderTradeRequest.Action
    ACTION_UNSUBSCRIBE: OrderTradeRequest.Action
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_ALL: _ClassVar[OrderTradeRequest.DataType]
        DATA_TYPE_ORDERS: _ClassVar[OrderTradeRequest.DataType]
        DATA_TYPE_TRADES: _ClassVar[OrderTradeRequest.DataType]
    DATA_TYPE_ALL: OrderTradeRequest.DataType
    DATA_TYPE_ORDERS: OrderTradeRequest.DataType
    DATA_TYPE_TRADES: OrderTradeRequest.DataType
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    action: OrderTradeRequest.Action
    data_type: OrderTradeRequest.DataType
    account_id: str
    def __init__(self, action: _Optional[_Union[OrderTradeRequest.Action, str]] = ..., data_type: _Optional[_Union[OrderTradeRequest.DataType, str]] = ..., account_id: _Optional[str] = ...) -> None: ...

class OrderTradeResponse(_message.Message):
    __slots__ = ("orders", "trades")
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderState]
    trades: _containers.RepeatedCompositeFieldContainer[_trade_pb2.AccountTrade]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderState, _Mapping]]] = ..., trades: _Optional[_Iterable[_Union[_trade_pb2.AccountTrade, _Mapping]]] = ...) -> None: ...

class SubscribeOrdersRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class SubscribeOrdersResponse(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderState]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderState, _Mapping]]] = ...) -> None: ...

class SubscribeTradesRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class SubscribeTradesResponse(_message.Message):
    __slots__ = ("trades",)
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[_trade_pb2.AccountTrade]
    def __init__(self, trades: _Optional[_Iterable[_Union[_trade_pb2.AccountTrade, _Mapping]]] = ...) -> None: ...

class GetOrderRequest(_message.Message):
    __slots__ = ("account_id", "order_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    order_id: str
    def __init__(self, account_id: _Optional[str] = ..., order_id: _Optional[str] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("account_id", "symbol", "quantity", "side", "type", "time_in_force", "limit_price", "stop_price", "stop_condition", "legs", "client_order_id", "valid_before", "comment")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_IN_FORCE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    STOP_PRICE_FIELD_NUMBER: _ClassVar[int]
    STOP_CONDITION_FIELD_NUMBER: _ClassVar[int]
    LEGS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_BEFORE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    symbol: str
    quantity: _decimal_pb2.Decimal
    side: _side_pb2.Side
    type: OrderType
    time_in_force: TimeInForce
    limit_price: _decimal_pb2.Decimal
    stop_price: _decimal_pb2.Decimal
    stop_condition: StopCondition
    legs: _containers.RepeatedCompositeFieldContainer[Leg]
    client_order_id: str
    valid_before: ValidBefore
    comment: str
    def __init__(self, account_id: _Optional[str] = ..., symbol: _Optional[str] = ..., quantity: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., side: _Optional[_Union[_side_pb2.Side, str]] = ..., type: _Optional[_Union[OrderType, str]] = ..., time_in_force: _Optional[_Union[TimeInForce, str]] = ..., limit_price: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., stop_price: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., stop_condition: _Optional[_Union[StopCondition, str]] = ..., legs: _Optional[_Iterable[_Union[Leg, _Mapping]]] = ..., client_order_id: _Optional[str] = ..., valid_before: _Optional[_Union[ValidBefore, str]] = ..., comment: _Optional[str] = ...) -> None: ...

class Leg(_message.Message):
    __slots__ = ("symbol", "quantity", "side")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    quantity: _decimal_pb2.Decimal
    side: _side_pb2.Side
    def __init__(self, symbol: _Optional[str] = ..., quantity: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., side: _Optional[_Union[_side_pb2.Side, str]] = ...) -> None: ...

class OrderState(_message.Message):
    __slots__ = ("order_id", "exec_id", "status", "order", "transact_at", "accept_at", "withdraw_at", "initial_quantity", "executed_quantity", "remaining_quantity", "sltp_order", "triggered_order_id")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    TRANSACT_AT_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_AT_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_AT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    REMAINING_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SLTP_ORDER_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    exec_id: str
    status: OrderStatus
    order: Order
    transact_at: _timestamp_pb2.Timestamp
    accept_at: _timestamp_pb2.Timestamp
    withdraw_at: _timestamp_pb2.Timestamp
    initial_quantity: _decimal_pb2.Decimal
    executed_quantity: _decimal_pb2.Decimal
    remaining_quantity: _decimal_pb2.Decimal
    sltp_order: SLTPOrder
    triggered_order_id: str
    def __init__(self, order_id: _Optional[str] = ..., exec_id: _Optional[str] = ..., status: _Optional[_Union[OrderStatus, str]] = ..., order: _Optional[_Union[Order, _Mapping]] = ..., transact_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., accept_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., withdraw_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., initial_quantity: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., executed_quantity: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., remaining_quantity: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., sltp_order: _Optional[_Union[SLTPOrder, _Mapping]] = ..., triggered_order_id: _Optional[str] = ...) -> None: ...

class OrdersRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class OrdersResponse(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderState]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderState, _Mapping]]] = ...) -> None: ...

class CancelOrderRequest(_message.Message):
    __slots__ = ("account_id", "order_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    order_id: str
    def __init__(self, account_id: _Optional[str] = ..., order_id: _Optional[str] = ...) -> None: ...

class SLTPOrder(_message.Message):
    __slots__ = ("account_id", "symbol", "side", "quantity_sl", "sl_price", "limit_price", "quantity_tp", "tp_price", "tp_guard_spread", "tp_spread_measure", "client_order_id", "valid_before", "valid_expiry_time", "comment")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SL_FIELD_NUMBER: _ClassVar[int]
    SL_PRICE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_TP_FIELD_NUMBER: _ClassVar[int]
    TP_PRICE_FIELD_NUMBER: _ClassVar[int]
    TP_GUARD_SPREAD_FIELD_NUMBER: _ClassVar[int]
    TP_SPREAD_MEASURE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_BEFORE_FIELD_NUMBER: _ClassVar[int]
    VALID_EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    symbol: str
    side: _side_pb2.Side
    quantity_sl: _decimal_pb2.Decimal
    sl_price: _decimal_pb2.Decimal
    limit_price: _decimal_pb2.Decimal
    quantity_tp: _decimal_pb2.Decimal
    tp_price: _decimal_pb2.Decimal
    tp_guard_spread: _decimal_pb2.Decimal
    tp_spread_measure: TPSpreadMeasure
    client_order_id: str
    valid_before: ValidBefore
    valid_expiry_time: _timestamp_pb2.Timestamp
    comment: str
    def __init__(self, account_id: _Optional[str] = ..., symbol: _Optional[str] = ..., side: _Optional[_Union[_side_pb2.Side, str]] = ..., quantity_sl: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., sl_price: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., limit_price: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., quantity_tp: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., tp_price: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., tp_guard_spread: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., tp_spread_measure: _Optional[_Union[TPSpreadMeasure, str]] = ..., client_order_id: _Optional[str] = ..., valid_before: _Optional[_Union[ValidBefore, str]] = ..., valid_expiry_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., comment: _Optional[str] = ...) -> None: ...
