# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetPrefixPrefixesAvailableResult',
]

@pulumi.output_type
class GetPrefixPrefixesAvailableResult(dict):
    def __init__(__self__, *,
                 family: int,
                 prefix: str,
                 vrf_id: int):
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "prefix", prefix)
        pulumi.set(__self__, "vrf_id", vrf_id)

    @property
    @pulumi.getter
    def family(self) -> int:
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def prefix(self) -> str:
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="vrfId")
    def vrf_id(self) -> int:
        return pulumi.get(self, "vrf_id")


