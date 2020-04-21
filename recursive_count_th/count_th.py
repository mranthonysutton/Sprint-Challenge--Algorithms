'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Need a variable that can hold our result
    string_occurence = 0

    # What is our base case? If the lenth of the word is less than 2 character
    # It must return 0
    if len(word) < 2:
        return 0

    # check if the next 2 slices in the array contain "th" and add to a result
    if word[:2] == 'th':
        string_occurence = 1

    # Continue running through the function until we have no more letters
    # We can do this by removing the first letter of the string and checking the next two indices
    # Return the number of the result
    return string_occurence + count_th(word[1:])

print(count_th("now th lets th testh this"))
