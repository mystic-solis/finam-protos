import sys
from pathlib import Path
from grpc_tools import protoc
from loguru import logger
import grpc_tools
import urllib.request
import zipfile
import io
import shutil


SRC_DIR = Path("./protos")  # папка с proto
DST_DIR = Path(__file__).parent / "."  # куда генерировать
DST_DIR.mkdir(exist_ok=True)

# Путь к встроенным Google proto (timestamp.proto и др.)
PROTO_INCLUDE = Path(grpc_tools.__path__[0]) / "_proto"

# Путь для сторонних (third-party) proto, например google/type/decimal.proto
THIRD_PARTY_DIR = Path(__file__).parent / ".." / "proto_third_party"


def fetch_third_party_proto(rel_path: str, url: str) -> bool:
    """Download a single third-party proto if missing. Returns True if downloaded."""
    dst = THIRD_PARTY_DIR / rel_path
    if dst.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    logger.info(f"Скачиваю сторонний proto: {rel_path}...")
    try:
        with urllib.request.urlopen(url) as resp, open(dst, "wb") as out_file:
            out_file.write(resp.read())
        logger.info(f"✅ Скачан {rel_path}")
        return True
    except Exception as e:
        logger.error(f"Не удалось скачать {url}: {e}")
        raise


def download_googleapis_google_tree_if_needed() -> bool:
    """Download googleapis master zip and extract google/ subtree if required.
    Returns True if anything was downloaded/extracted.
    """
    GOOGLE_API_ZIP_URL = "https://github.com/googleapis/googleapis/archive/refs/heads/master.zip"
    required_google_files = [
        THIRD_PARTY_DIR / "google" / "api" / "annotations.proto",
        THIRD_PARTY_DIR / "google" / "type" / "money.proto",
        THIRD_PARTY_DIR / "google" / "type" / "interval.proto",
    ]
    need_download = any(not p.exists() for p in required_google_files)
    if not need_download:
        return False

    logger.info("Скачиваю googleapis (только google/)... Это может занять несколько секунд...")
    try:
        THIRD_PARTY_DIR.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(GOOGLE_API_ZIP_URL) as resp:
            data = resp.read()
        z = zipfile.ZipFile(io.BytesIO(data))
        members = [m for m in z.namelist() if m.startswith("googleapis-master/google/")]
        for m in members:
            relative_path = Path(m).relative_to("googleapis-master")
            target_path = THIRD_PARTY_DIR / relative_path
            if m.endswith('/'):
                target_path.mkdir(parents=True, exist_ok=True)
            else:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                with z.open(m) as src, open(target_path, "wb") as dst:
                    shutil.copyfileobj(src, dst)
        logger.info("✅ googleapis (google/) скачан")
        return True
    except Exception as e:
        logger.warning(f"Не удалось скачать googleapis repository: {e}")
        return False


def generate_protos() -> None:
    proto_files = list(SRC_DIR.glob("**/*.proto"))
    if not proto_files:
        logger.error("❌ .proto файлы не найдены!")
        sys.exit(1)

    logger.info(f"Найдено: {len(proto_files)} `.proto` файлов")

    for proto_file in proto_files:
        protoc_args = [
            "protoc",
            f"-I{SRC_DIR}",            # твои proto
            f"-I{PROTO_INCLUDE}",      # встроенные Google proto (google/protobuf/...)
            f"-I{THIRD_PARTY_DIR}",    # сторонние proto (google/type/...)
            f"--python_out={DST_DIR}",
            f"--grpc_python_out={DST_DIR}",
            f"--pyi_out={DST_DIR}",  # для создания файлов .pyi для подсказок
            str(proto_file)
        ]
        if protoc.main(protoc_args) != 0:
            logger.error(f"❌ Ошибка генерации {proto_file.name}")
            raise SystemExit(1)
        logger.info(f"✅ Сгенерированно {proto_file.name}...")


def main() -> None:
    # CLI flag: --keep-deps to preserve downloaded third-party protos
    keep_deps = "--keep-deps" in sys.argv

    # Track whether we downloaded/extracted third-party protos in this run
    created_third_party = False

    # Ensure decimal.proto (a common dependency) is present
    DECIMAL_REL = Path("google") / "type" / "decimal.proto"
    DECIMAL_RAW_URL = (
        "https://raw.githubusercontent.com/googleapis/googleapis/master/google/type/decimal.proto"
    )
    try:
        if fetch_third_party_proto(str(DECIMAL_REL), DECIMAL_RAW_URL):
            created_third_party = True
    except Exception:
        logger.warning("Не удалось получить decimal.proto автоматически; проверьте соединение или добавьте файл вручную.")

    # Download google/ subtree if key files are missing
    try:
        if download_googleapis_google_tree_if_needed():
            created_third_party = True
    except Exception:
        logger.warning("Не удалось скачать googleapis google/ subtree.")

    try:
        generate_protos()
        logger.success(f"🎉 Генерация завершена! Файлы в {DST_DIR}")
    finally:
        # Cleanup downloaded third-party files unless user requested to keep them
        if created_third_party and not keep_deps and THIRD_PARTY_DIR.exists():
            try:
                shutil.rmtree(THIRD_PARTY_DIR)
                logger.info("Временные скачанные зависимости удалены [proto_third_party]")
            except Exception as e:
                logger.warning(f"Не удалось удалить {THIRD_PARTY_DIR}: {e}")


if __name__ == "__main__":
    main()
