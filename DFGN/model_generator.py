import numpy

from tools.data_helper import DataHelper

training_samples = int(numpy.random.uniform(1, 90449, [1]))


def build_helper(gz, args):
	return DataHelper(training_samples, gz=gz, config=args)
