# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['PortArgs', 'Port']

@pulumi.input_type
class PortArgs:
    def __init__(__self__, *,
                 device_id: pulumi.Input[int],
                 positions: pulumi.Input[int],
                 type: pulumi.Input[str],
                 color_hex: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mark_connected: Optional[pulumi.Input[bool]] = None,
                 module_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Port resource.
        :param pulumi.Input[str] type: One of [8p8c, 8p6c, 8p4c, 8p2c, 6p6c, 6p4c, 6p2c, 4p4c, 4p2c, gg45, tera-4p, tera-2p, tera-1p, 110-punch, bnc, f, n, mrj21, fc, lc, lc-pc, lc-upc, lc-apc, lsh, lsh-pc, lsh-upc, lsh-apc, mpo, mtrj, sc, sc-pc, sc-upc, sc-apc, st, cs, sn, sma-905, sma-906, urm-p2, urm-p4, urm-p8, splice, other].
        :param pulumi.Input[bool] mark_connected: Defaults to `false`.
        """
        pulumi.set(__self__, "device_id", device_id)
        pulumi.set(__self__, "positions", positions)
        pulumi.set(__self__, "type", type)
        if color_hex is not None:
            pulumi.set(__self__, "color_hex", color_hex)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if mark_connected is not None:
            pulumi.set(__self__, "mark_connected", mark_connected)
        if module_id is not None:
            pulumi.set(__self__, "module_id", module_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter
    def positions(self) -> pulumi.Input[int]:
        return pulumi.get(self, "positions")

    @positions.setter
    def positions(self, value: pulumi.Input[int]):
        pulumi.set(self, "positions", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        One of [8p8c, 8p6c, 8p4c, 8p2c, 6p6c, 6p4c, 6p2c, 4p4c, 4p2c, gg45, tera-4p, tera-2p, tera-1p, 110-punch, bnc, f, n, mrj21, fc, lc, lc-pc, lc-upc, lc-apc, lsh, lsh-pc, lsh-upc, lsh-apc, mpo, mtrj, sc, sc-pc, sc-upc, sc-apc, st, cs, sn, sma-905, sma-906, urm-p2, urm-p4, urm-p8, splice, other].
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "color_hex")

    @color_hex.setter
    def color_hex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color_hex", value)

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_fields")

    @custom_fields.setter
    def custom_fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_fields", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="markConnected")
    def mark_connected(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "mark_connected")

    @mark_connected.setter
    def mark_connected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mark_connected", value)

    @property
    @pulumi.getter(name="moduleId")
    def module_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "module_id")

    @module_id.setter
    def module_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "module_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _PortState:
    def __init__(__self__, *,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mark_connected: Optional[pulumi.Input[bool]] = None,
                 module_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 positions: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Port resources.
        :param pulumi.Input[bool] mark_connected: Defaults to `false`.
        :param pulumi.Input[str] type: One of [8p8c, 8p6c, 8p4c, 8p2c, 6p6c, 6p4c, 6p2c, 4p4c, 4p2c, gg45, tera-4p, tera-2p, tera-1p, 110-punch, bnc, f, n, mrj21, fc, lc, lc-pc, lc-upc, lc-apc, lsh, lsh-pc, lsh-upc, lsh-apc, mpo, mtrj, sc, sc-pc, sc-upc, sc-apc, st, cs, sn, sma-905, sma-906, urm-p2, urm-p4, urm-p8, splice, other].
        """
        if color_hex is not None:
            pulumi.set(__self__, "color_hex", color_hex)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if mark_connected is not None:
            pulumi.set(__self__, "mark_connected", mark_connected)
        if module_id is not None:
            pulumi.set(__self__, "module_id", module_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if positions is not None:
            pulumi.set(__self__, "positions", positions)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "color_hex")

    @color_hex.setter
    def color_hex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color_hex", value)

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_fields")

    @custom_fields.setter
    def custom_fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_fields", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="markConnected")
    def mark_connected(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "mark_connected")

    @mark_connected.setter
    def mark_connected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mark_connected", value)

    @property
    @pulumi.getter(name="moduleId")
    def module_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "module_id")

    @module_id.setter
    def module_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "module_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def positions(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "positions")

    @positions.setter
    def positions(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "positions", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        One of [8p8c, 8p6c, 8p4c, 8p2c, 6p6c, 6p4c, 6p2c, 4p4c, 4p2c, gg45, tera-4p, tera-2p, tera-1p, 110-punch, bnc, f, n, mrj21, fc, lc, lc-pc, lc-upc, lc-apc, lsh, lsh-pc, lsh-upc, lsh-apc, mpo, mtrj, sc, sc-pc, sc-upc, sc-apc, st, cs, sn, sma-905, sma-906, urm-p2, urm-p4, urm-p8, splice, other].
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Port(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mark_connected: Optional[pulumi.Input[bool]] = None,
                 module_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 positions: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/rearport/):

        > Like front ports, rear ports are pass-through ports which represent the continuation of a path from one cable to the next. Each rear port is defined with its physical type and a number of positions: Rear ports with more than one position can be mapped to multiple front ports. This can be useful for modeling instances where multiple paths share a common cable (for example, six discrete two-strand fiber connections sharing a 12-strand MPO cable).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_port = netbox.device.rear.Port("testPort",
            device_id=test_device.id,
            type="8p8c",
            positions=2,
            mark_connected=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] mark_connected: Defaults to `false`.
        :param pulumi.Input[str] type: One of [8p8c, 8p6c, 8p4c, 8p2c, 6p6c, 6p4c, 6p2c, 4p4c, 4p2c, gg45, tera-4p, tera-2p, tera-1p, 110-punch, bnc, f, n, mrj21, fc, lc, lc-pc, lc-upc, lc-apc, lsh, lsh-pc, lsh-upc, lsh-apc, mpo, mtrj, sc, sc-pc, sc-upc, sc-apc, st, cs, sn, sma-905, sma-906, urm-p2, urm-p4, urm-p8, splice, other].
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PortArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/rearport/):

        > Like front ports, rear ports are pass-through ports which represent the continuation of a path from one cable to the next. Each rear port is defined with its physical type and a number of positions: Rear ports with more than one position can be mapped to multiple front ports. This can be useful for modeling instances where multiple paths share a common cable (for example, six discrete two-strand fiber connections sharing a 12-strand MPO cable).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_port = netbox.device.rear.Port("testPort",
            device_id=test_device.id,
            type="8p8c",
            positions=2,
            mark_connected=True)
        ```

        :param str resource_name: The name of the resource.
        :param PortArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PortArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mark_connected: Optional[pulumi.Input[bool]] = None,
                 module_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 positions: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PortArgs.__new__(PortArgs)

            __props__.__dict__["color_hex"] = color_hex
            __props__.__dict__["custom_fields"] = custom_fields
            __props__.__dict__["description"] = description
            if device_id is None and not opts.urn:
                raise TypeError("Missing required property 'device_id'")
            __props__.__dict__["device_id"] = device_id
            __props__.__dict__["label"] = label
            __props__.__dict__["mark_connected"] = mark_connected
            __props__.__dict__["module_id"] = module_id
            __props__.__dict__["name"] = name
            if positions is None and not opts.urn:
                raise TypeError("Missing required property 'positions'")
            __props__.__dict__["positions"] = positions
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(Port, __self__).__init__(
            'netbox:device/rear/port:Port',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            color_hex: Optional[pulumi.Input[str]] = None,
            custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            device_id: Optional[pulumi.Input[int]] = None,
            label: Optional[pulumi.Input[str]] = None,
            mark_connected: Optional[pulumi.Input[bool]] = None,
            module_id: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            positions: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Port':
        """
        Get an existing Port resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] mark_connected: Defaults to `false`.
        :param pulumi.Input[str] type: One of [8p8c, 8p6c, 8p4c, 8p2c, 6p6c, 6p4c, 6p2c, 4p4c, 4p2c, gg45, tera-4p, tera-2p, tera-1p, 110-punch, bnc, f, n, mrj21, fc, lc, lc-pc, lc-upc, lc-apc, lsh, lsh-pc, lsh-upc, lsh-apc, mpo, mtrj, sc, sc-pc, sc-upc, sc-apc, st, cs, sn, sma-905, sma-906, urm-p2, urm-p4, urm-p8, splice, other].
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PortState.__new__(_PortState)

        __props__.__dict__["color_hex"] = color_hex
        __props__.__dict__["custom_fields"] = custom_fields
        __props__.__dict__["description"] = description
        __props__.__dict__["device_id"] = device_id
        __props__.__dict__["label"] = label
        __props__.__dict__["mark_connected"] = mark_connected
        __props__.__dict__["module_id"] = module_id
        __props__.__dict__["name"] = name
        __props__.__dict__["positions"] = positions
        __props__.__dict__["tags"] = tags
        __props__.__dict__["type"] = type
        return Port(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "color_hex")

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="markConnected")
    def mark_connected(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "mark_connected")

    @property
    @pulumi.getter(name="moduleId")
    def module_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "module_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def positions(self) -> pulumi.Output[int]:
        return pulumi.get(self, "positions")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        One of [8p8c, 8p6c, 8p4c, 8p2c, 6p6c, 6p4c, 6p2c, 4p4c, 4p2c, gg45, tera-4p, tera-2p, tera-1p, 110-punch, bnc, f, n, mrj21, fc, lc, lc-pc, lc-upc, lc-apc, lsh, lsh-pc, lsh-upc, lsh-apc, mpo, mtrj, sc, sc-pc, sc-upc, sc-apc, st, cs, sn, sma-905, sma-906, urm-p2, urm-p4, urm-p8, splice, other].
        """
        return pulumi.get(self, "type")

