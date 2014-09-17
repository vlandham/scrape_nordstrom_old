# Nordstrom Scraper

Use python's scrapy to pull down some data. Just to compare notes.

## Install

Should be able to do a 

     pip install -r requirements.txt

And get things going.

## Run

The ./run.sh script will run the spider and put the results in a file in the _out/_ directory - by date. 


_WARNING:_ if you run it again on the same day - it will remove that existing file and make a new one. This may or may not be what you want.


## Caveats

* Doesn't yet really deal with SKU level data - just Products. 
* Doesn't seem to capture everything.
* Not robust to errors
* Has some duplicate product ids in its capture - mostly around the referrer tag in the url.

## TODO

* SKU level data
* Is product availible or not?
* More robustness to the different types of pages we see.
