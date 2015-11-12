gofigure
========
An IRC statistics generator that actually works!  
(hopefully, once it's actually written)

Design
------
*No, this isn't implemented yet.*

At its core, gofigure is a collection of Python packages rather than a single
executable script. That may seem inconvenient for this purpose, but it allows
its configuration to be as flexible as it gets. The user is supposed to import
the required modules and then set up a Generator instance, which connects one
Parser and multiple Components with each other. Don't worry, a basic generation
script is very short:

```python
from gofigure.generator import Generator
from gofigure.parsers.xchat import XChat
from gofigure.components import Meta
from gofigure.components.activity import ActivityGraph

Generator(XChat("/path/to/logs/#channel.log"), [Meta(), ActivityGraph()]).run()
```

### Parsers
In order to support the abundance of IRC log formats out there, we use Python
classes with a common, date-based sequential access interface that will get
imported and instantiated by the generation script. Modules for the most common
clients shall be provided.

### Components
These transform the sequence of processed IRC messages into actual statistics.
*to be designed*


The generated data is output as a chunk of JSON which will get loaded by
the Angular.js client that composes the statistics page using directives
(provided together with the Component modules) that render the JSON data of
the component using d3.js. That means that everything but a single file can be
served statically (unless components are added).
