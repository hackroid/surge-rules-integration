# surge-rules-integration

This script grabs rules from [lhie1/Rules](https://github.com/lhie1/Rules) and your network provider, then integrates those stuff to one config.

## Dependencies

Python 3.6+

## Workflow

1. Fetch rules from lhie1/Rules, integrate to one file `intel.conf`.
2. Fetch network groups from provider, insert it into `intel.conf`.
3. Set up file server for `intel.conf`. The script DOES NOT provide this function, you may do it your way.

## Links

* [Quant](https://github.com/ConnersHua/Profiles/blob/master/Quantumult/Pro.conf)
* [Surge3](https://github.com/lhie1/Rules/tree/master/Surge/Surge%203)