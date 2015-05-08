# py-burrows-wheeler : using Burrows-Wheeler Transform to explore strings in python. #

  * [What does it look for?](http://code.google.com/p/py-rstr-max/#What_does_look_for?)
  * [Usage](http://code.google.com/p/py-rstr-max/#Usage)
  * [See also](http://code.google.com/p/py-rstr-max/#See_also)

## What does it look for? ##

The Burrows-Wheeler Tranform (BWT) gives simple data-structures to :

  * compress efficiently a string
  * count the number of pattern in a string
  * locate pattern in a string (offset)

## Usage ##

Just go to the svn version ; or download the last version http://code.google.com/p/py-burrows-wheeler/downloads/list

### Inside burrows\_wheeler.test.py ###

Starting with py-burrows-wheeler, here playing with "mississippi$"

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools_burrows_wheeler import BWT
import tools_karkkainen_sanders as tks

s  = 'mississippi$'
su = unicode(s,'utf-8')
```

Compute indexes and internal data structure (suffix array, pre-LF-mapping structure)

```
bwt = BWT(su)
```

Get the BWT of `s` : `ipssm$pissii`

```
str_bwt = bwt.bwt
```

Two way to localte a pattern in `s`

```
pattern = 'iss'
```

  * method 1 : use the complete LF-mapping to search in the string (size : n\*alphabet\_size)
  * method 2 : use a partial LF-mapping to search in the string (size : n)

<table>
<tr>
<blockquote><th>method 1<br />huge index, quick access</th>
<th>method 2<br />small index, log access</th>
</tr>
<tr><td>
<pre><code>bwt.prepare_search1()<br>
l1 = bwt.locate1(pattern)<br>
</code></pre>
</td><td>
<pre><code>bwt.prepare_search2()<br>
l2 = bwt.locate2(pattern)<br>
</code></pre>
</td></tr>
</table></blockquote>

```
"iss" in "mississipi$" : l1 == l2 == [4,1]
```


## See also ##

  * [pysuffix project](http://code.google.com/p/pysuffix/)
  * [py-rstr-max project](http://code.google.com/p/py-rstr-max/)