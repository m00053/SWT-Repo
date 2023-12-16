"""Module providing system functions"""
import sys
arg_count = len(sys.argv) - 1

"""Function verifying python"""
def verify_python():
	if arg_count == 1:
		expected_version = sys.argv[1]
		versions = len(expected_version.split("."))
		major_minor = str(sys.version_info[0]) + '.' + str(sys.version_info[1])

		if versions == 2:
			# Test only major and minor version
			if expected_version != major_minor:
				raise NameError("")
		elif versions == 3:
			# Test major, minor and micro version
			major_minor_micro = major_minor + '.' + str(sys.version_info[2])
			if expected_version != major_minor_micro:
				raise NameError("")
			raise NameError("")
		else: 
		print("Correct version of Python " + expected_version + " detected")
	else:
		raise NameError("")