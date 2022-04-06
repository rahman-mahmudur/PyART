from __future__ import unicode_literals

import os
import sys
import six
import copy
import time
import json
import logging
import traceback
import functools
import threading
import tornado.ioloop
import tornado.httputil
import tornado.httpclient
import pyspider

from six.moves import queue, http_cookies
from six.moves.urllib.robotparser import RobotFileParser
from requests import cookies
from six.moves.urllib.parse import urljoin, urlsplit
from tornado import gen
from tornado.curl_httpclient import CurlAsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient

from pyspider.libs import utils, dataurl, counter
from pyspider.libs.url import quote_chinese
from .cookie_utils import extract_cookies_to_jar
logger = logging.getLogger('fetcher')


class MyCurlAsyncHTTPClient(CurlAsyncHTTPClient):

    def free_size(self):
        return len(self._free_list)

    def size(self):
        return len(self._curls) - self.free_size()


class MySimpleAsyncHTTPClient(SimpleAsyncHTTPClient):

    def free_size(self):
        return self.max_clients - self.size()

    def size(self):
        return len(self.active)

fetcher_output = {
    "status_code": int,
    "orig_url": str,
    "url": str,
    "headers": dict,
    "content": str,
    "cookies": dict,
}


class Fetcher(object):
    user_agent = "pyspider/%s (+http://pyspider.org/)" % pyspider.__version__
    default_options = {
        'method': 'GET',
        'headers': {
        },
        'use_gzip': True,
        'timeout': 120,
        'connect_timeout': 20,
    }
    phantomjs_proxy = None
    splash_endpoint = None
    splash_lua_source = open(os.path.join(os.path.dirname(__file__), "splash_fetcher.lua")).read()
    robot_txt_age = 60*60  # 1h

    def __init__(self, inqueue, outqueue, poolsize=100, proxy=None, async_mode=True):
        self.inqueue = inqueue
        self.outqueue = outqueue

        self.poolsize = poolsize
        self._running = False
        self._quit = False
        self.proxy = proxy
        self.async_mode = async_mode
        self.ioloop = tornado.ioloop.IOLoop()

        self.robots_txt_cache = {}

        if self.async_mode:
            self.http_client = MyCurlAsyncHTTPClient(max_clients=self.poolsize,
                                                     io_loop=self.ioloop)
        else:
            self.http_client = tornado.httpclient.HTTPClient(MyCurlAsyncHTTPClient, max_clients=self.poolsize)

        self._cnt = {
            '5m': counter.CounterManager(
                lambda: counter.TimebaseAverageWindowCounter(30, 10)),
            '1h': counter.CounterManager(
                lambda: counter.TimebaseAverageWindowCounter(60, 60)),
        }

    def send_result(self, type, task, result):
        if self.outqueue:
            try:
            except Exception as e:

    def fetch(self, task, callback=None):
        if self.async_mode:
            return self.async_fetch(task, callback)
        else:
            return self.async_fetch(task, callback).result()

    @gen.coroutine
    def async_fetch(self, task, callback=None):
        if callback is None:
            callback = self.send_result

        type = 'None'
        try:
                type = 'data'
            elif task.get('fetch', {}).get('fetch_type') in ('js', 'phantomjs'):
                type = 'phantomjs'
                result = yield self.phantomjs_fetch(url, task)
            elif task.get('fetch', {}).get('fetch_type') in ('splash', ):
                type = 'splash'
                result = yield self.splash_fetch(url, task)
            elif task.get('fetch', {}).get('fetch_type') in ('puppeteer', ):
                type = 'puppeteer'
                result = yield self.puppeteer_fetch(url, task)
            else:
                type = 'http'
                result = yield self.http_fetch(url, task)
        except Exception as e:
            logger.exception(e)
            result = self.handle_error(type, url, task, start_time, e)

        callback(type, task, result)
        raise gen.Return(result)

    def sync_fetch(self, task):
        if not self._running:
            return self.ioloop.run_sync(functools.partial(self.async_fetch, task, lambda t, _, r: True))

        wait_result = threading.Condition()
        _result = {}

        def callback(type, task, result):
            _result['type'] = type
            _result['task'] = task
            _result['result'] = result
            wait_result.notify()

        wait_result.acquire()
        while 'result' not in _result:
        wait_result.release()
        return _result['result']

    def data_fetch(self, url, task):
        self.on_fetch('data', task)
        result = {}
        result['orig_url'] = url
        result['headers'] = {}
        result['status_code'] = 200
        result['url'] = url
        result['cookies'] = {}
        result['time'] = 0
        result['save'] = task.get('fetch', {}).get('save')
        if len(result['content']) < 70:
        else:
            logger.info(
                "[200] %s:%s data:,%s...[content:%d] 0s",
                task.get('project'), task.get('taskid'),
                result['content'][:70],
                len(result['content'])
            )

        return result

    def handle_error(self, type, url, task, start_time, error):
        result = {
            'status_code': getattr(error, 'code', 599)}
        reveal_type(traceback)