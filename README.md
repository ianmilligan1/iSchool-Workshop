# iSchool-Workshop
30 October 2015, 10am-noon, Semaphore Demo Room in the Robarts Library, University of Toronto (Room 1150)

The slidedeck for this [workshop can be found here](https://github.com/ianmilligan1/iSchool-Workshop/raw/master/Web-Archive-Workshop.pdf). Note that I will almost certainly be tinkering with it up until 10am on 30 October 2015. Slidedeck is mostly links and platforms that I will be running attendees through.

This workshop follows a lecture that Ian Milligan will be giving on 29 October 2015. A draft of his slidedeck can be found in this repository as well. Download the [PDF here](https://github.com/ianmilligan1/iSchool-Workshop/raw/master/iSchool-Slidedeck.pdf).

## Pre-Requisites
- this repository (`https://github.com/ianmilligan1/iSchool-Workshop.git`)
- Gephi
    + If you want to use your own system, you can download [Gephi here](http://gephi.github.io/). Note that it requires Java 1.6 and is temperamental beyond that. If you're on OS X, [these instructions *usually* work](http://sumnous.github.io/blog/2014/07/24/gephi-on-mac/).
    + If you don't feel like fighting with Java, you can download this [Java Virtual Machine](http://ianmilligan.ca/historycrawler/). You'll need to install Gephi on the VM. **The password for this VM is "go"**
    + To run Gephi in the VM, run `gephi` in `~/gephi/bin`

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
