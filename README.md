# Fuzzy String Matching Functions

## Overview
This Python module provides two functions, `fuzzy` and `fuzzypm`, for fuzzy string matching using the `thefuzz` library. These functions are designed to facilitate string comparison within a pandas DataFrame, making them particularly useful in data cleaning, text analysis, or any scenario where string matching is needed.

## Features
- **`fuzzy` Function**: Utilizes the simple ratio algorithm for string matching, ideal for comparing single strings.
- **`fuzzypm` Function**: Employs the partial ratio algorithm for matching multiple substrings, making it suitable for more complex string comparison tasks.

## Installation
To use these functions, ensure you have the `thefuzz` library installed. If not, you can install it via pip:

``` 
pip install thefuzz
```