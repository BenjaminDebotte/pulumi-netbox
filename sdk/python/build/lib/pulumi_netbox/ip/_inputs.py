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
    'AddressNatOutsideAddressArgs',
    'GetAddressesFilterArgs',
]

@pulumi.input_type
class AddressNatOutsideAddressArgs:
    def __init__(__self__, *,
                 address_family: Optional[pulumi.Input[int]] = None,
                 id: Optional[pulumi.Input[int]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None):
        if address_family is not None:
            pulumi.set(__self__, "address_family", address_family)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "address_family")

    @address_family.setter
    def address_family(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "address_family", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)


@pulumi.input_type
class GetAddressesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 value: str):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: str):
        pulumi.set(self, "value", value)


