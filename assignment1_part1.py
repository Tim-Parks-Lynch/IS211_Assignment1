class List_Divide_Exception(Exception):
    def __init__(self, message = "Assertion Error in list_divide"):
        self.message = message

    def __str__(self):
        return f'{self.message} - made by Tim'

def list_divide(numbers, divide = 2):
    """
    The function returns the number of elements in the numbers list that are divisible by divide
    :param numbers: List(array in JS) of numbers
    :param divide: Number to divide list[i] by, default = 2
    """
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count

def test_list_divide():
    """
    Test listDivide
    """
    try:
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        assert list_divide([30, 54, 63,98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5
    except AssertionError as e:
        raise List_Divide_Exception(e) from None
    else: 
        print('No errors: All Assertion Tests pass')
    
if __name__ == "__main__":
    test_list_divide()
