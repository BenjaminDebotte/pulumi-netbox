# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .tunnel import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_netbox.vpn.tunnel as __tunnel
    tunnel = __tunnel
else:
    tunnel = _utilities.lazy_import('pulumi_netbox.vpn.tunnel')

