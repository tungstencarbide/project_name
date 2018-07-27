Project Name Generator
----------------------

Generates random, nonsensical project names from WordNet files.
Suitable for use for "secret" project names.

Dependencies
------------

- WordNet 3.x files. Can be installed anywhere, script looks for them in
./wn by default. The -s option lets you specify an alternate WordNet file
location. WordNet data can be acquired here: https://wordnet.princeton.edu/download/

- docopt. Creates command line interfaces right from your help text. I think
this should become part of base python. :)
