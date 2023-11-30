from abc import ABC, abstractmethod

class DataReader(ABC):

    @abstractmethod
    def read_data(self):
        """Reads data from file"""

    @abstractmethod
    def format_data(self):
        """Formats data that was read"""


class FileReader(DataReader):

    def read_data(self):
        """Reads data from file"""

    def format_data(self):
        """Formats data that was read"""

class DatabaseReader(DataReader):
    def read_data(self):
        print("reading database-data")
    def format_data(self):
        print("Formating database-data")

class Analyser(ABC):

    def analyse_data(self):
        reader = create_reader()
        reader.get_data()
        data = reader.format_data()
        print('Analysing data...')


    @abstractmethod
    def create_reader(self):
        pass

class FileDataAnalyser(Analyser):

    def create_reader(self):
        return FileReader()


class DatabaseDataAnalyser(Analyser):

    def create_reader(self):
        return DatabaseReader()

file_data_analyser = FileDataAnalyser()
database_data_analyser = DatabaseDataAnalyser()