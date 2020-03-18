# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Kyle Hultman <kyle@gremlin.com>, Gremlin Inc <sales@gremlin.com>

import logging

from gremlinapi.cli import register_cli_action
from gremlinapi.exceptions import (
    GremlinParameterError,
    ProxyError,
    ClientError,
    HTTPTimeout,
    HTTPError
)

from gremlinapi.gremlinapi import GremlinAPI
from gremlinapi.http_clients import get_gremlin_httpclient


log = logging.getLogger('GremlinAPI.client')


class GremlinAPIContracts(GremlinAPI):

    @classmethod
    @register_cli_action('update_contract', ('identifier', 'body'), ('',))
    def update_contract(cls, https_client=get_gremlin_httpclient(), **kwargs):
        method = 'PATCH'
        identifier = cls._error_if_not_identifier(**kwargs)
        data = cls._error_if_not_body(**kwargs)
        endpoint = f'/companies/{identifier}/contracts/current'
        headers = https_client.header()
        (resp, body) = https_client.api_call(method, endpoint, **{'body': data, 'headers': headers})
        return body