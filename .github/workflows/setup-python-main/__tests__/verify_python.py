import sys
argCount = len(sys.argv) - 1

def print_test():
    if argCount == 1:
        expectedVersion = sys.argv[1]
        versions = len(expectedVersion.split("."))
        MAJOR_MINOR = str(sys.version_info[0]) + '.' + str(sys.version_info[1])

        if versions == 2:
            # Test only major and minor version
            if expectedVersion != MAJOR_MINOR:
                raise Exception("")
                #    logging.exception(e)
                #raise Exception("Incorrect MAJOR_MINOR v.: " + MAJOR_MINOR + "\nExpected: " + expectedVersion)
                #raise Exception("Incorrect major + minor version detected\nExpected: " + expectedVersion + "\nActual: " + MAJOR_MINOR)
        elif versions == 3:
            # Test major, minor and micro version
            MAJOR_MINOR_MICRO = MAJOR_MINOR + '.' + str(sys.version_info[2])
            if expectedVersion != MAJOR_MINOR_MICRO:
                raise Exception("")
                #    logging.exception(e)
                #raise Exception("Incorrect MAJOR_MINOR micro v.: " + MAJOR_MINOR_MICRO + "\nExpected: " + expectedVersion)
                #raise Exception("Incorrect major + minor + micro version detected\nExpected: " + expectedVersion + "\nActual: " + MAJOR_MINOR_MICRO)
        else:
            raise Exception("")
            #    logging.exception(e)
            #raise Exception("Incorrect number of arguments supplied")
        print("Correct version of Python " + expectedVersion + " detected")
    else:
        raise Exception("")
        #    logging.exception(e)
        #raise Exception("Incorrect number of arguments supplied")
