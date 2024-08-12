# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('netbox')


class _ExportableConfig(types.ModuleType):
    @property
    def allow_insecure_https(self) -> Optional[bool]:
        """
        Flag to set whether to allow https with invalid certificates. Can be set via the `NETBOX_ALLOW_INSECURE_HTTPS`
        environment variable. Defaults to `false`.
        """
        return __config__.get_bool('allowInsecureHttps')

    @property
    def api_token(self) -> Optional[str]:
        """
        Netbox API authentication token. Can be set via the `NETBOX_API_TOKEN` environment variable.
        """
        return __config__.get('apiToken')

    @property
    def headers(self) -> Optional[str]:
        """
        Set these header on all requests to Netbox. Can be set via the `NETBOX_HEADERS` environment variable.
        """
        return __config__.get('headers')

    @property
    def request_timeout(self) -> Optional[int]:
        """
        Netbox API HTTP request timeout in seconds. Can be set via the `NETBOX_REQUEST_TIMEOUT` environment variable.
        """
        return __config__.get_int('requestTimeout')

    @property
    def server_url(self) -> Optional[str]:
        """
        Location of Netbox server including scheme (http or https) and optional port. Can be set via the `NETBOX_SERVER_URL`
        environment variable.
        """
        return __config__.get('serverUrl')

    @property
    def skip_version_check(self) -> Optional[bool]:
        return __config__.get_bool('skipVersionCheck')

    @property
    def strip_trailing_slashes_from_url(self) -> Optional[bool]:
        """
        If true, strip trailing slashes from the `server_url` parameter and print a warning when doing so. Note that using
        trailing slashes in the `server_url` parameter will usually lead to errors. Can be set via the
        `NETBOX_STRIP_TRAILING_SLASHES_FROM_URL` environment variable. Defaults to `true`.
        """
        return __config__.get_bool('stripTrailingSlashesFromUrl')

