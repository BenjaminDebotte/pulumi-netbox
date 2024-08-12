# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['IpArgs', 'Ip']

@pulumi.input_type
class IpArgs:
    def __init__(__self__, *,
                 device_id: pulumi.Input[int],
                 ip_address_id: pulumi.Input[int],
                 ip_address_version: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Ip resource.
        :param pulumi.Input[int] ip_address_version: Defaults to `4`.
        """
        pulumi.set(__self__, "device_id", device_id)
        pulumi.set(__self__, "ip_address_id", ip_address_id)
        if ip_address_version is not None:
            pulumi.set(__self__, "ip_address_version", ip_address_version)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter(name="ipAddressId")
    def ip_address_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "ip_address_id")

    @ip_address_id.setter
    def ip_address_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "ip_address_id", value)

    @property
    @pulumi.getter(name="ipAddressVersion")
    def ip_address_version(self) -> Optional[pulumi.Input[int]]:
        """
        Defaults to `4`.
        """
        return pulumi.get(self, "ip_address_version")

    @ip_address_version.setter
    def ip_address_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ip_address_version", value)


@pulumi.input_type
class _IpState:
    def __init__(__self__, *,
                 device_id: Optional[pulumi.Input[int]] = None,
                 ip_address_id: Optional[pulumi.Input[int]] = None,
                 ip_address_version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Ip resources.
        :param pulumi.Input[int] ip_address_version: Defaults to `4`.
        """
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if ip_address_id is not None:
            pulumi.set(__self__, "ip_address_id", ip_address_id)
        if ip_address_version is not None:
            pulumi.set(__self__, "ip_address_version", ip_address_version)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter(name="ipAddressId")
    def ip_address_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ip_address_id")

    @ip_address_id.setter
    def ip_address_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ip_address_id", value)

    @property
    @pulumi.getter(name="ipAddressVersion")
    def ip_address_version(self) -> Optional[pulumi.Input[int]]:
        """
        Defaults to `4`.
        """
        return pulumi.get(self, "ip_address_version")

    @ip_address_version.setter
    def ip_address_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ip_address_version", value)


class Ip(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 ip_address_id: Optional[pulumi.Input[int]] = None,
                 ip_address_version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        This resource is used to define the primary IP for a given device. The primary IP is reflected in the device Netbox UI, which identifies the Primary IPv4 and IPv6 addresses.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test = netbox.Device("test",
            device_type_id=netbox_device_type["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_v4_address = netbox.ip.Address("testV4Address",
            ip_address="1.1.1.1/32",
            status="active",
            device_interface_id=netbox_device_interface["test"]["id"])
        test_v4_ip = netbox.device.primary.Ip("testV4Ip",
            device_id=test.id,
            ip_address_id=netbox_ip_address["test"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] ip_address_version: Defaults to `4`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource is used to define the primary IP for a given device. The primary IP is reflected in the device Netbox UI, which identifies the Primary IPv4 and IPv6 addresses.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test = netbox.Device("test",
            device_type_id=netbox_device_type["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_v4_address = netbox.ip.Address("testV4Address",
            ip_address="1.1.1.1/32",
            status="active",
            device_interface_id=netbox_device_interface["test"]["id"])
        test_v4_ip = netbox.device.primary.Ip("testV4Ip",
            device_id=test.id,
            ip_address_id=netbox_ip_address["test"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param IpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 ip_address_id: Optional[pulumi.Input[int]] = None,
                 ip_address_version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpArgs.__new__(IpArgs)

            if device_id is None and not opts.urn:
                raise TypeError("Missing required property 'device_id'")
            __props__.__dict__["device_id"] = device_id
            if ip_address_id is None and not opts.urn:
                raise TypeError("Missing required property 'ip_address_id'")
            __props__.__dict__["ip_address_id"] = ip_address_id
            __props__.__dict__["ip_address_version"] = ip_address_version
        super(Ip, __self__).__init__(
            'netbox:device/primary/ip:Ip',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            device_id: Optional[pulumi.Input[int]] = None,
            ip_address_id: Optional[pulumi.Input[int]] = None,
            ip_address_version: Optional[pulumi.Input[int]] = None) -> 'Ip':
        """
        Get an existing Ip resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] ip_address_version: Defaults to `4`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IpState.__new__(_IpState)

        __props__.__dict__["device_id"] = device_id
        __props__.__dict__["ip_address_id"] = ip_address_id
        __props__.__dict__["ip_address_version"] = ip_address_version
        return Ip(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="ipAddressId")
    def ip_address_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "ip_address_id")

    @property
    @pulumi.getter(name="ipAddressVersion")
    def ip_address_version(self) -> pulumi.Output[Optional[int]]:
        """
        Defaults to `4`.
        """
        return pulumi.get(self, "ip_address_version")

