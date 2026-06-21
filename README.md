# Python Data Structures — Learning Notes

An indexed log of concepts covered in this repo, organized by category.

---

## Index

1. [Python Basics](#1-python-basics)
2. [Algorithm Complexity (Big O)](#2-algorithm-complexity-big-o)
3. [Object-Oriented Programming](#3-object-oriented-programming)
4. [Data Structures — Linked List](#4-data-structures--linked-list)
5. [Memory & References (Pointers)](#5-memory--references-pointers)

---

## 1. Python Basics

**File:** [`1_intro.py`](1_intro.py)

- Running a simple Python program
- `print()` for output
- Hello World as a starting point

---

## 2. Algorithm Complexity (Big O)

**File:** [`2_BigO.py`](2_BigO.py)

- *Planned / not yet started*
- Time and space complexity notation
- How to compare algorithm efficiency

---

## 3. Object-Oriented Programming

**File:** [`3_class_cookie1.py`](3_class_cookie1.py)

- Building data structures with **classes**
- **`__init__`** constructor and the **`self`** keyword
- **Instance attributes** (e.g. `self.color`)
- **Methods** vs standalone functions
- Creating multiple **instances** from one class (`Cookie("green")`, `Cookie("blue")`)
- **Getter** and **setter** methods (`get_color`, `set_color`)
- How changing one instance does not affect another

---

## 4. Data Structures — Linked List

**File:** [`4_classLinkedList.py`](4_classLinkedList.py)

- Designing a `LinkedList` class
- Core operations (skeleton / in progress):
  - `append(value)` — add at the end
  - `pop()` — remove from the end
  - `prepend(value)` — add at the start
  - `insert(index, value)` — add at a position
  - `remove(index)` — remove at a position

---

## 5. Memory & References (Pointers)

**File:** [`5_pointers.py`](5_pointers.py)

- Variables as **references** to objects in memory
- Using **`id()`** to inspect memory addresses
- **Assignment** (`num2 = num1`) — both names point to the same object
- **Reassignment** (`num2 = 22`) — creates a new object; `num1` is unchanged
- Python integers are **immutable** — updating one variable does not overwrite another’s value

---

## File Map

| # | File | Topic |
|---|------|--------|
| 1 | `1_intro.py` | Python basics |
| 2 | `2_BigO.py` | Big O notation |
| 3 | `3_class_cookie1.py` | Classes & OOP |
| 4 | `4_classLinkedList.py` | Linked list |
| 5 | `5_pointers.py` | Memory & references |