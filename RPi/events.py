class OutputEvent:
    def __init__(self, channel, outmode):
        self.channel = channel
        self.outmode = outmode

    def as_dict(self):
        return {
            'type': 'output',
            'channel': self.channel,
            'outmode': self.outmode
        }


class SetmodeEvent:
    def __init__(self, mode):
        self.mode = mode

    def as_dict(self):
        return {
            'type': 'mode',
            'mode': self.mode
        }
