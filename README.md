
Генерируем файлы протобафа
uv run .\generate_proto_files.py

Билдим пакет
uv build

Устанавливаем wheel
uv pip install dist/finam_grpc-1.0.0-py3-none-any.whl

В оригинальные протофайлы добавлена папка finam_grpc, чтобы пофиксить ошибку расположения grpc вне корня проекта и перезаписи базовой библиотеки grpc
