import logging
import pkg_resources
from functools import partial

from cornice.errors import Errors  # NOQA
from cornice.renderer import CorniceRenderer
from cornice.service import Service   # NOQA
from cornice.pyramidhook import (
    wrap_request,
    register_service_views,
    handle_exceptions,
    register_resource_views,
)
from cornice.util import ContentTypePredicate, current_service
from pyramid.events import NewRequest
from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.settings import aslist, asbool


logger = logging.getLogger('cornice')
__version__ = pkg_resources.get_distribution(__package__).version


def set_localizer_for_languages(event, available_languages,
                                default_locale_name):
    request = event.request
    if request.accept_language:
        accepted = request.accept_language.lookup(available_languages,
                                                  default=default_locale_name)
        request._LOCALE_ = accepted


def setup_localization(config):
    try:
        config.add_translation_dirs('colander:locale/')
        settings = config.get_settings()
        available_languages = aslist(settings['available_languages'])
        set_localizer = partial(set_localizer_for_languages,
                                available_languages=available_languages,
                                default_locale_name=default_locale_name)
        config.add_subscriber(set_localizer, NewRequest)
    except ImportError:  # pragma: no cover
        pass


def includeme(config):
    config.registry.cornice_services = {}

    settings = config.get_settings()

    if settings.get('available_languages'):
        setup_localization(config)

    config.add_directive('add_cornice_service', register_service_views)
    config.add_directive('add_cornice_resource', register_resource_views)
    config.add_subscriber(wrap_request, NewRequest)
    config.add_renderer('cornicejson', CorniceRenderer())
    config.add_view_predicate('content_type', ContentTypePredicate)
    reveal_type(config)