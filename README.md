# periodallica
This is a very basic python script to bulk-download the full text html-files of journal issues in Gallica using the parent-ARK of the BNF catalogue général. Useful for journals with no/unknown rate of publication, as (other than [Pyllica](https://api.bnf.fr/fr/extracteur-python-de-corpus-de-periodiques)) it looks up the individual issues via the api first.

This is a **work in progress** and it might not work.

## How to use

Command line: After cloning this repository or simply downloading Periodallica.py to a convenient location, navigate to the folder and type 

```python Periodallica.py 'yourARK' info```

to get a list of years and the total number of issues available in Gallica [note: this will also count issues for which there is no full text available!].

To download the actual html-files type

```python Periodallica.py 'yourARK' write```



## Example
Starting from the entry for the "Courier lyrique et amusant, ou Passe-temps des toilettes" in the [Catalogue général](https://catalogue.bnf.fr/ark:/12148/cb327515088), copy the ARK either from the catalogue entry or the URL. **Only copy the string after "ark:/12148/"**, in this case: "cb327515088".

```python Periodallica.py cb327515088 info```

should produce

```
There are records for issues in these years:['1785', '1786', '1787', '1788', '1789']
There are records for 7 issues.
```


```python Periodallica.py 'yourARK' write```

will create an output folder (if this does not exist yet) in your current location and write 7 html files using the individual ARKs of the issues (as opposed to the ARK of the journal) as filename; it will tell you when its done:
```
There are records for issues issues in these years:['1785', '1786', '1787', '1788', '1789']
There are records for 7 issues
7 files have been written
0 files could not be downloaded

```


## Caveats
- The script will write html files for each issue referenced in gallica (including header-only files those for which there is no OCR!)
- It might produce duplicates if there is more than 1 instance of an issue in gallica!
- It will skip issues where access to the full text is denied.
- It will produce no usable result, if there is a forward to retronews. those files are easily sorted by size...
- Downloading large corpora will take a while as there is a built-in delay to avoid 429-warnings.

> it's bulky, slow and inelegant...
