'''
Problem: Longest absolute path
From: Daily Coding Problem 19/09/2019

Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters)
absolute path to a file within our file system. For example,
in the second example above, the longest absolute path is
"dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes)

Given a string representing the file system in the above format,
return the length of the longest absolute path to a file in theabstracted file system.
If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
'''

from collections import deque

class DirFile:
  def __init__(self, name, parent = None):
    self.name = name
    self.parent = parent

  def __str__(self):
    if self.parent == None:
      return self.name
    else:
      return str(self.parent) + "/" + self.name

def longest_path(path):
  path_split = path.split('\n')
  dir_stack = deque()
  files_found = []
  indent = 0
  dir_stack.append(DirFile(path_split[0], None))
  for token in path_split:
    token_split = token.split('\t')
    curr = len(token_split) - 1

    # Check how far in we are indented compared to the last time, 
    # if it is the same indentation, we pop the stack
    # (knowing we push to the stack at the end of
    # EVERY visited sub-directory/file)
    # drop the indent if it has to and pop the directory stack
    # as we go, careful as to not change directory too much
    # no popping occur if we are in a new level of subdirectory
    # eg inside the previous explored folder
    while curr <= indent:
      dir_stack.pop()
      if curr - 1 != indent:
        indent -= 1
    indent = curr

    # let parent be the last item in the stack (or None if stack empty)
    parent = None
    if dir_stack:
      parent = dir_stack[-1]
    df = DirFile(token_split[curr], parent)
    dir_stack.append(df)

    # handle files
    # if a dot is in the name, assume file
    # and add to list of directories
    if '.' in str(df):
      files_found.append(df)
    print('[', len(str(df)), ']', df, sep='')  # prints out directory names and their lengths
  
  # retrieve longest file by doing a linear search on found files
  longest = 0
  for f in files_found:
    fname = str(f)
    if len(fname) > longest:
      longest = len(fname)
  return longest

print(longest_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

# tests:
print(longest_path("root.txt"))
print(longest_path("root\n\tlonglonglonglonglonglongfilename.txt\n\tshort\n\t\tshortfile.txt\nrootfile.txt"))
print(longest_path("dir"))
print(longest_path("dir\n\tsubdir1\n\t\tsubsubdir\n\tsubdir2\nrootdir2nofiles"))