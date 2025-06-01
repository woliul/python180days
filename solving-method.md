# Problem-Solving Best Practices and Most-Used Methods

The **world’s best problem solvers** (think IOI/IMO/ACM ICPC champions, LeetCode top coders, Google/Facebook engineers, or Nobel/Turing-awarded mathematicians) follow a **set of principles and favorite methods** that go beyond coding syntax.

Here’s a distilled list of **Best Practices** and **Most-Used Methods**, broken down by top-tier problem solvers — **with deep explanations and processes to use them**.

---

## 🧠 PART 1: Best Practices of Elite Problem Solvers

| #  | Best Practice                          | Why It's Effective                                                                 | How to Use / Process                                                                                                |
| -- | -------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 1  | **Understand the Problem Fully First** | Elite coders spend more time reading & analyzing than typing. Misreading is fatal. | Read problem carefully → Highlight key constraints → Restate in your own words → Ask clarifying questions if needed |
| 2  | **Work Out Small Cases by Hand**       | Gives intuition about patterns, edge cases, or formulas.                           | Take example inputs → Solve manually step-by-step → Note patterns, exceptions, or potential pitfalls                |
| 3  | **Simplify the Problem**               | Break it into simpler sub-problems or a base version.                              | Identify core components → Solve simpler version first → Gradually add complexity                                   |
| 4  | **Think Before You Code**              | Sketch logic or pseudocode. Saves debugging later.                                 | Write pseudocode or flowchart → Discuss algorithm verbally or on paper before implementation                        |
| 5  | **Use Proven Patterns**                | Like sliding window, two pointers, or divide and conquer.                          | Map problem features to known patterns → Choose and adapt the pattern accordingly                                   |
| 6  | **Optimize Only After It's Correct**   | First make it work, then make it fast.                                             | Implement straightforward solution → Test correctness → Profile and optimize bottlenecks                            |
| 7  | **Know Your Tools (STL, libraries)**   | Experts don’t reinvent sorting, heaps, sets — they **use them**.                   | Identify standard data structures/libraries relevant to problem → Use them instead of custom code                   |
| 8  | **Code Cleanly & Modularly**           | Easy to debug, test, and change.                                                   | Write functions/modules → Use clear variable names → Comment tricky parts → Keep code readable                      |
| 9  | **Test Edge Cases**                    | 0, 1, max, empty, duplicates, sorted, reverse-sorted.                              | Prepare test suite including edge and corner cases → Run all tests regularly                                        |
| 10 | **Practice Regularly, Reflect Deeply** | Solve, but also **review why you were wrong or slow.**                             | After solving, analyze mistakes/difficulties → Study faster/better solutions → Repeat with similar problems         |

---

## 🔍 PART 2: Most Used Problem-Solving Methods (with How to Use Them)

### 1. **Brute Force First**

* **Why it works:** Gives a guaranteed correct solution for small inputs.
* **Use it for:** Validating your idea, building test cases.
* **How to use:**

  1. Identify all possible solutions (even if slow).
  2. Implement naive solution quickly.
  3. Use outputs to verify optimized methods.
* ✅ Good for starting
* ❌ Bad for performance on large inputs

---

### 2. **Greedy Algorithms**

* **Idea:** At each step, pick the locally best choice.
* **Best when:** Problem exhibits greedy-choice property.
* **How to use:**

  1. Confirm problem’s greedy property (e.g., proof or intuition).
  2. Sort or prioritize choices if needed.
  3. Iteratively pick best local option → Build solution.
  4. Check if solution is optimal.
* ✅ Fast
* ❌ Doesn’t always give optimal result

---

### 3. **Two Pointers / Sliding Window**

* **When to use:** Arrays, subarrays, substrings with constraints.
* **How to use:**

  1. Initialize two pointers (start/end).
  2. Move one pointer forward while maintaining condition.
  3. Adjust other pointer as needed to keep valid window.
  4. Track max/min values or counts during traversal.
* ✅ O(n) instead of O(n²)

---

### 4. **Binary Search (on answer)**

* **Use:** When answer lies in a numeric range and predicate is monotonic.
* **How to use:**

  1. Define search range for the answer.
  2. Implement a predicate function that returns true/false.
  3. Binary search over range to find boundary where predicate changes.
* ✅ Fast (O(log range))

---

### 5. **Prefix Sum / Difference Array**

* **Use:** Fast range queries.
* **How to use:**

  1. Precompute prefix sums or difference arrays.
  2. Use prefix sums to answer queries in O(1).
* ✅ Speeds up cumulative queries drastically.

---

### 6. **Dynamic Programming (DP)**

