# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['RoleArgs', 'Role']

@pulumi.input_type
class RoleArgs:
    def __init__(__self__, *,
                 color_hex: pulumi.Input[str],
                 slug: pulumi.Input[str],
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Role resource.
        """
        pulumi.set(__self__, "color_hex", color_hex)
        pulumi.set(__self__, "slug", slug)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> pulumi.Input[str]:
        return pulumi.get(self, "color_hex")

    @color_hex.setter
    def color_hex(self, value: pulumi.Input[str]):
        pulumi.set(self, "color_hex", value)

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Input[str]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "slug", value)

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
class _RoleState:
    def __init__(__self__, *,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Role resources.
        """
        if color_hex is not None:
            pulumi.set(__self__, "color_hex", color_hex)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Role(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/inventoryitemrole/):

        > Inventory items can be organized by functional roles, which are fully customizable by the user. For example, you might create roles for power supplies, fans, interface optics, etc.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            tenant_id=netbox_tenant["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_role = netbox.inventory.item.Role("testRole",
            slug="role-1-slug",
            color_hex="123456")
        parent = netbox.inventory.Item("parent",
            device_id=test_device.id,
            role_id=test_role.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/inventoryitemrole/):

        > Inventory items can be organized by functional roles, which are fully customizable by the user. For example, you might create roles for power supplies, fans, interface optics, etc.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            tenant_id=netbox_tenant["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_role = netbox.inventory.item.Role("testRole",
            slug="role-1-slug",
            color_hex="123456")
        parent = netbox.inventory.Item("parent",
            device_id=test_device.id,
            role_id=test_role.id)
        ```

        :param str resource_name: The name of the resource.
        :param RoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoleArgs.__new__(RoleArgs)

            if color_hex is None and not opts.urn:
                raise TypeError("Missing required property 'color_hex'")
            __props__.__dict__["color_hex"] = color_hex
            __props__.__dict__["custom_fields"] = custom_fields
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if slug is None and not opts.urn:
                raise TypeError("Missing required property 'slug'")
            __props__.__dict__["slug"] = slug
            __props__.__dict__["tags"] = tags
        super(Role, __self__).__init__(
            'netbox:inventory/item/role:Role',
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
            name: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoleState.__new__(_RoleState)

        __props__.__dict__["color_hex"] = color_hex
        __props__.__dict__["custom_fields"] = custom_fields
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["slug"] = slug
        __props__.__dict__["tags"] = tags
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> pulumi.Output[str]:
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
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

