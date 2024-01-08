from collections import deque


# depth first values
def depth_first_values(root):
    """depth first values"""
    if not root:
        return []

    left = depth_first_values(root.left)
    right = depth_first_values(root.right)
    return [root.val, *left, *right]


# * acts like spread operator, but also can do extended unpacking(capture excess items) or do keyword argument unpacking(unpack dictionaries into args for functions)
first, *middle, last = [1, 2, 3, 4, 5]
print("first ", first)
print("middle", middle)
print("last", last)


def printer(a, b, c):
    """prints arguments"""
    print(a, b, c)


args = {"a": 1, "b": 2, "c": 3}
printer(**args)


# breadth first values
def breadth_first_values(root):
    """breadth first values"""
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:  # pop from left <---- [ queue ] <---- append from right
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return values


# tree sum
def tree_sum(root):
    """finds sum of all roots in tree"""
    if not root:
        return 0
    queue = deque([root])
    total = 0

    while queue:
        current = queue.popleft()
        total += current.val

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return total


# tree includes
def tree_includes(root, target):
    """look for instance of target in tree"""
    if not root:
        return False

    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)


# tree min value
def tree_min_value(root):
    minimum = float("inf")
    queue = deque([root])

    while queue:
        current = queue.popleft()
        minimum = min(minimum, current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return minimum


# max root to leaf path
def max_path_sum_1(root):
    maximum = float("-inf")

    def dfs(root, current_sum):
        nonlocal maximum
        if root is None:
            return

        current_sum = sum + root.val

        if not root.left and not root.right:
            maximum = max(maximum, current_sum)

        dfs(root.left, current_sum)
        dfs(root.right, current_sum)

    dfs(root, 0)
    return maximum


def max_path_sum(root):
    if not root:
        return float("-inf")

    if not root.left and not root.right:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


# tree path finder
def path_finder(root, target):
    if not root:
        return None

    if root.val == target:
        return [root.val]

    left_path = path_finder(root.left, target)
    if left_path:
        return [root.val, *left_path]

    right_path = path_finder(root.right, target)
    if right_path:
        return [root.val, *right_path]

    return None


# tree value count
def tree_value_count_recurisve(root, target):
    if not root:
        return 0

    match = 1 if root.val == target else 0

    return (
        match
        + tree_value_count_recurisve(root.left, target)
        + tree_value_count_recurisve(root.right, target)
    )


def tree_value_count_iterative(root, target):
    if not root:
        return 0
    queue = [root]
    sum = 0
    while queue:
        current = queue.pop()
        if current.val == target:
            sum += 1

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return sum


# how high
def how_high(node):
    if not node:
        return -1
    maximum = -1

    def dfs(node, height):
        nonlocal maximum
        if not node:
            return
        maximum = max(maximum, height)
        dfs(node.left, height + 1)
        dfs(node.right, height + 1)

    dfs(node, 0)
    return maximum


def how_high_recursive(node):
    if not node:
        return -1

    left_height = how_high(node.left)
    right_height = how_high(node.right)

    return 1 + max(left_height, right_height)


# bottom right value
def bottom_right_value(root):
    queue = deque([root])
    current = None

    while queue:
        current = queue.popleft()

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return current


# all tree paths
def all_tree_paths(root):
    final = []

    def dfs(root, slate):
        if not root:
            return
        new_path = slate + [root.val]
        if not root.left and not root.right:
            final.append(new_path)
            return

        dfs(root.left, new_path)
        dfs(root.right, new_path)

    dfs(root, [])
    return final


def all_tree_paths_2(root):
    if not root:
        return []

    if not root.left and not root.right:
        return [[root.val]]

    paths = []

    left_sub_paths = all_tree_paths(root.left)
    for sub_path in left_sub_paths:
        paths.append([root.val, *sub_path])
    right_sub_paths = all_tree_paths(root.right)
    for sub_path in right_sub_paths:
        paths.append([root.val, *sub_path])

    return paths


# tree levels
def tree_levels(root):
    if not root:
        return []

    final = []
    current_queue = deque([root])
    next_queue = deque()

    while current_queue or next_queue:
        slate = []
        while current_queue:
            current = current_queue.popleft()
            slate.append(current.val)
            if current.left:
                next_queue.append(current.left)
            if current.right:
                next_queue.append(current.right)
        final.append(slate)
        current_queue, next_queue = next_queue, deque()

    return final


def tree_levels_recursive(root):
    levels = []

    def dfs(root, levels, level_num):
        if not root:
            return

        if level_num == len(levels):
            levels.append([root.val])
        else:
            levels[level_num].append(root.val)

        dfs(root.left, levels, level_num + 1)
        dfs(root.right, levels, level_num + 1)

    dfs(root, levels, 0)
    return levels


# level averages
def level_averages(root):
    if not root:
        return []

    final = []
    current_queue = deque([root])
    next_queue = deque()

    while current_queue:
        slate = []
        while current_queue:
            current = current_queue.popleft()
            slate.append(current.val)

            if current.left:
                next_queue.append(current.left)
            if current.right:
                next_queue.append(current.right)
        final.append(sum(slate) / len(slate))
        current_queue, next_queue = next_queue, deque()

    return final


# leaf list
def leaf_list(root):
    if not root:
        return []
    final = []
    queue = deque([root])

    while queue:
        current = queue.pop()
        if not current.left and not current.right:
            final.append(current.val)
            continue

        if current.right:
            queue.append(current.right)
        if current.left:
            queue.append(current.left)

    return final
