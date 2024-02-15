# 71. Simplify Path
"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""


class Solution:
    def simplifyPath(self, path):
        stack = []
        arr = path.split("/")

        for i in arr:
            if i == ".." and stack:
                stack.pop()
                i = ""
            elif i == "." or i == "" or i == "..":
                continue
            else:
                stack.append(i)

        return "/" + "/".join(stack)


"""
canonical paths:
(1) path starts with single /
(2) directories separated by /
(3) path doesn't end with /
(4) no periods

.. -> go back

create a stack and add each time you see a /
stack = []

iterate through path.split("/")
  if is alphabetical, add to stack
  if it is . ignore
  if it is .. pop from stack

join stack with "/"
"""
