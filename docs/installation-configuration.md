---
title: Netbox Installation & Configuration
meta_desc: Information on how to install the Netbox provider.
layout: installation
---

## Installation

The Pulumi Netbox provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@pulumiverse/netbox`](https://www.npmjs.com/package/@pulumiverse/netbox)
* Python: [`pulumi_netbox`](https://pypi.org/project/pulumi_netbox/)
* Go: [`github.com/BenjaminDebotte/pulumi-netbox/sdk/go/netbox`](https://pkg.go.dev/github.com/BenjaminDebotte/pulumi-netbox/sdk/go/netbox)
* .NET: [`Pulumiverse.Netbox`](https://www.nuget.org/packages/Pulumiverse.Netbox)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `netbox` provider:

- `netbox:apiKey` (environment: `netbox_API_KEY`) - the API key for `netbox`
- `netbox:region` (environment: `netbox_REGION`) - the region in which to deploy resources

### Provider Binary

The Netbox provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource netbox <version>
```

Replace the version string `<version>` with your desired version.
