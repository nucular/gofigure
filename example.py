from gofigure.generator import Generator
from gofigure.parsers.xchat import XChatParser
from gofigure.figures import MetaFigure
from gofigure.figures.activity import ActivityFigure

Generator(XChat("/path/to/logs/#channel.log"), [
    MetaFigure(), ActivityFigure()
]).run()
