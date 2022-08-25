import string

def print_rangoli(size):
    # your code goes here
    alp = list(string.ascii_lowercase)
    
    x = alp[size - 1 ]
    l = (size * 2) - 1
    w = l + (l - 1)


    ref_str = ''
    list_of_strings = []
    for i in range(1, size + 1):
        # Get the new letter to place at the center
        letter = alp[size - i]
        
        # Print the reference string
        # print(f'ref is {ref_str}')

        # We use div to split the reference string
        if i != 1:
            # print(letter)
            # print(x)
            div = len(ref_str) // 2
            new_str = f'{ref_str[:div + 1]}-' + f'{letter}' + f'-{ref_str[div: ]}'
        else:
            
            div = 1
        
            new_str = f'{letter}'
            # print(new_str)

        # Assign a new string
        ref_str = new_str
        final_string = new_str.center(w, '-')
        list_of_strings.append(final_string)

    for item in list_of_strings:
        print(item)

    for item in list_of_strings[-2::-1]:
        
        print(item)
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)