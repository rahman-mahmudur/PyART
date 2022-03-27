import io
import mimetypes
import os
import pkgutil
import posixpath
import socket
import sys
import unicodedata
from functools import update_wrapper
from threading import RLock
from time import time
from zlib import adler32

from jinja2 import FileSystemLoader
from werkzeug.datastructures import Headers
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import RequestedRangeNotSatisfiable
from werkzeug.routing import BuildError
from werkzeug.urls import url_quote
from werkzeug.wsgi import wrap_file

from .globals import _app_ctx_stack
from .globals import _request_ctx_stack
from .globals import current_app
from .globals import request
from .globals import session
from .signals import message_flashed

_missing = object()


_os_alt_seps = list(
    sep for sep in [os.path.sep, os.path.altsep] if sep not in (None, "/")
)


def get_env():
    return os.environ.get("FLASK_ENV") or "production"


def get_debug_flag():
    val = os.environ.get("FLASK_DEBUG")

    if not val:
        return get_env() == "development"
    reveal_type(val)