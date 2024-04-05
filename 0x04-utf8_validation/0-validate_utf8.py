#!/usr/bin/python3

"""
a method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Helper function to check if a byte is a valid continuation byte
    """
    def isContinuation(byte):
        return (byte & 0b11000000) == 0b10000000
    
    # Iterate through the list of integers
    i = 0
    while i < len(data):
        """
        Get the number of bytes for the current UTF-8 character
        """
        num_bytes = 0
        if (data[i] & 0b10000000) == 0:  # 1-byte character
            num_bytes = 1
        elif (data[i] & 0b11100000) == 0b11000000:  # 2-byte character
            num_bytes = 2
        elif (data[i] & 0b11110000) == 0b11100000:  # 3-byte character
            num_bytes = 3
        elif (data[i] & 0b11111000) == 0b11110000:  # 4-byte character
            num_bytes = 4
        else:
            return False  # Invalid leading byte
        
        # Check if there are enough bytes in the data set for the current character
        if i + num_bytes > len(data):
            return False
        
        """
        Check if subsequent bytes are valid continuation bytes
        """
        for j in range(1, num_bytes):
            if not isContinuation(data[i + j]):
                return False
        
        i += num_bytes
    
    return True

# Example usage:

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
