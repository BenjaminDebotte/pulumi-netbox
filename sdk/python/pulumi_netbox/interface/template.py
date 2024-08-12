# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TemplateArgs', 'Template']

@pulumi.input_type
class TemplateArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 device_type_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mgmt_only: Optional[pulumi.Input[bool]] = None,
                 module_type_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Template resource.
        :param pulumi.Input[int] device_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        :param pulumi.Input[int] module_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_type_id is not None:
            pulumi.set(__self__, "device_type_id", device_type_id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if mgmt_only is not None:
            pulumi.set(__self__, "mgmt_only", mgmt_only)
        if module_type_id is not None:
            pulumi.set(__self__, "module_type_id", module_type_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceTypeId")
    def device_type_id(self) -> Optional[pulumi.Input[int]]:
        """
        Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        return pulumi.get(self, "device_type_id")

    @device_type_id.setter
    def device_type_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "device_type_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="mgmtOnly")
    def mgmt_only(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "mgmt_only")

    @mgmt_only.setter
    def mgmt_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mgmt_only", value)

    @property
    @pulumi.getter(name="moduleTypeId")
    def module_type_id(self) -> Optional[pulumi.Input[int]]:
        """
        Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        return pulumi.get(self, "module_type_id")

    @module_type_id.setter
    def module_type_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "module_type_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TemplateState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 device_type_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mgmt_only: Optional[pulumi.Input[bool]] = None,
                 module_type_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Template resources.
        :param pulumi.Input[int] device_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        :param pulumi.Input[int] module_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_type_id is not None:
            pulumi.set(__self__, "device_type_id", device_type_id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if mgmt_only is not None:
            pulumi.set(__self__, "mgmt_only", mgmt_only)
        if module_type_id is not None:
            pulumi.set(__self__, "module_type_id", module_type_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceTypeId")
    def device_type_id(self) -> Optional[pulumi.Input[int]]:
        """
        Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        return pulumi.get(self, "device_type_id")

    @device_type_id.setter
    def device_type_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "device_type_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="mgmtOnly")
    def mgmt_only(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "mgmt_only")

    @mgmt_only.setter
    def mgmt_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mgmt_only", value)

    @property
    @pulumi.getter(name="moduleTypeId")
    def module_type_id(self) -> Optional[pulumi.Input[int]]:
        """
        Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        return pulumi.get(self, "module_type_id")

    @module_type_id.setter
    def module_type_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "module_type_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Template(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_type_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mgmt_only: Optional[pulumi.Input[bool]] = None,
                 module_type_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/interfacetemplate/):

        > A template for a network interface that will be created on all instantiations of the parent device type. See the interface documentation for more detail.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        test_manufacturer = netbox.Manufacturer("testManufacturer")
        test_type = netbox.device.Type("testType",
            model="test-model",
            slug="test-model",
            part_number="test-part-number",
            manufacturer_id=test_manufacturer.id)
        test_template = netbox.interface.Template("testTemplate",
            description="eth0 description",
            label="eth0 label",
            device_type_id=test_type.id,
            type="100base-tx",
            mgmt_only=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] device_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        :param pulumi.Input[int] module_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/interfacetemplate/):

        > A template for a network interface that will be created on all instantiations of the parent device type. See the interface documentation for more detail.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_netbox as netbox

        test_manufacturer = netbox.Manufacturer("testManufacturer")
        test_type = netbox.device.Type("testType",
            model="test-model",
            slug="test-model",
            part_number="test-part-number",
            manufacturer_id=test_manufacturer.id)
        test_template = netbox.interface.Template("testTemplate",
            description="eth0 description",
            label="eth0 label",
            device_type_id=test_type.id,
            type="100base-tx",
            mgmt_only=True)
        ```

        :param str resource_name: The name of the resource.
        :param TemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_type_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 mgmt_only: Optional[pulumi.Input[bool]] = None,
                 module_type_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TemplateArgs.__new__(TemplateArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["device_type_id"] = device_type_id
            __props__.__dict__["label"] = label
            __props__.__dict__["mgmt_only"] = mgmt_only
            __props__.__dict__["module_type_id"] = module_type_id
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(Template, __self__).__init__(
            'netbox:interface/template:Template',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            device_type_id: Optional[pulumi.Input[int]] = None,
            label: Optional[pulumi.Input[str]] = None,
            mgmt_only: Optional[pulumi.Input[bool]] = None,
            module_type_id: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Template':
        """
        Get an existing Template resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] device_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        :param pulumi.Input[int] module_type_id: Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TemplateState.__new__(_TemplateState)

        __props__.__dict__["description"] = description
        __props__.__dict__["device_type_id"] = device_type_id
        __props__.__dict__["label"] = label
        __props__.__dict__["mgmt_only"] = mgmt_only
        __props__.__dict__["module_type_id"] = module_type_id
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        return Template(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceTypeId")
    def device_type_id(self) -> pulumi.Output[Optional[int]]:
        """
        Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        return pulumi.get(self, "device_type_id")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="mgmtOnly")
    def mgmt_only(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "mgmt_only")

    @property
    @pulumi.getter(name="moduleTypeId")
    def module_type_id(self) -> pulumi.Output[Optional[int]]:
        """
        Exactly one of `device_type_id` or `module_type_id` must be given.
        """
        return pulumi.get(self, "module_type_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

