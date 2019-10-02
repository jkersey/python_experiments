#!/usr/bin/python3

def longest_common_path(path1, path2):

    start_range = 0
    end_range = 0

    left_edge_found = False
    right_edge_found = False

    longest_path = []
    current_path = []

    for i in range(len(path2)):
        for j in range(len(path1)):
            if path2[i] == path1[j]:
                
                current_path = []
                
                start_needle = j
                end_needle = j

                start_haystack = i
                end_haystack = i

                left_edge_found = False
                right_edge_found = False
                                
                while not left_edge_found and not right_edge_found:
                    
                    if not left_edge_found:
                        if start_needle > 0 and start_haystack > 0:
                            start_needle -= 1
                            start_haystack -= 1
                            if path1[start_needle] != path2[start_haystack]:
                                left_edge_found = True
                                start_needle += 1
                        else:
                            left_edge_found = True

                    if not right_edge_found:
                        if end_needle < len(path1) - 1 and end_haystack < len(path2) - 1:
                            end_needle += 1
                            end_haystack += 1
                            if path1[end_needle] != path2[end_haystack]:
                                end_needle -= 1
                                right_edge_found = True
                        else:
                            right_edge_found = True
                  
                    current_path = path1[start_needle:end_needle + 1]
                    
                if len(current_path) > len(longest_path):
                    longest_path = current_path
                    

    return longest_path

                    

path1 = ['one', 'two', 'three', 'five', 'six']
path2 = ['zero', 'one', 'two', 'three', 'five', 'six']
print(*['one', 'two', 'three', 'five', 'six'])
print(*longest_common_path(path1, path2))
print()

path1 = ['one', 'two', 'three', 'five', 'zero']
path2 = ['zero', 'one', 'two', 'three', 'five', 'six']
print(*['one', 'two', 'three', 'five'])
print(*longest_common_path(path1, path2))
print()

path1 = ['zero', 'one', 'two', 'three', 'four']
path2 = ['zero', 'one', 'two', 'three', 'five', 'six']
print(*['zero', 'one', 'two', 'three'])
print(*longest_common_path(path1, path2))
print()

path1 = ['one', 'two', 'three', 'four', 'six', 'seven', 'eight', 'nine']
path2 = ['zero', 'one', 'two', 'three', 'five', 'six', 'seven', 'eight', 'nine']
print(*['six', 'seven', 'eight', 'nine'])
print(*longest_common_path(path1, path2))
print()

path1 = ['one', 'two', 'three', 'four', 'one', 'two', 'three', 'five']
path2 = ['zero', 'one', 'two', 'three', 'five', 'six']
print(*['one', 'two', 'three', 'five'])
print(*longest_common_path(path1, path2))
print()



                        

                       
    

