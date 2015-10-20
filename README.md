# iSchool-Workshop
30 October 2015, 10am-noon, Semaphore Demo Room in the Robarts Library, University of Toronto (Room 1150)

## Pre-Requisites
- this repository
- Gephi
    + If you want to use your own system, you can download [Gephi here](http://gephi.github.io/). Note that it requires Java 1.6 and is temperamental beyond that. 
    + If you don't feel like fighting with Java, you can download this Java Virtual Machine. (link TBA)

## The Demonstration Collection
We'll be discussing and demonstrating the Canadian Political Parties and Political Interest Groups web collection. You can access it in two ways:
- Archive-It/University of Toronto Collection: <https://archive-it.org/collections/227>
- Shine Portal: <http://webarchives.ca/>

We also have pre-generated derivative data that we've generated using [warcbase](https://github.com/lintool/warcbase), which will be demoed in this workshop.

## Accessing Web Archived Data
- Archive-It portal
- Shine portal: [Setting up UK Web Archive's Shine on OS X](https://github.com/lintool/warcbase/wiki/Shine:-Installing-Shine-Frontend-on-OS-X)
- Indexing with Hadoop: [Building Lucene Indexes Using Hadoop](https://github.com/lintool/warcbase/wiki/Building-Lucene-Indexes-Using-Hadoop)
- Warcbase: [Building and Running Warcbase Under OS X](https://github.com/lintool/warcbase/wiki/Building-and-Running-Warcbase-Under-OS-X)

## Link Analysis Example
- [Gephi](http://gephi.github.io/)
- Political-Links.gdf: Generated using warcbase and the `pig2gdfp.py` portal. I will provide a walkthrough. [Raw data downloadable here.](https://raw.githubusercontent.com/ianmilligan1/iSchool-Workshop/master/political-links.gdf)
- Ingest Political-Links.gdf into Gephi and do some analysis!
