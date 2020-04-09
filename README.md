# surge-rules-integration

*Unfinished*

This script grabs rules from [lhie1/Rules](https://github.com/lhie1/Rules) and your network provider, then integrates
those stuff to one config.

## Dependencies

### main

* Python >= 3.6

### packages

* requests >= 2.22.0
* os
* sys

## Workflow

1. Fetch rules from lhie1/Rules, integrate to one file `tmp/intel.conf`.
2. Fetch network groups from provider, insert it into `tmp/intel.conf`.
3. Set up file server for `tmp/intel.conf`. The script DOES NOT provide this function, you may do it your way.
4. Finally, for instance, you can use http://127.0.0.1:2222/intel.conf as url of MANAGED-CONFIG

## Instruction

`python integration.py`

## Q&A

* In certain circumstances you may fix your proxy problem for sub fetching by yourself.

## Links

* [Quantumult](https://github.com/ConnersHua/Profiles/blob/master/Quantumult/Pro.conf)
* [Surge3](https://github.com/lhie1/Rules/tree/master/Surge/Surge%203)