* **When to use:** Overlapping subproblems + optimal substructure.
* **How to use:**

  1. Define state representing subproblem.
  2. Write recurrence relation.
  3. Choose top-down (memo) or bottom-up approach.
  4. Implement with careful indexing.
  5. Test base cases and transitions.
* ✅ Most powerful technique for state-based problems

---

### 7. **Graph Algorithms (BFS/DFS, Dijkstra, Union-Find)**

* **When to use:** Connectivity, shortest paths, grouping.
* **How to use:**

  1. Model problem as graph.
  2. Choose algorithm based on graph type and goal (DFS for traversal, BFS for shortest unweighted path, Dijkstra for weighted).
  3. Implement or use library functions.
* ✅ Core in contests and real systems

---

### 8. **Backtracking**

* **Use:** Search space with pruning.
* **How to use:**

  1. Define recursive function that tries choices.
  2. Prune invalid or suboptimal branches early.
  3. Track partial solution and undo changes when backtracking.
* ✅ Elegant, powerful

---

### 9. **Bitmasking**

* **Use:** Compactly represent sets.
* **How to use:**

  1. Encode subsets as integers with bits representing elements.
  2. Use bitwise operations to add/remove/check elements.
  3. Combine with DP or brute force for state reduction.
* ✅ Cool trick to reduce space/time

---

### 10. **Mathematical Thinking**

* **Use:** Number theory, combinatorics, algebraic insights.
* **How to use:**

  1. Recognize math patterns or formulas.
  2. Apply GCD, modular arithmetic, combinatorics as needed.
  3. Use precomputation like sieve for primes.
* ✅ Essential for many contests and algorithmic problems

---

## 🧠 PART 3: Mindsets of Top Problem Solvers

| Mindset                     | Description                                        | How to Cultivate                                                  |
| --------------------------- | -------------------------------------------------- | ----------------------------------------------------------------- |
| **Curiosity**               | Ask "Why does this work?" not just "Does it work?" | Always seek understanding → Question solutions and proofs         |
| **Pattern Recognition**     | Connect new problems with familiar ones            | Solve diverse problems → Review solutions → Identify similarities |
| **Resilience**              | Treat failure as learning, not defeat              | Keep trying → Analyze failures → Maintain growth mindset          |
| **Abstraction**             | Reduce problems to core ideas                      | Strip unnecessary detail → Focus on essential constraints         |
| **Speed Through Structure** | Organize approach instead of rushing               | Plan → Prioritize tasks → Avoid careless haste                    |

---

## 🏁 Summary Table of Methods (with Usage Process)

| Method          | Use Case Example                  | Time Benefit  | How to Use / Process Summary                                    |
| --------------- | --------------------------------- | ------------- | --------------------------------------------------------------- |
| Brute Force     | Try everything                    | ❌ Slow        | Implement naive solution → Use for validation/test cases        |
| Greedy          | Scheduling, interval problems     | ✅ Fast        | Verify greedy property → Pick best local option iteratively     |
| Two Pointers    | Subarrays, strings                | ✅ O(n)        | Use two indices to maintain window → Move to keep conditions    |
| Binary Search   | Threshold problems, sorted arrays | ✅ O(log n)    | Define search range and predicate → Binary search for answer    |
| Prefix Sum      | Range sums                        | ✅ O(1)        | Precompute prefix sums → Answer queries with O(1) operations    |
| DP              | State problems, optimization      | ✅ Optimal     | Define states & recurrences → Memoize or tabulate results       |
| Graph (BFS/DFS) | Connectivity, shortest paths      | ✅ Essential   | Model graph → Apply correct traversal/shortest path algorithm   |
| Union-Find      | Component grouping                | ✅ Fast        | Use union-find to manage disjoint sets efficiently              |
| Backtracking    | Search with undo                  | ❌ Exponential | Recursive exploration → Prune branches to limit search          |
| Bitmasking      | Subsets, flags, DP state          | ✅ Compact     | Encode sets as bits → Use bit operations to manage states       |
| Math            | GCD, Primes, Modulo               | ✅ Clean       | Apply mathematical formulas and theorems → Use precomputed data |

---

Let’s walk through each **problem-solving method**, explaining its core idea **plus a step-by-step pseudo-process** you can follow to use it effectively on *any* problem.

## 1. Brute Force First

### What it is:

Try all possible solutions (or a large subset) in a straightforward way, even if it’s slow. This guarantees correctness on small inputs and helps understand the problem.

---

### How to use Brute Force (Pseudo-process):

1. **Understand problem constraints and input size.**
   If small or moderate, brute force might be feasible.

