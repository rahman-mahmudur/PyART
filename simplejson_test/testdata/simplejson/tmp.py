from __future__ import absolute_import
__version__ = '3.17.2'
__all__ = [
    'dump', 'dumps', 'load', 'loads',
    'JSONDecoder', 'JSONDecodeError', 'JSONEncoder',
    'OrderedDict', 'simple_first', 'RawJSON'
]

__author__ = 'Bob Ippolito <bob@redivi.com>'

from decimal import Decimal

from .errors import JSONDecodeError
from .raw_json import RawJSON
from .decoder import JSONDecoder
from .encoder import JSONEncoder, JSONEncoderForHTML
def _import_OrderedDict():
    import collections
    try:
        return collections.OrderedDict
    except AttributeError:
        from . import ordered_dict
        return ordered_dict.OrderedDict
OrderedDict = _import_OrderedDict()

def _import_c_make_encoder():
    try:
        from ._speedups import make_encoder
        return make_encoder
    except ImportError:
        return None

_default_encoder = JSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    encoding='utf-8',
    default=None,
    use_decimal=True,
    namedtuple_as_object=True,
    tuple_as_array=True,
    iterable_as_array=False,
    bigint_as_string=False,
    item_sort_key=None,
    for_json=False,
    ignore_nan=False,
    int_as_string_bitcount=None,
)

def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
         allow_nan=True, cls=None, indent=None, separators=None,
         encoding='utf-8', default=None, use_decimal=True,
         namedtuple_as_object=True, tuple_as_array=True,
         bigint_as_string=False, sort_keys=False, item_sort_key=None,
         for_json=False, ignore_nan=False, int_as_string_bitcount=None,
         iterable_as_array=False, **kw):
    if (not skipkeys and ensure_ascii and
        check_circular and allow_nan and
        cls is None and indent is None and separators is None and
        encoding == 'utf-8' and default is None and use_decimal
        and namedtuple_as_object and tuple_as_array and not iterable_as_array
        and not bigint_as_string and not sort_keys
        and not item_sort_key and not for_json
        and not ignore_nan and int_as_string_bitcount is None
        and not kw
    ):
    else:
        if cls is None:
            cls = JSONEncoder
        iterable = cls(skipkeys=skipkeys, ensure_ascii=ensure_ascii,
            check_circular=check_circular, allow_nan=allow_nan, indent=indent,
            separators=separators, encoding=encoding,
            default=default, use_decimal=use_decimal,
            namedtuple_as_object=namedtuple_as_object,
            tuple_as_array=tuple_as_array,
            iterable_as_array=iterable_as_array,
            bigint_as_string=bigint_as_string,
            sort_keys=sort_keys,
            item_sort_key=item_sort_key,
            for_json=for_json,
            ignore_nan=ignore_nan,
            int_as_string_bitcount=int_as_string_bitcount,
            **kw).iterencode(obj)
    for chunk in iterable:


def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
          allow_nan=True, cls=None, indent=None, separators=None,
          encoding='utf-8', default=None, use_decimal=True,
          namedtuple_as_object=True, tuple_as_array=True,
          bigint_as_string=False, sort_keys=False, item_sort_key=None,
          for_json=False, ignore_nan=False, int_as_string_bitcount=None,
          iterable_as_array=False, **kw):
    if (not skipkeys and ensure_ascii and
        check_circular and allow_nan and
        cls is None and indent is None and separators is None and
        encoding == 'utf-8' and default is None and use_decimal
        and namedtuple_as_object and tuple_as_array and not iterable_as_array
        and not bigint_as_string and not sort_keys
        and not item_sort_key and not for_json
        and not ignore_nan and int_as_string_bitcount is None
        and not kw
    ):
    if cls is None:
        cls = JSONEncoder
    return cls(
        skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        separators=separators, encoding=encoding, default=default,
        use_decimal=use_decimal,
        namedtuple_as_object=namedtuple_as_object,
        tuple_as_array=tuple_as_array,
        iterable_as_array=iterable_as_array,
        bigint_as_string=bigint_as_string,
        sort_keys=sort_keys,
        item_sort_key=item_sort_key,
        for_json=for_json,
        ignore_nan=ignore_nan,
        int_as_string_bitcount=int_as_string_bitcount,
        **kw).encode(obj)


_default_decoder = JSONDecoder(encoding=None, object_hook=None,
                               object_pairs_hook=None)


def load(fp, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None,
        use_decimal=False, namedtuple_as_object=True, tuple_as_array=True,
        **kw):
    return loads(fp.read(),
        encoding=encoding, cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook,
        use_decimal=use_decimal, **kw)


def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None,
        use_decimal=False, **kw):
    if (cls is None and encoding is None and object_hook is None and
            parse_int is None and parse_float is None and
            parse_constant is None and object_pairs_hook is None
            and not use_decimal and not kw):
        reveal_type(_default_decoder)