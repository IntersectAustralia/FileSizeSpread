# Copyright 2023 Intersect Australia Ltd
# Author: Fivos Kyriakakis
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

#all counters for the file size calculations
counter_10KB = 0
counter_50KB = 0
counter_100KB = 0
counter_1MB = 0
counter_50MB = 0
counter_100MB = 0
counter_500MB = 0
counter_1GB = 0
counter_50GB = 0
counter_50GB_Plus = 0

#to list all files in the directory for all files
entries = os.listdir('../Filesizes')
for entry in entries:
    print(entry)

#creates a user input to select the file that needs to be calculated.
file_to_open = input('choose a file to open (e.g Q1234): ')
fixed_filename = f"./Filesizes/{file_to_open}-filesizes.txt"
contents = open(fixed_filename, 'r')

#goes through the file one line at a time to determine the rough filesize of each line and adds to the counter
for num in contents:
    FileSize = int(num)
    #print("%2d" % (y))

    if FileSize >= 0 and FileSize <= 10000:
        counter_10KB += 1

    elif FileSize >= 10001 and FileSize <= 50000:
        counter_50KB += 1

    elif FileSize >= 50001 and FileSize <= 100000:
        counter_100KB += 1

    elif FileSize >= 100001 and FileSize <= 1000000:
        counter_1MB += 1

    elif FileSize >= 1000001 and FileSize <= 50000000:
        counter_50MB += 1

    elif FileSize >= 50000001 and FileSize <= 100000000:
        counter_100MB += 1

    elif FileSize >= 100000001 and FileSize <= 500000000:
        counter_500MB += 1

    elif FileSize >= 500000001 and FileSize <= 1000000000:
        counter_1GB += 1

    elif FileSize >= 1000000001  and FileSize <= 50000000000:
        counter_50GB += 1

    else:
        counter_50GB_Plus += 1

#prints all results and adds them up at the end to ensure that they match the amount of files that were totally calculated
print("0-10KB:          ",counter_10KB)
print("10-50KB:         ",counter_50KB)
print("51-100KB:        ",counter_100KB)
print("101KB-1MB:       ",counter_1MB)
print("1MB-50MB:        ",counter_50MB)
print("50MB-100MB:      ",counter_100MB)
print("100MB-500MB:     ",counter_500MB)
print("500MB-1GB:       ",counter_1GB)
print("1GB-50GB:        ",counter_50GB)
print("50GB Plus:       ",counter_50GB_Plus)
print("total count:     ",counter_10KB + counter_50KB + counter_100KB + counter_1MB + counter_50MB + counter_100MB + counter_500MB + counter_1GB + counter_50GB + counter_50GB_Plus)