2. **Enumerate all possible candidate solutions.**

   * Think: Can I try all subsets? All pairs? All permutations?
   * Usually nested loops over input elements.

3. **For each candidate, check if it satisfies problem requirements.**

   * Implement the simplest check possible.

4. **Keep track of best or valid solution found.**

5. **Return the final answer after all candidates checked.**

---

### Pseudo-code sketch

```pseudo
best_solution = NULL
for candidate in all_possible_candidates:
    if is_valid(candidate):
        best_solution = update_if_better(best_solution, candidate)
return best_solution
```

---

### When to use it

* To verify correctness before optimizing.
* When input size is small enough.
* When stuck and need a baseline solution.

---

## 2. Greedy Algorithms

### What it is:

At every step, pick the choice that looks the best *right now* (locally optimal), hoping this leads to a globally optimal solution.

---

### How to use Greedy (Pseudo-process):

1. **Confirm the problem has a “greedy-choice property.”**

   * The locally best choice at each step leads to a globally optimal solution.
   * Sometimes requires proof or logical reasoning.

2. **Sort or prioritize input if needed.**

   * Many greedy solutions depend on sorting data first.

3. **Initialize an empty solution or data structure.**

4. **Iterate through the input:**

   * At each step, pick the “best” choice available according to the problem’s criteria.
   * Update the solution accordingly.

5. **Return the constructed solution.**

---

### Pseudo-code sketch

```pseudo
sort(input)  // if required by problem
solution = empty
for element in input:
    if choosing element is valid and improves solution:
        add element to solution
return solution
```

---

### When to use it

* Scheduling tasks (e.g., interval scheduling).
* Minimizing cost with immediate local decisions.
* Huffman coding, activity selection, coin change (with certain denominations).

---

## 3. Two Pointers / Sliding Window

### What it is:

Use two indices (pointers) moving through a sequence (array/string) to maintain a window or pair of elements satisfying certain conditions efficiently.

---

### How to use Two Pointers / Sliding Window (Pseudo-process):

1. **Identify problem requires finding a subarray or substring with certain properties**

   * Example: longest substring without repeats, max sum subarray ≤ k.

2. **Initialize two pointers:**

   * `start = 0`, `end = 0` (beginning of window).

3. **Expand window by moving `end` forward:**

   * Include new elements, update any running counts/sums/state.

4. **While window violates constraints:**

   * Move `start` forward to shrink window until valid again.

5. **Keep track of best window found so far during iterations.**

6. **Return result after iterating through array/string.**

---

### Pseudo-code sketch

```pseudo
start = 0
best_result = initial_value
for end in range(0, length_of_array):
    include element at end in window_state
    while window_state violates condition:
        remove element at start from window_state
        start += 1
    update best_result using current window
return best_result
```

---

### When to use it

* Subarray or substring problems with constraints on size, sum, distinct elements, etc.
* When a naive O(n²) approach tries all windows but is too slow.

---

## 4. Binary Search (on answer)

### What it is:

A divide-and-conquer technique to find an answer within a numeric range by repeatedly narrowing down where a predicate switches from false to true (or vice versa).

---

### How to use Binary Search on Answer (Pseudo-process):

1. **Identify the problem asks for a numeric answer that lies within a known range.**
   Examples: minimum max distance, minimum speed, max capacity.

2. **Define a predicate function `can_achieve(x)` that returns:**

   * `True` if solution is possible with candidate answer `x`.
   * `False` otherwise.

3. **Set initial search range:**

   * `low` = minimum possible answer.
   * `high` = maximum possible answer.

4. **While `low < high`:**

   * Compute `mid = (low + high) // 2`.
   * If `can_achieve(mid)` is true, try to find a better (lower) answer by setting `high = mid`.
   * Else, set `low = mid + 1`.

5. **Return `low` (or `high`) as the answer after the loop finishes.**

---

### Pseudo-code sketch

```pseudo
low = min_possible_answer
high = max_possible_answer
while low < high:
    mid = (low + high) // 2
    if can_achieve(mid):
        high = mid
    else:
        low = mid + 1
return low
```

---

### When to use it

* When the answer is numeric and you can check feasibility quickly.
* When the problem has monotonicity — if answer `x` works, all answers > `x` (or < `x`) also work.

---

## 5. Prefix Sum / Difference Array

### What it is:

Precompute cumulative sums or differences so you can answer range queries (like sum, count) in O(1) time instead of recomputing every time.

---

### How to use Prefix Sum (Pseudo-process):

1. **Given an array, create a prefix sum array `prefix` where:**

   * `prefix[0] = 0`
   * `prefix[i] = prefix[i-1] + arr[i-1]` for `i` from 1 to n

