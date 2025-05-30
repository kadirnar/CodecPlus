"""Base classes for audio codecs"""

class BaseCodec:
    """Base class for all audio codecs"""
    
    def __init__(self, config=None):
        self.config = config or {}
        
    def encode(self, audio):
        """Encode audio to tokens/latents"""
        raise NotImplementedError
        
    def decode(self, tokens):
        """Decode tokens/latents to audio"""
        raise NotImplementedError
        
class BaseEncoder:
    """Base class for encoders"""
    
    def __call__(self, audio):
        return self.encode(audio)
        
    def encode(self, audio):
        raise NotImplementedError

class BaseDecoder:
    """Base class for decoders"""
    
    def __call__(self, tokens):
        return self.decode(tokens)
        
    def decode(self, tokens):
        raise NotImplementedError
