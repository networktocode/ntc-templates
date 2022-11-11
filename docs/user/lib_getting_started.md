# Getting Started with the Library

The library's primary use case is to provide pre-canned parsers for TextFSM.

## Install the Library

To install the library, please follow the instructions detailed in the [Installation Guide](../admin/install.md).

## Usage

The libraries interface is fairly simple, the only public function is the `parse_output` function.

```python
>>> from ntc_templates.parse import parse_output
>>> vlan_output = (
        "VLAN Name                             Status    Ports\n"
        "---- -------------------------------- --------- -------------------------------\n"
        "1    default                          active    Gi0/1\n"
        "10   Management                       active    \n"
        "50   VLan50                           active    Fa0/1, Fa0/2, Fa0/3, Fa0/4, Fa0/5,\n"
        "                                                Fa0/6, Fa0/7, Fa0/8\n"
    )
>>> vlan_parsed = parse_output(platform="cisco_ios", command="show vlan", data=vlan_output)
>>> vlan_parsed
[
    {
        'vlan_id': '1',
        'name': 'default',
        'status': 'active',
        'interfaces': ['Gi0/1']
    },
    {
        'vlan_id': '10',
        'name': 'Management',
        'status': 'active',
        'interfaces': []
    },
    {
        'vlan_id': '50',
        'name': 'VLan50', 'status': 'active',
        'interfaces': ['Fa0/1', 'Fa0/2', 'Fa0/3', 'Fa0/4', 'Fa0/5', 'Fa0/6', 'Fa0/7', 'Fa0/8']
    }
]
>>> 
```

The rest of the functionality comes from the indiviudal TextFSM templates and the primary index file.