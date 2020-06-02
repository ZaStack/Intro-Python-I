"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt', 'r') as x:
    file_data = x.read()
    print(file_data)
    x.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'r+') as file:
    file_data = 'Here is my first line of data \n Here is my second line of data \n And here is the third, because I\'m lazy'
    file.write(file_data)
    print(file_data)
    file.close()



