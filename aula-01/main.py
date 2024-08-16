from typing import Tuple
import numpy as np

def get_data(file_path: str) -> np.array:
  with open(file_path, 'rb') as audio_file:
    audio_bytes = audio_file.read()
    audio_data = np.frombuffer(audio_bytes, dtype=np.int16)

  return audio_data

def fill_array(input: np.array, desired_length: int) -> np.array:
  padded_array = np.zeros(desired_length, dtype=input.dtype)
  padded_array[:len(input)] = input
  return padded_array

def prepare_data(data_1: np.array, data_2:np.array) -> Tuple[np.array, np.array]:
  if len(data_1) == len(data_2):
    return data_1, data_2
  
  if len(data_1) > len(data_2):
    data_2 = fill_array(data_2, len(data_1))
    return data_1, data_2

  data_1 = fill_array(data_1, len(data_2))
  return data_1, data_2


def main():
  audio_1 = get_data('./audio-teste.pcm')
  audio_2 = get_data('./sin-400hz.pcm')

  audio_1, audio_2 = prepare_data(audio_1, audio_2)
  summed_audio = audio_1 + audio_2
  summed_audio = np.clip(summed_audio, -32768, 32767)
  summed_pcm_data = summed_audio.astype(np.int16).tobytes()

  with open('./result.pcm', 'wb') as output_file:
    output_file.write(summed_pcm_data)

if __name__ == '__main__':
  main()