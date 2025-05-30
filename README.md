# CodecPlus

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org)

CodecPlus is a comprehensive audio codec library that implements various state-of-the-art audio codec models without external dependencies. The library is designed to be modular, easy to use, and extend.

## Features

- Pure Python implementation of audio codec models
- Includes multiple codec implementations:
  - WavTokenizer: Audio tokenization model
  - DAC: Descript Audio Codec
- Easy-to-use API for encoding and decoding audio
- Comprehensive utilities for audio processing

## Installation

```bash
# From source
git clone https://github.com/kadirnar/CodecPlus.git
cd CodecPlus
pip install -e .
```

## Usage

```python
from codecplus import load_codec
from codecplus.utils import load_audio, save_audio

# Load audio file
audio, sr = load_audio('path/to/audio.wav')

# Using WavTokenizer
wav_tokenizer = load_codec('wav_tokenizer')
tokens = wav_tokenizer.encode(audio)
reconstructed_audio = wav_tokenizer.decode(tokens)

# Using DAC (Descript Audio Codec)
dac = load_codec('dac', sample_rate=44100)
latents = dac.encode(audio)
reconstructed_audio = dac.decode(latents)

# Save processed audio
save_audio(reconstructed_audio, 'path/to/output.wav', sr)
```

## Documentation

For more detailed documentation, examples, and API references, see the [documentation](docs/).

## Examples

Explore the [notebooks](notebooks/) directory for interactive examples and tutorials.

## Project Structure

```
codecplus/
├── __init__.py             # Main package initialization
├── codecs/                 # Codec implementations
│   ├── __init__.py
│   ├── base.py             # Base codec classes
│   ├── wav_tokenizer/      # WavTokenizer implementation
│   │   ├── __init__.py
│   │   └── model.py
│   └── dac/                # Descript Audio Codec
│       ├── __init__.py
│       └── model.py
└── utils/                  # Utility functions
    ├── __init__.py
    └── audio.py            # Audio processing utilities
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
