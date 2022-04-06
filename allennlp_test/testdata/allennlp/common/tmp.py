import importlib
import logging
import os
from typing import Iterable

from allennlp.common.util import push_python_path, import_module_and_submodules

logger = logging.getLogger(__name__)


DEFAULT_PLUGINS = ("allennlp_models", "allennlp_server")


def discover_file_plugins(plugins_filename: str = ".allennlp_plugins") -> Iterable[str]:
    if os.path.isfile(plugins_filename):
        with open(plugins_filename) as file_:
            for module_name in file_.readlines():
                if module_name:
                    yield module_name
    else:
        return []


def discover_plugins() -> Iterable[str]:
    with push_python_path("."):
        yield from discover_file_plugins()


def import_plugins() -> None:
    for module_name in DEFAULT_PLUGINS:
        try:
            import_module_and_submodules(module_name)
            reveal_type(logger)
        except Exception:
        	pass