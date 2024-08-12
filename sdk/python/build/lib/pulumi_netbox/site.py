# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SiteArgs', 'Site']

@pulumi.input_type
class SiteArgs:
    def __init__(__self__, *,
                 asn_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 facility: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[int]] = None,
                 latitude: Optional[pulumi.Input[float]] = None,
                 longitude: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 physical_address: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 shipping_address: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[int]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Site resource.
        :param pulumi.Input[str] status: Valid values are `planned`, `staging`, `active`, `decommissioning` and `retired`. Defaults to `active`.
        """
        if asn_ids is not None:
            pulumi.set(__self__, "asn_ids", asn_ids)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if facility is not None:
            pulumi.set(__self__, "facility", facility)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if latitude is not None:
            pulumi.set(__self__, "latitude", latitude)
        if longitude is not None:
            pulumi.set(__self__, "longitude", longitude)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if physical_address is not None:
            pulumi.set(__self__, "physical_address", physical_address)
        if region_id is not None:
            pulumi.set(__self__, "region_id", region_id)
        if shipping_address is not None:
            pulumi.set(__self__, "shipping_address", shipping_address)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter(name="asnIds")
    def asn_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "asn_ids")

    @asn_ids.setter
    def asn_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "asn_ids", value)

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
    def facility(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "facility")

    @facility.setter
    def facility(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "facility", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def latitude(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "latitude")

    @latitude.setter
    def latitude(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "latitude", value)

    @property
    @pulumi.getter
    def longitude(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "longitude")

    @longitude.setter
    def longitude(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "longitude", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="physicalAddress")
    def physical_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "physical_address")

    @physical_address.setter
    def physical_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "physical_address", value)

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "region_id")

    @region_id.setter
    def region_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "region_id", value)

    @property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "shipping_address")

    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shipping_address", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values are `planned`, `staging`, `active`, `decommissioning` and `retired`. Defaults to `active`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


@pulumi.input_type
class _SiteState:
    def __init__(__self__, *,
                 asn_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 facility: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[int]] = None,
                 latitude: Optional[pulumi.Input[float]] = None,
                 longitude: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 physical_address: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 shipping_address: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[int]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Site resources.
        :param pulumi.Input[str] status: Valid values are `planned`, `staging`, `active`, `decommissioning` and `retired`. Defaults to `active`.
        """
        if asn_ids is not None:
            pulumi.set(__self__, "asn_ids", asn_ids)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if facility is not None:
            pulumi.set(__self__, "facility", facility)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if latitude is not None:
            pulumi.set(__self__, "latitude", latitude)
        if longitude is not None:
            pulumi.set(__self__, "longitude", longitude)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if physical_address is not None:
            pulumi.set(__self__, "physical_address", physical_address)
        if region_id is not None:
            pulumi.set(__self__, "region_id", region_id)
        if shipping_address is not None:
            pulumi.set(__self__, "shipping_address", shipping_address)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter(name="asnIds")
    def asn_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "asn_ids")

    @asn_ids.setter
    def asn_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "asn_ids", value)

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
    def facility(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "facility")

    @facility.setter
    def facility(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "facility", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def latitude(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "latitude")

    @latitude.setter
    def latitude(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "latitude", value)

    @property
    @pulumi.getter
    def longitude(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "longitude")

    @longitude.setter
    def longitude(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "longitude", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="physicalAddress")
    def physical_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "physical_address")

    @physical_address.setter
    def physical_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "physical_address", value)

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "region_id")

    @region_id.setter
    def region_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "region_id", value)

    @property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "shipping_address")

    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shipping_address", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values are `planned`, `staging`, `active`, `decommissioning` and `retired`. Defaults to `active`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


class Site(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asn_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 facility: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[int]] = None,
                 latitude: Optional[pulumi.Input[float]] = None,
                 longitude: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 physical_address: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 shipping_address: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[int]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/features/sites-and-racks/#sites):

        > How you choose to employ sites when modeling your network may vary depending on the nature of your organization, but generally a site will equate to a building or campus. For example, a chain of banks might create a site to represent each of its branches, a site for its corporate headquarters, and two additional sites for its presence in two colocation facilities.
        > 
        > Each site must be assigned a unique name and may optionally be assigned to a region and/or tenant.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] status: Valid values are `planned`, `staging`, `active`, `decommissioning` and `retired`. Defaults to `active`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SiteArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/features/sites-and-racks/#sites):

        > How you choose to employ sites when modeling your network may vary depending on the nature of your organization, but generally a site will equate to a building or campus. For example, a chain of banks might create a site to represent each of its branches, a site for its corporate headquarters, and two additional sites for its presence in two colocation facilities.
        > 
        > Each site must be assigned a unique name and may optionally be assigned to a region and/or tenant.

        :param str resource_name: The name of the resource.
        :param SiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asn_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 facility: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[int]] = None,
                 latitude: Optional[pulumi.Input[float]] = None,
                 longitude: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 physical_address: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 shipping_address: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[int]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SiteArgs.__new__(SiteArgs)

            __props__.__dict__["asn_ids"] = asn_ids
            __props__.__dict__["custom_fields"] = custom_fields
            __props__.__dict__["description"] = description
            __props__.__dict__["facility"] = facility
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["latitude"] = latitude
            __props__.__dict__["longitude"] = longitude
            __props__.__dict__["name"] = name
            __props__.__dict__["physical_address"] = physical_address
            __props__.__dict__["region_id"] = region_id
            __props__.__dict__["shipping_address"] = shipping_address
            __props__.__dict__["slug"] = slug
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["timezone"] = timezone
        super(Site, __self__).__init__(
            'netbox:index/site:Site',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            asn_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            facility: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[int]] = None,
            latitude: Optional[pulumi.Input[float]] = None,
            longitude: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            physical_address: Optional[pulumi.Input[str]] = None,
            region_id: Optional[pulumi.Input[int]] = None,
            shipping_address: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tenant_id: Optional[pulumi.Input[int]] = None,
            timezone: Optional[pulumi.Input[str]] = None) -> 'Site':
        """
        Get an existing Site resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] status: Valid values are `planned`, `staging`, `active`, `decommissioning` and `retired`. Defaults to `active`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SiteState.__new__(_SiteState)

        __props__.__dict__["asn_ids"] = asn_ids
        __props__.__dict__["custom_fields"] = custom_fields
        __props__.__dict__["description"] = description
        __props__.__dict__["facility"] = facility
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["latitude"] = latitude
        __props__.__dict__["longitude"] = longitude
        __props__.__dict__["name"] = name
        __props__.__dict__["physical_address"] = physical_address
        __props__.__dict__["region_id"] = region_id
        __props__.__dict__["shipping_address"] = shipping_address
        __props__.__dict__["slug"] = slug
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tenant_id"] = tenant_id
        __props__.__dict__["timezone"] = timezone
        return Site(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="asnIds")
    def asn_ids(self) -> pulumi.Output[Optional[Sequence[int]]]:
        return pulumi.get(self, "asn_ids")

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
    def facility(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "facility")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def latitude(self) -> pulumi.Output[Optional[float]]:
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter
    def longitude(self) -> pulumi.Output[Optional[float]]:
        return pulumi.get(self, "longitude")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="physicalAddress")
    def physical_address(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "physical_address")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "shipping_address")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Valid values are `planned`, `staging`, `active`, `decommissioning` and `retired`. Defaults to `active`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "timezone")

