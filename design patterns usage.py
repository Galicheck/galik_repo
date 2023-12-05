#import analyser
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


class ExporterFactory(ABC):

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        pass

class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_factory() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference"""

    factories = {'low': FastExporter(),
                 'master': MasterQualityExporter()
                 }
    while True:
        export_quality = input('Enter desired output quality: low or master')
        if export_quality in factories:
            return factories[export_quality]
        print("Bad choice")

def main(fac: ExporterFactory) -> None:
    # retrieve the exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export

    video_exporter.prepare_export("Placeholder for video data")
    audio_exporter.prepare_export("Placeholder for audio data")

    # do the export

    folder = pathlib.Path('/usr/tmp/video')
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

factory = read_factory()
main(factory)
# FILE= 'hello.txt'
#
# path= pathlib.Path("..")
# with open(FILE,'r') as f:
#     print(f.readlines() )
