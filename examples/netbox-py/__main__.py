"""A Python Pulumi program"""

import pulumi
import pulumi_netbox as netbox


cluster = netbox.get_cluster(name="CLUSTER_ESX")

pulumi.export("cluster", cluster.name)
