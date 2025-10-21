# Sum of Decimal Numbers

A program to calculate the sum of all decimal (floating-point) numbers from a user-defined series of inputs, ignoring any whole numbers.

## 📝 Description

This program first prompts the user for a number, `n`, which specifies how many numbers will be entered subsequently. It then reads `n` numbers, which can be either integers or decimals. The program identifies only the numbers with fractional parts (decimals) and calculates their total sum.

-----

## 🎯 Problem Statement

### Input:

  * The first input is a single positive integer (`n`).
  * The next `n` inputs are the numbers to be evaluated (can be integers or floats).

### Output:

  * The total sum of all decimal numbers entered.
  * "NotProceed" if the first input `n` is not a positive integer or not an integer at all.

### Rules:

1.  The first input **n** (the count of numbers to follow) must be a **positive integer**.
2.  If `n` is zero, negative, or a non-integer, the program should output the message **"NotProceed"**.
3.  The program will then read `n` numbers.
4.  The program must determine which of these numbers are decimals. A number is considered a decimal if it is not a whole number (e.g., `5.5`, `-1.5`). Integers like `3`, `-4`, `5.0` are considered whole numbers and should be excluded.
5.  The final output should be the sum of only these decimal numbers.

-----

## 💡 Examples

### Example 1 (n = 3)

**Input:**

```
3
-1.5
2.5
1
```

**Output:**

```
1.0
```

**Explanation:** Out of the numbers `-1.5`, `2.5`, `1`, the decimals are `-1.5` and `2.5`. The sum is `(-1.5) + 2.5 = 1.0`.

### Example 2 (n = 2)

**Input:**

```
2
5.5
2
```

**Output:**

```
5.5
```

**Explanation:** The only decimal number is `5.5`. The sum is **5.5**.

### Example 3 (n = 3)

**Input:**

```
3
1
2
3
```

**Output:**

```
0
```

**Explanation:** There are no decimal numbers in the input list. The sum is **0**.

### Example 4 (n = -4)

**Input:**

```
-4
```

**Output:**

```
NotProceed
```

**Explanation:** The first input `n` is negative, which is not a valid count.

### Example 5 (n = 1.5)

**Input:**

```
1.5
```

**Output:**

```
NotProceed
```

**Explanation:** The first input `n` is not an integer.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/sum-of-decimals.git
    cd sum-of-decimals
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Enter the count `n` first, then enter `n` numbers to see the result.
