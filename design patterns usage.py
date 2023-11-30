import analyser
import pathlib

# answer = input("Select source (1-file, 2 - database):")
# if answer == '1':
#     analyser.file_data_analyser.analyse_data()
#
# if answer == '2':
#     analyser.database_data_analyser.analyse_data()
#
# else:
#     print("incorrect selection")

from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """Basic representation of video exporting codec"""

    @abstractmethod
    def prepare_export(self, video_data):
        pass
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        pass

class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec"""

    def prepare_export(self, video_data):
        print("preparing video for lossless export ")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting data in lossless format to {folder} ")

class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec"""

    def prepare_export(self, video_data):
        print("preparing video for lossless export ")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting data in H264 format to {folder} ")

class AudioExporter(ABC):
    """Basic representation of video exporting codec"""

    @abstractmethod
    def prepare_export(self, audio_data):
        pass
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        pass

class AACAudioExporter(AudioExporter):
    """AAC Audio exporting codec"""

    def prepare_export(self, video_data):
        print("preparing audio for AAC Audio export ")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting audio in AAC format to {folder} ")


class WAVAudioExporter(AudioExporter):
    """WAV Audio exporting codec"""

    def prepare_export(self, audio_data):
        print("preparing audio for WAV Audio export ")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting audio in WAV format to {folder} ")

# FILE= 'hello.txt'
#
# path= pathlib.Path("..")
# with open(FILE,'r') as f:
#     print(f.readlines() )