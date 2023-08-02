from TTS.config import load_config
from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.models.vits import Vits
import math
import os
from dataclasses import dataclass, field, replace
from itertools import chain
from typing import Dict, List, Tuple, Union

import numpy as np
import torch
import torch.distributed as dist
import torchaudio
from coqpit import Coqpit
from librosa.filters import mel as librosa_mel_fn
from torch import nn
from torch.cuda.amp.autocast_mode import autocast
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torch.utils.data.sampler import WeightedRandomSampler
from trainer.torch import DistributedSampler, DistributedSamplerWrapper
from trainer.trainer_utils import get_optimizer, get_scheduler

from TTS.tts.configs.shared_configs import CharactersConfig
from TTS.tts.datasets.dataset import TTSDataset, _parse_sample
from TTS.tts.layers.glow_tts.duration_predictor import DurationPredictor
from TTS.tts.layers.vits.discriminator import VitsDiscriminator
from TTS.tts.layers.vits.networks import PosteriorEncoder, ResidualCouplingBlocks, TextEncoder
from TTS.tts.layers.vits.stochastic_duration_predictor import StochasticDurationPredictor
from TTS.tts.models.base_tts import BaseTTS
from TTS.tts.utils.fairseq import rehash_fairseq_vits_checkpoint
from TTS.tts.utils.helpers import generate_path, maximum_path, rand_segments, segment, sequence_mask
from TTS.tts.utils.languages import LanguageManager
from TTS.tts.utils.speakers import SpeakerManager
from TTS.tts.utils.synthesis import synthesis
from TTS.tts.utils.text.characters import BaseCharacters, BaseVocabulary, _characters, _pad, _phonemes, _punctuations
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.tts.utils.visual import plot_alignment
from TTS.utils.io import load_fsspec
from TTS.utils.samplers import BucketBatchSampler
from TTS.vocoder.models.hifigan_generator import HifiganGenerator
from TTS.vocoder.utils.generic_utils import plot_results


config_path = "https://huggingface.co/mohelwah/tts-finetuned/resolve/main/config.json"
model_path = "https://huggingface.co/mohelwah/tts-finetuned/resolve/main/checkpoint_2530000.pth"





config = load_config(config_path)
print("done 0")


model = Vits.init_from_config(config,verbose=True)
print("done 1")
model.load_checkpoint( config, model_path, eval=True)
print("done")





