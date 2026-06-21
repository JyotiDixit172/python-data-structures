# Python Data Structures — Learning Notes

An indexed log of concepts covered in this repo, organized by category.

---

## Index

1. [Python Basics](#1-python-basics)
2. [Data Types](#2-data-types)
3. [Algorithm Complexity (Big O)](#3-algorithm-complexity-big-o)
4. [Object-Oriented Programming](#4-object-oriented-programming)
5. [Data Structures — Linked List (Skeleton)](#5-data-structures--linked-list-skeleton)
6. [Arrays](#6-arrays)
7. [Memory & References (Pointers)](#7-memory--references-pointers)
8. [Linked List (Implementation)](#8-linked-list-implementation)

---

## 1. Python Basics

**File:** [`1_intro.py`](1_intro.py) — **Done**

- Running a simple Python program
- `print()` for output
- Hello World as a starting point

---

## 2. Data Types

**File:** [`2_dataTypes.py`](2_dataTypes.py) — *Not yet started*

- *Planned*
- Python built-in data types and how they behave

---

## 3. Algorithm Complexity (Big O)

**File:** [`3_BigO.py`](3_BigO.py) — *Not yet started*

- *Planned*
- Time and space complexity notation
- How to compare algorithm efficiency

---

## 4. Object-Oriented Programming

**File:** [`4_class_cookie1.py`](4_class_cookie1.py) — **Done**

- Building data structures with **classes**
- **`__init__`** constructor and the **`self`** keyword
- **Instance attributes** (e.g. `self.color`)
- **Methods** vs standalone functions
- Creating multiple **instances** from one class (`Cookie("green")`, `Cookie("blue")`)
- **Getter** and **setter** methods (`get_color`, `set_color`)
- How changing one instance does not affect another (each instance has its own state)

---

## 5. Data Structures — Linked List (Skeleton)

**File:** [`5_classLinkedList.py`](5_classLinkedList.py) — *In progress*

- Started designing a `LinkedList` class (skeleton only)
- Planned core operations:
  - `append(value)` — add at the end
  - `pop()` — remove from the end
  - `prepend(value)` — add at the start
  - `insert(index, value)` — add at a position
  - `remove(index)` — remove at a position

---

## 6. Arrays

**File:** [`6_array.py`](6_array.py) — *Not yet started*

- *Planned*
- Array data structure and operations

---

## 7. Memory & References (Pointers)

### Part 1 — Immutable types (integers)

**File:** [`7_pointers1.py`](7_pointers1.py) — **Done**

- Variables are **references** to objects in memory
- Using **`id()`** to inspect memory addresses
- **Assignment** (`num2 = num1`) — both names point to the same object (same `id`)
- **Reassignment** (`num2 = 22`) — creates a new object; `num1` stays unchanged
- Python integers are **immutable** — updating one variable does not overwrite another's value

### Part 2 — Mutable types (dictionaries)

**File:** [`8_pointers2.py`](8_pointers2.py) — **Done**

- **Mutable** objects behave differently from immutable ones
- `dict2 = dict1` — both variables reference the **same** dictionary (same `id`)
- Modifying through one name (`dict2['value'] = 22`) **changes the object for both** names
- Key takeaway: assignment shares a reference; mutating the object affects all names pointing to it

---

## 8. Linked List (Implementation)

**File:** [`9_LinkedList1.py`](9_LinkedList1.py) — *Not yet started*

- *Planned*
- Full linked list implementation

---

## File Map

| # | File | Topic | Status |
|---|------|--------|--------|
| 1 | `1_intro.py` | Python basics | Done |
| 2 | `2_dataTypes.py` | Data types | Not started |
| 3 | `3_BigO.py` | Big O notation | Not started |
| 4 | `4_class_cookie1.py` | Classes & OOP | Done |
| 5 | `5_classLinkedList.py` | Linked list (skeleton) | In progress |
| 6 | `6_array.py` | Arrays | Not started |
| 7 | `7_pointers1.py` | Memory & references (immutable) | Done |
| 8 | `8_pointers2.py` | Memory & references (mutable) | Done |
| 9 | `9_LinkedList1.py` | Linked list (implementation) | Not started |