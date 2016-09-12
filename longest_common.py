def longest_common_substring(str1, str2):
    """Gets two strings as input and returns longest common substring"""
    if len(str1) > len(str2):
        str1, str2 = (str2, str1)
    length = len(str1)
    while length > 0:
        for i in range(len(str1)-length + 1):
            if str1[i:i+length] in str2:
                return str1[i:i+length]
        length -= 1
    print('No match was found.')
