import numpy

from tools.data_helper import DataHelper


def build_helper(gz, args):
	return DataHelper(args.training_samples, gz=gz, config=args)
