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


