# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .item import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_netbox.inventory.item as __item
    item = __item
else:
    item = _utilities.lazy_import('pulumi_netbox.inventory.item')

