# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetVrfResult',
    'AwaitableGetVrfResult',
    'get_vrf',
    'get_vrf_output',
]

@pulumi.output_type
class GetVrfResult:
    """
    A collection of values returned by getVrf.
    """
    def __init__(__self__, id=None, name=None, tenant_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tenant_id and not isinstance(tenant_id, int):
            raise TypeError("Expected argument 'tenant_id' to be a int")
        pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[int]:
        return pulumi.get(self, "tenant_id")


class AwaitableGetVrfResult(GetVrfResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVrfResult(
            id=self.id,
            name=self.name,
            tenant_id=self.tenant_id)


def get_vrf(name: Optional[str] = None,
            tenant_id: Optional[int] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVrfResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_netbox as netbox

    cust_a_prod = netbox.get_vrf(name="cust-a-prod")
    ```
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tenantId'] = tenant_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('netbox:index/getVrf:getVrf', __args__, opts=opts, typ=GetVrfResult).value

    return AwaitableGetVrfResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'))


@_utilities.lift_output_func(get_vrf)
def get_vrf_output(name: Optional[pulumi.Input[str]] = None,
                   tenant_id: Optional[pulumi.Input[Optional[int]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVrfResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_netbox as netbox

    cust_a_prod = netbox.get_vrf(name="cust-a-prod")
    ```
    """
    ...
