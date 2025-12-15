
Генерируем файлы протобафа
uv run .\generate_proto_files.py

Билдим пакет
uv build

Устанавливаем wheel
uv pip install dist/finam_grpc-1.0.0-py3-none-any.whl

В оригинальные протофайлы добавлена папка finam_grpc, чтобы пофиксить ошибку расположения grpc вне корня проекта и перезаписи базовой библиотеки grpc
То есть: `grpc.tradeapi.v1` -> `finam_protos.grpc.tradeapi.v1`

Флаг при генерации `--grpc_python_out` генерирует gRPC-stubs, которые могут работать как синхронно, так и асинхронно.
Асинхронность появляется только если использовать grpc.aio.Channel во время выполнения.
