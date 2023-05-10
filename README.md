# periodallica
This is a very basic python script to bulk-download the full text of journal issues in Gallica using the parent-ARK of the BNF catalogue général. Useful for journals with no/unknown rate of publication, as (other than [Pyllica](https://api.bnf.fr/fr/extracteur-python-de-corpus-de-periodiques)) it looks up the individual issues via the api first.

This is a **work in progress** and it might not work.

## How to use

Command line: After cloning this repository or simply downloading Periodallica.py to a convenient location, navigate to the folder and type 
'''python Periodallica.py 'yourARK''''

## Example
Downloading 



## Caveats
The script will write html files for each issue referenced in gallica (including header-only files those for which there is no OCR!)
It might produce duplicates if there is more than 1 instance of an issue in gallica!
It will skip issues where access to the full text is denied.
It will produce no usable result, if there is a forward to retronews. those files are easily sorted by size...
Downloading large corpora will take a while as there is a built-in delay to avoid 429-warnings.

> it's bulky, slow and inelegant...