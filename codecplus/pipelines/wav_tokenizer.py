import torch
import torchaudio

from codecplus.codecs.wav_tokenizer.decoder.pretrained import WavTokenizer
from codecplus.codecs.wav_tokenizer.encoder.utils import convert_audio


class WavTokenizerPipeline:
    def __init__(
        self,
        model_path,
        config_path,
        device,
    ):
        self.model_path = model_path
        self.config_path = config_path
        self.device = device

        self.wavtokenizer = None
        if self.wavtokenizer is None:
            self.load_model()

    def load_model(self):
        wavtokenizer = WavTokenizer.from_pretrained0802(
            self.config_path, self.model_path
        )
        wavtokenizer = wavtokenizer.to(self.device)
        bandwidth_id = torch.tensor([0])

        self.wavtokenizer = wavtokenizer
        self.bandwidth_id = bandwidth_id

        return wavtokenizer

    def encode(self, audio_path):
        wav, sr = torchaudio.load(audio_path)
        wav = convert_audio(wav, sr, 24000, 1)
        wav = wav.to(self.device)
        features, discrete_code = self.wavtokenizer.encode_infer(
            wav, bandwidth_id=self.bandwidth_id
        )

        self.features = features
        self.discrete_code = discrete_code

        return features, discrete_code

    def decode(self, audio_outpath):
        audio_out = self.wavtokenizer.decode(
            self.features, bandwidth_id=self.bandwidth_id
        )
        torchaudio.save(
            audio_outpath,
            audio_out,
            sample_rate=24000,
            encoding="PCM_S",
            bits_per_sample=16,
        )