2. **To get the sum of a subarray `arr[l..r]`:**

   * Compute `sum = prefix[r+1] - prefix[l]`

3. **For difference arrays (when updating ranges frequently):**

   * Create an array to store differences.
   * Apply increments/decrements to ranges by updating difference array boundaries.
   * Recompute prefix sums to get final values.

---

### Pseudo-code sketch

```pseudo
// Precompute prefix sums
prefix[0] = 0
for i in range(1 to n):
    prefix[i] = prefix[i-1] + arr[i-1]

// Query sum from l to r
sum_subarray = prefix[r+1] - prefix[l]
```

---

### When to use it

* When multiple queries ask for sums/counts over subranges.
* When frequent range updates require efficient computation.
* Common in competitive programming and data compression problems.

---

## 6. Dynamic Programming (DP)

### What it is:

A technique to solve problems by breaking them down into overlapping subproblems and storing their results to avoid repeated work.

---

### How to use Dynamic Programming (Pseudo-process):

1. **Identify if the problem has:**

   * **Optimal substructure:** The solution can be built from solutions of smaller subproblems.
   * **Overlapping subproblems:** Same subproblems appear multiple times.

2. **Define the state(s):**

   * Decide what parameters uniquely define a subproblem.
   * Example: `dp[i]` = best solution using first `i` elements, or `dp[i][j]` = solution considering elements `i` to `j`.

3. **Define the recurrence relation:**

   * Express the solution of a state in terms of smaller states.

4. **Set base cases:**

   * Initialize dp states for simplest cases.

5. **Choose a computation order:**

   * Bottom-up: compute from base cases up to the final answer.
   * Or top-down with memoization.

6. **Return the dp value representing the solution to the original problem.**

---

### Pseudo-code sketch (Bottom-up example for Fibonacci)

```pseudo
dp[0] = 0
dp[1] = 1
for i in range(2 to n):
    dp[i] = dp[i-1] + dp[i-2]
return dp[n]
```

---

### When to use it

* Problems involving sequences, subsets, optimization with overlapping subproblems.
* Classic examples: Fibonacci, Knapsack, Longest Increasing Subsequence, Coin Change.

---

## 7. Graph Algorithms (BFS/DFS, Dijkstra, Union-Find)

### What it is:
Algorithms to explore, analyze, and solve problems modeled as graphs (nodes and edges).

### A. BFS (Breadth-First Search)

**When to use:**

* Shortest path in unweighted graphs
* Level order traversal
* Connectivity checks
* Example problems: shortest path in a maze, minimum steps to reach target

**Pseudo-process:**

1. Initialize a queue and add the starting node.
2. Mark the starting node as visited.
3. While queue not empty:

   * Dequeue node `u`.
   * For each neighbor `v` of `u`:

     * If `v` not visited, mark visited, enqueue `v`.
4. Optionally, track distance or path info.

**Pseudo-code:**

```pseudo
queue = new Queue()
visited = set()
distance = array with default infinity
queue.enqueue(start)
visited.add(start)
distance[start] = 0

while not queue.is_empty():
    u = queue.dequeue()
    for v in neighbors(u):
        if v not in visited:
            visited.add(v)
            distance[v] = distance[u] + 1
            queue.enqueue(v)
```

---

### B. DFS (Depth-First Search)

**When to use:**

* Exploring all paths or connected components
* Cycle detection
* Topological sorting
* Example problems: detect cycles in a graph, generate permutations via backtracking

**Pseudo-process:**

1. Start at node `u`.
2. Mark `u` as visited.
3. For each neighbor `v` of `u`:

   * If `v` not visited, recursively DFS on `v`.
4. Optionally perform operations before/after recursion (e.g., for topological sort).

**Pseudo-code (recursive):**

```pseudo
function DFS(u):
    visited.add(u)
    for v in neighbors(u):
        if v not in visited:
            DFS(v)
```

---

### C. Dijkstra’s Algorithm

**When to use:**

* Shortest paths on weighted graphs with non-negative weights
* Examples: GPS navigation, network routing

**Pseudo-process:**

1. Initialize `distance[]` array with infinity; distance to source = 0.
2. Use a priority queue (min-heap) to store `(distance, node)`.
3. While queue not empty:

   * Extract node `u` with smallest distance.
   * For each neighbor `v` of `u`:

     * Calculate new distance = `distance[u] + weight(u,v)`.
     * If new distance < `distance[v]`, update `distance[v]` and add to queue.

**Pseudo-code:**

