import pathlib

from pydplace.dataset import DatasetWithSocieties


class Dataset(DatasetWithSocieties):
    dir = pathlib.Path(__file__).parent
    id = "dplace-dataset-ea"
