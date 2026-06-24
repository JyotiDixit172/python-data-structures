# Python Data Structures — Learning Notes

An indexed log of concepts covered in this repo, organized by category.

---

## Index

1. [Python Basics](#1-python-basics)
2. [Data Types](#2-data-types)
3. [Booleans & None](#3-booleans--none)
4. [Type Checking (`type` & `isinstance`)](#4-type-checking-type--isinstance)
5. [Type Conversion](#5-type-conversion)
6. [Algorithm Complexity (Big O)](#6-algorithm-complexity-big-o)
7. [Object-Oriented Programming](#7-object-oriented-programming)
8. [Arrays](#8-arrays)
9. [Data Structures — Linked List (Skeleton)](#9-data-structures--linked-list-skeleton)
10. [Memory & References (Pointers) — Part 1](#10-memory--references-pointers--part-1)
11. [Memory & References (Pointers) — Part 2](#11-memory--references-pointers--part-2)
12. [Linked List (Implementation)](#12-linked-list-implementation)
13. [User Input](#13-user-input)
14. [Escape Characters](#14-escape-characters)
15. [Customizing `print()`](#15-customizing-print)
16. [String Formatting (f-strings)](#16-string-formatting-f-strings)
17. [Formatting Methods (`.format()` & `%`)](#17-formatting-methods-format--)
18. [Variables](#18-variables)

---

## 1. Python Basics

**File:** [`1_intro.py`](1_intro.py) — **Done**

- Running a simple Python program
- `print()` for output
- Hello World as a starting point

---

## 2. Data Types

**File:** [`2_dataTypes.py`](2_dataTypes.py) — **Done**

- Why **types** matter — different types behave differently (e.g. name → text, age → number)
- Four basic types:
  - **`str`** (string) — text, e.g. `"alex"`
  - **`int`** (integer) — whole numbers, e.g. `25`
  - **`float`** — decimal numbers, e.g. `19.99`
  - **`None`** — represents no value (note: `"None"` in quotes is a string, not the actual `None` type)
- **`float` vs `Decimal`**:
  - `float` uses binary floating-point — fast (hardware-optimized) but imprecise for some decimals (e.g. `0.1 + 0.2` ≠ `0.3`)
  - `Decimal` stores exact base-10 values — slower (software) but precise; preferred for money and financial math
- **String quoting** — use alternate quote style when text contains quotes (e.g. `'She said "Hello" !!'`)
- **Common string methods**:
  - `.lower()`, `.upper()`, `.strip()`, `.replace(old, new)`
  - `.startswith()`, `.endswith()`
  - `in` operator to check if a substring exists (e.g. `"@" in email`)
- **Strings vs numbers** — numbers in quotes are strings (`"100"`), not integers; `"100" + "100"` concatenates, `100 + 100` adds
- **Integers** — can be positive, negative, or zero
- **Readable number literals** — underscores allowed for grouping (e.g. `7_90_000` → `790000`)
- **Float imprecision** — computers store decimals approximately (`0.1 + 0.2` prints `0.30000000000000004`)
- **Cross-type comparison** — `100 == "100"` is `False` because types differ
- **Basic type conversion** — cast with `int()`, e.g. `x == int(y)` to compare after converting a string to an integer

---

## 3. Booleans & None

**File:** [`3_Booleans_NoneValue.py`](3_Booleans_NoneValue.py) — **Done**

- **Booleans** — only two values: `True` or `False` (capitalization matters)
- Booleans are the foundation of **decision-making** in code
- **Comparison expressions** produce booleans (e.g. `age >= 18` → `True`, `age <= 18` → `True` for the same age — both can be true at boundary values)
- **`None`** — represents the **absence of value**; not zero, not empty text — just nothing
- **`None` vs `""` vs `0`**:
  - `""` is an empty string (a value of type `str`)
  - `0` is integer zero (a value of type `int`)
  - `None` means there is no value at all
- Practical example: `cart_count = 0` means the cart exists with 0 items; `cart_count = None` means the count is unknown or not applicable
- Common in frameworks like Django when a value may not exist yet

---

## 4. Type Checking (`type` & `isinstance`)

**File:** [`4_type_isinstance.py`](4_type_isinstance.py) — **Done**

- **`type()`** — inspect what type a value is (e.g. `type("hello")` → `<class 'str'>`, `type(None)` → `<class 'NoneType'>`)
- Useful for **debugging** when something isn't behaving as expected
- **`isinstance()`** — check if a value is a specific type (e.g. `isinstance(age, int)` → `True`, `isinstance(age, str)` → `False`)
- **`isinstance()` with a tuple** — check if a value is one of several types (e.g. `isinstance(age, (int, float))`)
- Helpful when you receive data and need to handle different types differently

---

## 5. Type Conversion

**File:** [`5_typeConversion.py`](5_typeConversion.py) — *Not yet started*

- *Planned*
- Converting between types (`int()`, `float()`, `str()`, etc.)
- When and why to convert types safely

---

## 6. Algorithm Complexity (Big O)

**File:** [`6_BigO.py`](6_BigO.py) — *Not yet started*

- *Planned*
- Time and space complexity notation
- How to compare algorithm efficiency

---

## 7. Object-Oriented Programming

**File:** [`7_class_cookie1.py`](7_class_cookie1.py) — **Done**

- Building data structures with **classes**
- **`__init__`** constructor and the **`self`** keyword
- **Instance attributes** (e.g. `self.color`)
- **Methods** vs standalone functions
- Creating multiple **instances** from one class (`Cookie("green")`, `Cookie("blue")`)
- **Getter** and **setter** methods (`get_color`, `set_color`)
- How changing one instance does not affect another (each instance has its own state)

---

## 8. Arrays

**File:** [`8_array.py`](8_array.py) — *Not yet started*

- *Planned*
- Array data structure and operations

---

## 9. Data Structures — Linked List (Skeleton)

**File:** [`9_classLinkedList.py`](9_classLinkedList.py) — *In progress*

- Started designing a `LinkedList` class (skeleton only)
- Planned core operations:
  - `append(value)` — add at the end
  - `pop()` — remove from the end
  - `prepend(value)` — add at the start
  - `insert(index, value)` — add at a position
  - `remove(index)` — remove at a position

---

## 10. Memory & References (Pointers) — Part 1

**File:** [`10_pointers1.py`](10_pointers1.py) — **Done**

- Variables are **references** to objects in memory
- Using **`id()`** to inspect memory addresses
- **Assignment** (`num2 = num1`) — both names point to the same object (same `id`)
- **Reassignment** (`num2 = 22`) — creates a new object; `num1` stays unchanged
- Python integers are **immutable** — updating one variable does not overwrite another's value

---

## 11. Memory & References (Pointers) — Part 2

**File:** [`11_pointers2.py`](11_pointers2.py) — **Done**

- **Mutable** objects behave differently from immutable ones
- `dict2 = dict1` — both variables reference the **same** dictionary (same `id`)
- Modifying through one name (`dict2['value'] = 22`) **changes the object for both** names
- Key takeaway: assignment shares a reference; mutating the object affects all names pointing to it

---

## 12. Linked List (Implementation)

**File:** [`12_LinkedList1.py`](After%20Module%20Completion/12_LinkedList1.py) — *Not yet started*

- *Planned*
- Full linked list implementation

---

## 13. User Input

**File:** [`6_input.py`](6_input.py) — **Done**

- **`input()`** — pauses the program and waits for the user to type something
- **`input()` always returns a `str`** — even if the user types digits (e.g. `"25"`, not `25`)
- Use **`type()`** to confirm what `input()` returned
- Convert user input with **`int()`** (or other casts) when you need a number: `age = int(input("Enter your age: "))`
- **f-strings with input** — combine `input()` and f-strings for personalized output (e.g. `print(f"Hello, {name}!")`)

---

## 14. Escape Characters

**File:** [`7_EscapeCharacters.py`](7_EscapeCharacters.py) — **Done**

- **Escape sequences** — special character combos inside strings that start with `\`
- **`\n`** — newline (starts the next output on a new line)
- **`\t`** — tab (adds horizontal spacing, useful for aligned columns)
- **`\\`** — literal backslash (e.g. file paths like `C:\\Users\\Alex`)
- **`\"`** — literal double quote inside a double-quoted string (e.g. `She said \"hello\"`)

---

## 15. Customizing `print()`

**File:** [`8_customizePrint.py`](8_customizePrint.py) — **Done**

- **`sep`** — controls what goes *between* multiple arguments (default is a space; e.g. `sep="-"` → `2024-01-15`)
- **`end`** — controls what goes *after* the output (default is `\n`; e.g. `end="...."` keeps the next print on the same line)
- **`print()` returns `None`** — it is a side-effect function (output), not a value-producing function; don't use it inside comprehensions expecting a value
- **`flush=True`** — forces output immediately instead of buffering; useful in long-running loops or progress indicators so text appears right away
- **Unpacking with `*`** — `print(*[1, 2, 3], sep=",")` spreads a list into separate arguments

---

## 16. String Formatting (f-strings)

**File:** [`9_StringFormatting.py`](9_StringFormatting.py) — **Done**

- **f-strings** — prefix a string with `f` and embed expressions in `{}` (e.g. `f"Hello, {name}!"`)
- **Expressions inside `{}`** — can do math (`f"Total: ${price * quantity}"`) or call methods (`f"{name.upper()}"`)
- **Number formatting in f-strings**:
  - `{price:.2f}` — two decimal places
  - `{population:,}` — thousands separators
  - `{rate:.1%}` — percentage with one decimal place
- **Multi-line f-strings** — triple-quoted f-strings work for emails, messages, and templates
- **Older styles** (still seen in legacy code):
  - `.format()` — `"Hello, {}! Balance: ${:.2f}".format(name, balance)`
  - `%` formatting — `"Hello, %s! Balance: $%.2f" % (name, balance)`

---

## 17. Formatting Methods (`.format()` & `%`)

**File:** [`10_FormattingMethods.py`](10_FormattingMethods.py) — *Not yet started*

- *Planned*
- Deeper practice with `.format()` and `%` style formatting

---

## 18. Variables

**File:** [`11_Variables.py`](11_Variables.py) — *In progress*

- A **variable** is a name that points to a value — created with `=` (no special keywords, no type declarations)
- **`=` means assignment** — "store the value on the right under the name on the left" (not mathematical equality)
- **Reassignment with math** — `x = x + 1` takes the current value, computes, and stores back (same for `count = count + 5`, etc.)
- **Basic examples** — `username = "alex"`, `age = 25`, `price = 19.99`, `is_active = True`
- **Naming rules** (started):
  1. Must start with a letter or `_` (underscore)
  2. Only letters, numbers, and underscores after the first character

---

## File Map

| # | File | Topic | Status |
|---|------|--------|--------|
| 1 | `1_intro.py` | Python basics | Done |
| 2 | `2_dataTypes.py` | Data types | Done |
| 3 | `3_Booleans_NoneValue.py` | Booleans & None | Done |
| 4 | `4_type_isinstance.py` | Type checking (`type` & `isinstance`) | Done |
| 5 | `5_typeConversion.py` | Type conversion | Not started |
| 6 | `6_BigO.py` | Big O notation | Not started |
| 7 | `7_class_cookie1.py` | Classes & OOP | Done |
| 8 | `8_array.py` | Arrays | Not started |
| 9 | `9_classLinkedList.py` | Linked list (skeleton) | In progress |
| 10 | `10_pointers1.py` | Memory & references (immutable) | Done |
| 11 | `11_pointers2.py` | Memory & references (mutable) | Done |
| 12 | `12_LinkedList1.py` | Linked list (implementation) | Not started |
| 13 | `6_input.py` | User input | Done |
| 14 | `7_EscapeCharacters.py` | Escape characters | Done |
| 15 | `8_customizePrint.py` | Customizing `print()` | Done |
| 16 | `9_StringFormatting.py` | String formatting (f-strings) | Done |
| 17 | `10_FormattingMethods.py` | Formatting methods (`.format()` & `%`) | Not started |
| 18 | `11_Variables.py` | Variables | In progress |
