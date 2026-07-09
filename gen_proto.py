import sys
from pathlib import Path
from grpc_tools import protoc
import grpc_tools
import logging

SRC_DIR = Path("./proto")                     # папка с вашими proto (включая google/ и grpc/)
DST_DIR = Path(__file__).parent / "finam_protos"  # куда генерировать
DST_DIR.mkdir(exist_ok=True)

# Встроенные Google proto (timestamp.proto и др.) из grpc_tools
PROTO_INCLUDE = Path(grpc_tools.__path__[0]) / "_proto"


def generate_protos() -> None:
    proto_files = list(SRC_DIR.glob("**/*.proto"))
    if not proto_files:
        logging.error("❌ .proto файлы не найдены!")
        sys.exit(1)

    logging.info(f"Найдено: {len(proto_files)} `.proto` файлов")

    for proto_file in proto_files:
        protoc_args = [
            "protoc",
            f"-I{SRC_DIR}",            # ваши proto (включая google/ и grpc/)
            f"-I{PROTO_INCLUDE}",      # встроенные Google proto (protobuf)
            f"--python_out={DST_DIR}",
            f"--grpc_python_out={DST_DIR}",
            f"--pyi_out={DST_DIR}",    # для создания файлов .pyi для подсказок
            str(proto_file)
        ]
        if protoc.main(protoc_args) != 0:
            logging.error(f"❌ Ошибка генерации {proto_file.name}")
            raise SystemExit(1)
        logging.info(f"✅ Сгенерирован {proto_file.name}")

    # Создаём __init__.py во всех папках
    for folder in DST_DIR.rglob("*"):
        if folder.is_dir():
            init_file = folder / "__init__.py"
            if not init_file.exists():
                init_file.touch()
                logging.info(f"Создан {init_file}")


def main() -> None:
    generate_protos()
    logging.info(f"🎉 Генерация завершена! Файлы в {DST_DIR}")


if __name__ == "__main__":
    main()
