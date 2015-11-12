from gofigure.generator import Generator
from gofigure.parsers.xchat import XChat
from gofigure.components import Meta
from gofigure.components.activity import ActivityGraph

Generator(XChat("/path/to/logs/#channel.log"), [Meta(), ActivityGraph()]).run()
