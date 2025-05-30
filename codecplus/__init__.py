# CodecPlus: Audio codec models library
__version__ = "0.1.0"


def load_codec(name, **kwargs):
    """Load a codec model by name"""
    if name == "wav_tokenizer":
        from codecplus.codecs.wav_tokenizer import WavTokenizer

        return WavTokenizer(**kwargs)
    elif name == "dac":
        from codecplus.codecs.dac import DAC

        return DAC(**kwargs)
    else:
        raise ValueError(f"Unknown codec: {name}")
