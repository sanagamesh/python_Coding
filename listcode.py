# interview_practice.py
# 20 Python interview examples (minimal builtins), with tests and short explanations.

# -------------------------
# 1. Reverse a string
def reverse_string(s):
    res = ""
    for ch in s:
        res = ch + res
    return res

# Explanation: Build the reversed string by prepending each char.
# Interview line: "I reverse by iterating and prepending characters to a result string."

# -------------------------
# 2. Palindrome check (two-pointer)
def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# Explanation: Two-pointer comparison from both ends.
# Interview line: "I use two pointers from both ends to check equality without extra memory."

# -------------------------
# 3. Count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        for v in vowels:
            if ch == v:
                count += 1
                break
    return count

# Explanation: Manual membership check in a vowel string.
# Interview line: "I loop characters and check against vowel list, counting matches."

# -------------------------
# 4. Anagram check (frequency maps)
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1
    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1
    if len(freq1) != len(freq2):
        return False
    for k in freq1:
        if freq2.get(k, 0) != freq1[k]:
            return False
    return True

# Explanation: Build frequency dicts for both strings and compare.
# Interview line: "I compare character counts from both strings to confirm anagram."

# -------------------------
# 5. Character frequency
def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

# Explanation: Manual counting using a dict.
# Interview line: "I traverse the string and increment counts in a dictionary."

# -------------------------
# 6. Second largest (single pass)
def second_largest(nums):
    if len(nums) < 2:
        raise ValueError("Need at least two numbers")
    first = second = None
    for n in nums:
        if first is None or n > first:
            second = first
            first = n
        elif n != first and (second is None or n > second):
            second = n
    if second is None:
        raise ValueError("No second largest (all equal)")
    return second

# Explanation: Maintain top two values in one pass (O(n), O(1) extra).
# Interview line: "I update first and second maxima in a single traversal to avoid sorting."

# -------------------------
# 7. Remove duplicates (preserve order)
def remove_duplicates(nums):
    seen = {}
    res = []
    for n in nums:
        if n not in seen:
            seen[n] = True
            res.append(n)
    return res

# Explanation: Use a dict as a seen-set to preserve order.
# Interview line: "I keep a seen map and append only unseen items to preserve order."

