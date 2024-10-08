# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TypeArgs', 'Type']

@pulumi.input_type
class TypeArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Type resource.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)


@pulumi.input_type
class _TypeState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Type resources.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)


class Type(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/features/virtualization/#cluster-types):

        > A cluster type represents a technology or mechanism by which a cluster is formed. For example, you might create a cluster type named "VMware vSphere" for a locally hosted cluster or "DigitalOcean NYC3" for one hosted by a cloud provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        vmw_vsphere = netbox.cluster.Type("vmwVsphere")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TypeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/features/virtualization/#cluster-types):

        > A cluster type represents a technology or mechanism by which a cluster is formed. For example, you might create a cluster type named "VMware vSphere" for a locally hosted cluster or "DigitalOcean NYC3" for one hosted by a cloud provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        vmw_vsphere = netbox.cluster.Type("vmwVsphere")
        ```

        :param str resource_name: The name of the resource.
        :param TypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TypeArgs.__new__(TypeArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["slug"] = slug
        super(Type, __self__).__init__(
            'netbox:cluster/type:Type',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None) -> 'Type':
        """
        Get an existing Type resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TypeState.__new__(_TypeState)

        __props__.__dict__["name"] = name
        __props__.__dict__["slug"] = slug
        return Type(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug")

