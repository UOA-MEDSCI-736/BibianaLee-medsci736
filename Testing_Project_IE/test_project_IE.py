from project_IE import * #import all the functions from project_IE


#READ THE README BEFORE TRYING OUT TESTS


file = open('Testing_Data', 'r') #test file for the append values test
lines = [] #list for the append values to lines function 

#checking to see that function removing #, blank lines and separating at ','
#need to remove "#" from line 64 in order for test to pass
def test_append_values_to_lines(): 
	assert append_values_to_lines(file) == [['aif', '0', '0.914', '1.115', '1.235', '1.225', '1.218', '1.122', '1.106', '1.192', '1.017', '1.214']]

#checking user input for main menu
#When function expects a value it should pass
def test__input_expected_values(): 
	assert check_the_user_input(['1', '2'], '1') == '1'
#when the function does not have the string value in the expected values it is expected to return a 0 and bring up error message for user
def test__input_unexpected1(): 
	assert check_the_user_input([1, 2], '2') == 0
#when the function does not have the number in the expected values it is expected to return 0 and bring up an error message for user
def test__input_unexpected2():
	assert check_the_user_input(['1', '2'], 2) == 0

#Checking user input for secondary input values 
#testing with expected values 
#when function can recognize the value and the type of value it will pass 
def test__input_expected_values_secondary():
	assert check_the_user_input_secondarymenu(["1", "2", "3"], "3") == "3"

def test__input_expected_values2_secondary():
	assert check_the_user_input_secondarymenu([1,2,3], 3) == 3

#testing with unexpected values 
#when the values in the [list] do not match the value on the outside then it should return a 0 and bring up an error message for the user - this test ensures that this function is working 
def test_input_unexpected_values1_secondary(): 
	assert check_the_user_input_secondarymenu([1,2,3], "2") == 0

def test_user_input_unexpected_values2_secondary():
	assert check_the_user_input_secondarymenu([3,4,5,6], 2) == 0

def test_user_input_unexpected_values3_secondary():
    assert check_the_user_input_secondarymenu([1,2,3], 500) == 0


