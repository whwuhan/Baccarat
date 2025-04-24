import os
from enum import Enum

class BuildConfig(Enum):
	BUILD_NONE = 0
	BUILD_DEBUG = 1
	BUILD_TEST = 2
	BUILD_SHIPPING = 3

build_evn = BuildConfig.BUILD_NONE


