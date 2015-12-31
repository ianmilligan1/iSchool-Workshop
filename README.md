# iSchool-Workshop
30 October 2015, 10am-noon, Semaphore Demo Room in the Robarts Library, University of Toronto (Room 1150)

## Workshop
The slidedeck for this [workshop can be found here](https://github.com/ianmilligan1/iSchool-Workshop/raw/master/Web-Archive-Workshop.pdf). Slidedeck is mostly links and platforms that I will be running attendees through. If you were there in person, you can see what we did here. If you have any questions, please send me a note at [i2millig@uwaterloo.ca](mailto:i2millig@uwaterloo.ca).

## Preceding Lecture
This workshop follows a lecture that I (Ian Milligan) will be giving on 29 October 2015. A draft of my slidedeck can be found in this repository as well. Download the [PDF here](https://github.com/ianmilligan1/iSchool-Workshop/raw/master/iSchool-Slidedeck.pdf).

## Pre-Requisites
- this repository (`git clone https://github.com/ianmilligan1/iSchool-Workshop.git`)
- [Gephi 0.9](http://gephi.github.io/) - should now work out of the box on most systems!

## The Demonstration Collection
We'll be discussing and demonstrating the Canadian Political Parties and Political Interest Groups web collection. You can access it in two ways:
- Archive-It/University of Toronto Collection: <https://archive-it.org/collections/227>
- Shine Portal: <http://webarchives.ca/>

We also have pre-generated derivative data that we've generated using [warcbase](https://github.com/lintool/warcbase), which will be demoed in this workshop.

## Accessing Web Archived Data
![Shine](https://raw.githubusercontent.com/ianmilligan1/iSchool-Workshop/master/Shine.png)
_Figure 1: Shine in Action_

- Archive-It portal
- Shine portal: [Setting up UK Web Archive's Shine on OS X](https://github.com/lintool/warcbase/wiki/Shine:-Installing-Shine-Frontend-on-OS-X)
- Indexing with Hadoop: [Building Lucene Indexes Using Hadoop](https://github.com/lintool/warcbase/wiki/Building-Lucene-Indexes-Using-Hadoop)
- Warcbase: [Building and Running Warcbase Under OS X](https://github.com/lintool/warcbase/wiki/Building-and-Running-Warcbase-Under-OS-X)

## Link Analysis Example
![Virtual Machine with Gephi running](https://raw.githubusercontent.com/ianmilligan1/iSchool-Workshop/master/Gephi-VM-In-Action.png)
_Figure 2: Virtual Machine with Gephi running_

- [Gephi](http://gephi.github.io/)
- Political-Links.gdf: Generated using warcbase and the `pig2gdfp.py` portal. I will provide a walkthrough. [Raw data downloadable here.](https://raw.githubusercontent.com/ianmilligan1/iSchool-Workshop/master/political-links.gdf)
- Ingest Political-Links.gdf into Gephi and do some analysis!

## Acknowlegements
Thanks to Dr. Christoph Becker at the University of Toronto for making this event a reality!

This research has been supported by two Social Sciences and Humanities Research Council (SSHRC) grants, an Insight Grant (435-2015-0011) and an Insight Development Grant (430-2013-0616). Additional funding for student labour on this project comes from an Ontario Ministry of Research and Innovation Early Reseacher Award and the University of Waterloo.