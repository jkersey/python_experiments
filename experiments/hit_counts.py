#!/usr/bin/python3

def hit_counts(arr):

    count_arr = {}

    for key in arr:
        path = key.split(".")

        for i in range(len(path)):
            if ".".join(path[-i:]) in count_arr:
                count_arr[".".join(path[-i:])] += arr[key]
            else:
                count_arr[".".join(path[-i:])] = arr[key]

    return count_arr

    


hits = { "google.com": 10,
         "mail.google.com": 23,
         "mail.google.co.uk": 4,
         "yahoo.com": 34,
         "mail.yahoo.com": 23,
         "www.yahoo.com": 44,
         "images.yahoo.com": 22,
         }

counts = hit_counts(hits)

for key in counts:
    print(key + " : " + str(counts[key]))

    
                          

