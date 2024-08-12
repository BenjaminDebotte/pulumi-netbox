# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetRacksResult',
    'AwaitableGetRacksResult',
    'get_racks',
    'get_racks_output',
]

@pulumi.output_type
class GetRacksResult:
    """
    A collection of values returned by getRacks.
    """
    def __init__(__self__, filters=None, id=None, limit=None, racks=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if limit and not isinstance(limit, int):
            raise TypeError("Expected argument 'limit' to be a int")
        pulumi.set(__self__, "limit", limit)
        if racks and not isinstance(racks, list):
            raise TypeError("Expected argument 'racks' to be a list")
        pulumi.set(__self__, "racks", racks)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetRacksFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def limit(self) -> Optional[int]:
        """
        Defaults to `0`.
        """
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter
    def racks(self) -> Sequence['outputs.GetRacksRackResult']:
        return pulumi.get(self, "racks")


class AwaitableGetRacksResult(GetRacksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRacksResult(
            filters=self.filters,
            id=self.id,
            limit=self.limit,
            racks=self.racks)


def get_racks(filters: Optional[Sequence[Union['GetRacksFilterArgs', 'GetRacksFilterArgsDict']]] = None,
              limit: Optional[int] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRacksResult:
    """
    Use this data source to access information about an existing resource.

    :param int limit: Defaults to `0`.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['limit'] = limit
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('netbox:index/getRacks:getRacks', __args__, opts=opts, typ=GetRacksResult).value

    return AwaitableGetRacksResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        limit=pulumi.get(__ret__, 'limit'),
        racks=pulumi.get(__ret__, 'racks'))


@_utilities.lift_output_func(get_racks)
def get_racks_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetRacksFilterArgs', 'GetRacksFilterArgsDict']]]]] = None,
                     limit: Optional[pulumi.Input[Optional[int]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRacksResult]:
    """
    Use this data source to access information about an existing resource.

    :param int limit: Defaults to `0`.
    """
    ...
