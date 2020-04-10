# surge-rules-integration

**v1.0**

This script grabs rules from [lhie1/Rules](https://github.com/lhie1/Rules) and your network provider, then integrates
those stuff to one config. Two `conf` files use code from both lhie1 and ConnersHua.

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

* [lhie1/Rules](https://github.com/lhie1/Rules/tree/master/Surge/Surge%203)
* [Surge3 配置详解 from zhuangzhuang](https://zhuangzhuang.cf/2018-11-14/surge/)
* [ConnersHua/Profiles](https://raw.githubusercontent.com/ConnersHua/Profiles/master/Surge/Surge3.conf)
