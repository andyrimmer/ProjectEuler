import sys

###################################################################################################

class TriangleOfNumbers(object):
    """
    Represent a triangle of numerical values of the form

         3
        7 4
       2 4 6
      8 5 9 3

    with some utility functions for querying the data
    """
    def __init__(self):
        """
        Use simple list of lists to represent data
        """
        self.data = []

    def get_first_value(self):
        """
        Return the number at the top of the triangle
        """
        return self.data[0][0]

    def add_row(self, row):
        """
        Append a new row of values to the triangle
        """
        if len(self.data) > 0:
            if not len(row) > len(self.data[-1]):
                raise StandardError, "Trying to add row {} to triangle. Last row was {}".format(row, self.data[-1])

        self.data.append(row)

    def get_adjacent_numbers_from_next_row(self, irow, icol):
        """
        Return the numbers which are diagonal to the specified entry in the
        triangle.
        """
        n_rows = len(self.data)

        if irow == n_rows - 1:
            return None
        else:
            return (self.data[irow+1][icol], self.data[irow+1][icol+1])

    def get_max_value_in_row(self, irow):
        return max(self.data[irow])

    def get_max_value_going_into_cell(self, irow, icol):
        """
        Each cell, apart from those on the extreme left and extreme right, can
        have 2 inputs, top-left and top-right. Return the highest value of these 2.
        """
        if irow == 0 and icol == 0: # Starting point
            return 0
        elif icol == 0: # Extreme left
            return self.data[irow-1][icol]
        elif icol + 1 == len(self.data[irow]): # Extreme right
            return self.data[irow-1][icol-1]
        else: # Normal case
            top_left = self.data[irow -1][icol-1]
            top_right = self.data[irow -1][icol]

            return max(top_left, top_right)

###################################################################################################

def loadDataFromFile(file_name):
    """
    Load and return integer triangle
    """
    triangle = TriangleOfNumbers()

    with open(file_name, 'r') as data_file:
        for line in data_file:
            if len(line.strip()) == 0:
                continue
            else:
                cols = line.strip().split()
                new_row = map(int, cols)
                triangle.add_row(new_row)

    return triangle

###################################################################################################

def findMaxPathDownTriangle(triangle):
    """
    Find and return the value of the highest path down the triangle
    """
    dp_table = TriangleOfNumbers()
    n_rows = len(triangle.data)

    for irow in xrange(0,n_rows):
        dp_table.add_row([0]*(irow+1))

    irow = 0
    icol = 0

    for irow in xrange(0, n_rows):
        n_cols = len(triangle.data[irow])

        for icol in xrange(0, n_cols):
            current_value = triangle.data[irow][icol]
            max_value_so_far = dp_table.get_max_value_going_into_cell(irow, icol)
            print current_value, max_value_so_far, current_value + max_value_so_far
            dp_table.data[irow][icol] = current_value + max_value_so_far

    return dp_table.get_max_value_in_row(n_rows-1)

###################################################################################################

file_name = sys.argv[1]
triangle = loadDataFromFile(file_name)
max_value = findMaxPathDownTriangle(triangle)

print "The answer is..."
print max_value
print ""