# -------------------------
# 8. Rotate list by k
def rotate_list(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    res = []
    for i in range(n - k, n):
        res.append(nums[i])
    for i in range(0, n - k):
        res.append(nums[i])
    return res

# Explanation: Build rotated array by concatenating two slices via loops.
# Interview line: "I compute k modulo length and rebuild the list from the two segments."

# -------------------------
# 9. Sum of list elements
def list_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

# Explanation: Accumulate in a loop (no built-in sum).
# Interview line: "I iterate and maintain an accumulator variable."

# -------------------------
# 10. Missing number 1..N
def missing_number(nums, n):
    expected = n * (n + 1) // 2
    actual = 0
    for x in nums:
        actual += x
    return expected - actual

# Explanation: Use arithmetic series sum minus actual sum computed manually.
# Interview line: "I use formula for 1..N sum and subtract the observed sum."

# -------------------------
# 11. Fibonacci series (iterative)
def fibonacci(n):
    if n <= 0:
        return []
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Explanation: Iteratively generate sequence with two variables.
# Interview line: "I use two variables and iterate n times to produce Fibonacci numbers."

# -------------------------
# 12. Prime check (trial division)
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Explanation: Test divisors up to sqrt(n) using trial division.
# Interview line: "I check divisibility up to square root to reduce checks."

# -------------------------
# 13. Factorial (recursion)
def factorial(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Explanation: Standard recursive factorial with base-case.
# Interview line: "I implement factorial recursively with base-case n==0."

# -------------------------
# 14. Armstrong number (manual power)
def is_armstrong(n):
    s = str(n)
    p = len(s)
    total = 0
    for ch in s:
        d = ord(ch) - ord('0')
        pow_val = 1
        for _ in range(p):
            pow_val *= d
        total += pow_val
    return total == n

# Explanation: Compute digit powers manually and compare total.
# Interview line: "I raise digits to the power of the digit-count using repeated multiplication."

# -------------------------
# 15. GCD (Euclidean)
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

# Explanation: Classic Euclidean algorithm with modulo.
# Interview line: "I use Euclid's algorithm because it's efficient and simple."

# -------------------------
# 16. Merge dictionaries (manual copy)
def merge_dicts(d1, d2):
    res = {}
    for k in d1:
        res[k] = d1[k]
    for k in d2:
        res[k] = d2[k]
    return res

# Explanation: Copy keys manually; second dict overrides if same key.
# Interview line: "I copy entries from both dicts; later entries overwrite earlier ones."

# -------------------------
# 17. Sort dict by value (selection sort on items)
def sort_dict_by_value(d):
    items = []
    for k in d:
        items.append((k, d[k]))
    n = len(items)
    for i in range(n):
        min_idx = i
        j = i + 1
        while j < n:
            if items[j][1] < items[min_idx][1]:
                min_idx = j
            j += 1
        items[i], items[min_idx] = items[min_idx], items[i]
    res = {}
    for k, v in items:
        res[k] = v
    return res

# Explanation: Turn dict into list-of-tuples, selection sort by value, rebuild dict.
# Interview line: "I implement selection sort on key-value pairs to order by value."

# -------------------------
# 18. Find key with max value (single pass)
def max_key(d):
    first = True
    max_k = None
    max_v = None
    for k in d:
        if first or d[k] > max_v:
            max_v = d[k]
            max_k = k
            first = False
    return max_k

# Explanation: Single traversal to track maximum value and its key.
# Interview line: "I traverse once and update the max key/value pair as I go."

# -------------------------
# 19. Simple class example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        return "{} earns {}".format(self.name, self.salary)

# Explanation: Basic class with constructor and instance method.
# Interview line: "I defined a simple class to encapsulate employee data and behavior."

# -------------------------
# 20. Inheritance example
class Animal:
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Bark"

# Explanation: Subclass overrides base method to provide specific behavior.
# Interview line: "I use inheritance and method overriding to specialize behavior."

# -------------------------
# Simple tests using assert
def run_tests():
    # 1
    assert reverse_string("Infosys") == "sysofni"
    # 2
    assert is_palindrome("madam") is True
    assert is_palindrome("python") is False
    # 3
    assert count_vowels("Automation") == 6
    # 4
    assert is_anagram("listen", "silent") is True
    assert is_anagram("aab", "aba") is True
    # 5
    assert char_frequency("robot") == {'r':1, 'o':2, 'b':1, 't':1}
    # 6
    assert second_largest([10, 20, 4, 45, 99, 99]) == 45
    # 7
    assert remove_duplicates([1,2,2,3,4,4,5]) == [1,2,3,4,5]
    # 8
    assert rotate_list([1,2,3,4,5], 2) == [4,5,1,2,3]
    # 9
    assert list_sum([1,2,3,4,5]) == 15
    # 10
    assert missing_number([1,2,4,5], 5) == 3
    # 11
    assert fibonacci(7) == [0,1,1,2,3,5,8]
    # 12
    assert is_prime(29) is True
    assert is_prime(1) is False
    # 13
    assert factorial(5) == 120
    # 14
    assert is_armstrong(153) is True
    # 15
    assert gcd(48, 18) == 6
    # 16
    assert merge_dicts({"a":1}, {"b":2}) == {'a':1, 'b':2}
    # 17
    assert sort_dict_by_value({"a":3,"b":1,"c":2}) == {'b':1,'c':2,'a':3}
    # 18
    assert max_key({"a":10,"b":50,"c":30}) == 'b'
    # 19
    e = Employee("Sangamesh", 75000)
    assert e.display() == "Sangamesh earns 75000"
    # 20
    d = Dog()
    assert d.speak() == "Bark"
    print("All tests passed ✅")

if __name__ == "__main__":
    run_tests()