```pseudo
distance = array with infinity
distance[source] = 0
pq = new PriorityQueue()
pq.insert((0, source))

while not pq.is_empty():
    (dist_u, u) = pq.extract_min()
    if dist_u > distance[u]:
        continue
    for v in neighbors(u):
        alt = dist_u + weight(u,v)
        if alt < distance[v]:
            distance[v] = alt
            pq.insert((alt, v))
```

---

### D. Union-Find (Disjoint Set Union)

**When to use:**

* Finding connected components
* Cycle detection in undirected graphs
* Kruskal’s MST algorithm
* Examples: network connectivity, grouping similar items

**Pseudo-process:**

1. Initialize parent and rank arrays for each node (each node is its own set).
2. Define functions:

   * `find(x)`: returns representative of x’s set (with path compression).
   * `union(x, y)`: merges sets of x and y if different (by rank).
3. For each edge `(u, v)`:

   * If `find(u) != find(v)`, union sets.
   * Else, edge creates a cycle (if detecting cycles).

**Pseudo-code:**

```pseudo
function find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

function union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

// usage:
for (u,v) in edges:
    if find(u) != find(v):
        union(u,v)
    else:
        // cycle detected
```

---

## 8. Backtracking

### What it is:

A systematic way to try all possible options by exploring choices step-by-step and **undoing** (“backtracking”) choices that lead to dead ends.

---

### How to use Backtracking (Pseudo-process):

1. **Define your decision tree:**

   * Each level corresponds to a choice to make.

2. **Create a recursive function that:**

   * Checks if the current partial solution is valid or complete.
   * If complete, records or outputs the solution.
   * Otherwise, tries all possible next steps (choices).

3. **For each choice:**

   * Make the choice (update state).
   * Recurse to next level.
   * Undo the choice (backtrack) to explore other possibilities.

---

### Pseudo-code sketch

```pseudo
function backtrack(state):
    if solution_complete(state):
        record_solution(state)
        return
    for choice in possible_choices(state):
        if choice is valid:
            make_choice(state, choice)
            backtrack(state)
            undo_choice(state, choice)
```

---

### When to use it

* Problems requiring exploring **all** configurations or subsets.
* Examples:

  * Sudoku solver
  * N-Queens problem
  * Generating permutations or combinations
  * Constraint satisfaction problems

---


## 9. Bitmasking

### What it is:

Using bits in an integer to represent sets or flags, allowing compact representation and efficient manipulation of subsets and states.

---

### How to use Bitmasking (Pseudo-process):

1. **Represent a set of elements using an integer (bitmask):**

   * Each bit corresponds to presence (1) or absence (0) of an element.
   * For example, if you have n elements, bit `i` represents element `i`.

2. **Iterate over subsets by incrementing a bitmask from 0 to 2^n - 1.**

3. **Use bitwise operators to:**

   * Check if element `i` is in the set: `(mask & (1 << i)) != 0`
   * Add element `i`: `mask | (1 << i)`
   * Remove element `i`: `mask & ~(1 << i)`
   * Toggle element `i`: `mask ^ (1 << i)`

4. **Use bitmask as DP state or to generate subsets efficiently.**

---

### Pseudo-code sketch (Generating all subsets of set {0,1,...,n-1})

```pseudo
for mask in range(0 to (1 << n) - 1):
    subset = []
    for i in range(0 to n-1):
        if (mask & (1 << i)) != 0:
            subset.append(i)
    process(subset)
```

---

### When to use it

* Problems involving subsets, combinations, or states with up to \~20 elements.
* DP problems with states that can be encoded as subsets.
* Example: Traveling Salesman Problem (TSP), subset sum, scheduling problems.

---

## 10. Mathematical Thinking

### What it is:

Using math insights, formulas, and number theory to simplify, optimize, or solve problems efficiently.

---

### How to use Mathematical Thinking (Pseudo-process):

1. **Analyze the problem for known math concepts:**

   * Patterns, sequences, divisibility, primes, combinatorics, modular arithmetic.

2. **Apply relevant formulas or theorems:**

   * For example, use GCD for simplifying fractions or Euclid’s algorithm to find the greatest common divisor.
   * Use combinatorial formulas to count arrangements without brute force.

3. **Use mathematical properties to reduce computation:**

   * For instance, properties of modulo to handle large numbers.
   * Use Sieve of Eratosthenes to find primes efficiently.

4. **Translate the problem into a math expression and solve it.**

---

### Pseudo-code sketch (Example: Compute GCD using Euclid’s Algorithm)

```pseudo
function gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
```

---

### When to use it

* Problems involving divisibility, prime numbers, counting, probability, or geometry.
* Classic examples:

  * Calculating GCD/LCM
  * Counting combinations/permutations
  * Modular exponentiation in cryptography
  * Number theory problems in contests

---

