import logging

import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts


class Example(plugins.Plugin):
    __author__ = 'Deine-Email.InsertwhenReady@Domain.com'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Describe your Plugin Here! YES YOU DO THAT! ... Later'

    def on_loaded(self):
        logging.info("Directions Plugin Loaded!")

    # called before the plugin is unloaded
    def on_unload(self, ui):
        logging.info("Directions Plugin Unloaded! ... Bye!")
      
    # called hen there's internet connectivity
    def on_internet_available(self, agent):
        logging.info("Internet Conncection astablished")

    # called to setup the ui elements
    def on_ui_setup(self, ui):
        ui.add_element(
            'Direction',
            LabeledValue(
                color=BLACK,
                label='Direction:',
                value='North-East',
                position=(1, 95),
                label_font=fonts.Small,
                text_font=fonts.Small
            )
        )
