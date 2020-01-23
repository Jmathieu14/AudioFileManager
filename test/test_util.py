
class TestDetail:
    def __init__(self, expected, actual, name: str):
        self.expected = expected
        self.actual = actual
        self.name = name
        self.passed = True

    def set_passed_false(self):
        self.passed = False

    def get_message(self):
        if self.passed:
            return self.success_message()
        else:
            return self.failure_message()

    def success_message(self):
        return "Passed: " + self.name

    def failure_message(self):
        return "Failed: " + self.name + \
                "\n\tactual: " + str(self.actual) + \
                "\n\tDid NOT equal: \n\t" + \
                "expected: " + str(self.expected)


# Test's global variables
TESTS_PASSED = 0
TESTS_FAILED = 0
TESTS_RAN = []


def assert_not_null(result, name):
    my_test_detail = TestDetail("Not Null", result, name)
    global TESTS_PASSED
    global TESTS_FAILED
    global TESTS_RAN
    if None == result:
        print("Error in " + name)
        my_test_detail.set_passed_false()
        TESTS_FAILED = TESTS_FAILED + 1
    else:
        TESTS_PASSED = TESTS_PASSED + 1
    TESTS_RAN.append(my_test_detail)


# Compare results of conducted test
def compare_results(expected, actual, name):
    my_test_detail = TestDetail(expected, actual, name)
    global TESTS_PASSED
    global TESTS_FAILED
    global TESTS_RAN
    # Allow for testing of multiple possible expected outcomes
    if type(expected) is dict and "pos_outcomes" in expected.keys():
        possible_outcomes = expected['pos_outcomes']
        __compare_multiple_outcomes__(my_test_detail, possible_outcomes, actual, name)
    else:
        if actual != expected:
            print("Error in " + name)
            my_test_detail.set_passed_false()
            TESTS_FAILED = TESTS_FAILED + 1
        else:
            TESTS_PASSED = TESTS_PASSED + 1
    TESTS_RAN.append(my_test_detail)


def __compare_multiple_outcomes__(current_test_detail: TestDetail, possible_outcomes, actual, name):
    global TESTS_PASSED
    global TESTS_FAILED
    global TESTS_RAN
    prev_tests_passed = TESTS_PASSED
    # Iterate through each possible outcome and see if at least one was true
    for outcome in possible_outcomes:
        if actual == outcome:
            TESTS_PASSED = TESTS_PASSED + 1
            break
    # If no change in tests passed, mark this test as a failure
    if prev_tests_passed == TESTS_PASSED:
        print("Error in " + name)
        current_test_detail.set_passed_false()
        TESTS_FAILED = TESTS_FAILED + 1
    TESTS_RAN.append(current_test_detail)



# Print all test results and stop script from running if any test failed
def print_test_results(failsafe: bool):
    global TESTS_PASSED
    global TESTS_FAILED
    print("\n--------------------------------------------\n" + \
          str(TESTS_PASSED) + " successful test(s) and " + \
          str(TESTS_FAILED) + " failed test(s)." + \
          "\n--------------------------------------------\n")
    if failsafe and TESTS_FAILED > 0:
        print("Stopping script b/c of failed tests")
        exit()

def verbose_print_test_results():
    global TESTS_FAILED
    global TESTS_RAN

    for test_detail in TESTS_RAN:
        print(test_detail.get_message())

    if TESTS_FAILED > 0:
        print("Stopping script b/c of failed tests")
        exit()

    print_test_results(failsafe=False)


def assert_true(boolean_result, name):
    my_test_detail = TestDetail("True", boolean_result, name)
    global TESTS_PASSED
    global TESTS_FAILED
    global TESTS_RAN
    if not boolean_result:
        print("Error in " + name)
        my_test_detail.set_passed_false()
        TESTS_FAILED = TESTS_FAILED + 1
    else:
        TESTS_PASSED = TESTS_PASSED + 1
    TESTS_RAN.append(my_test_detail)