# SENTINEL: Moving Assertions Earlier for Enhanced Python Program Safety

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dhruvtpatel/2540_finalproj)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)

## Overview

SENTINEL is a novel approach for automatically transforming Python programs to detect violations earlier in program execution while preserving the exact logical guarantees of original assertions. This project combines Large Language Models (LLMs) for assertion generation with a multi-stage verification pipeline that guarantees logical equivalence between early and final checks.

Our key concept is to transform assertions that typically appear at the end of computations to equivalent assertions placed earlier in execution. This enables proactive error detection before unnecessary computation occurs or side effects happen.

## Project Structure

```
├── code_files/                    # Python code files directory
│   ├── a_original_programs/       # Original input programs
│   ├── b_llm_assertion_programs/  # Programs with LLM-generated early assertions
│   └── c_transformed_programs/    # Programs transformed for verification
├── verification/                  # Verification pipeline components
│   ├── fuzz/                      # Property-based fuzzing tests
│   ├── crosshair/                 # Symbolic execution tests
│   ├── nagini/                    # Static verification tests
│   └── failure_explanation_quality/ # FEQ evaluation
├── difficulty/                    # Program difficulty analysis
├── writeups/                      # Project documentation and paper
│   └── final_writeup.tex          # Final project report
├── wikis/                         # Reference materials for LLM context
├── with_graphs_analysis/          # Analysis of results with graphs
│   └── bytecode/                  # Scripts and graphs for bytecode analysis
│   └── program_complexity/        # Scripts and graphs for program complexity relationships
│   └── code_exec_stats/           # Scripts and graphs for code execution stats
└── requirements.txt               # Project dependencies
```

## Key Features

1. **Early Assertion Generation**: Uses LLMs to generate candidate early assertions based on program context and existing final assertions.

2. **Program Transformation**: Creates transformed programs that encode logical equivalence between early and final assertions for verification.

3. **Multi-layered Verification**:
   - **Symbolic Execution**: Uses CrossHair to search for counterexamples.
   - **Fuzz Testing**: Employs Hypothesis to generate boundary-case inputs.
   - **Static Verification**: Applies Nagini for formal proof of assertion equivalence.

4. **Failure Explanation**: Provides high-quality diagnostic feedback for failed verification cases.

## Workflow

```
    Original Program         LLM Assertion         Transformed Program         Verification
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐     ┌─────────────────┐
│                  │    │                  │    │                  │     │  1. Hypothesis  │
│  def foo():      │    │  def foo():      │    │  def foo():      │     │     Fuzzing     │
│    # code        │ => │    assert early  │ => │    b_early = ... │ ==> │                 │
│    # more code   │    │    # code        │    │    # code        │     │  2. CrossHair   │
│    assert final  │    │    # more code   │    │    b_final = ... │     │     Symbolic    │
│                  │    │    assert final  │    │    assert b_early│     │                 │
│                  │    │                  │    │      == b_final  │     │  3. Nagini      │
└──────────────────┘    └──────────────────┘    └──────────────────┘     │     Static      │
                                                                          └─────────────────┘
                                                                                   │
                                                                                   ▼
                                                                          ┌─────────────────┐
                                                                          │  Classification  │
                                                                          │                  │
                                                                          │  ✓ VERIFIED      │
                                                                          │  ⚠ VALIDATED     │
                                                                          │  ✗ REJECTED      │
                                                                          └─────────────────┘
```

## Installation

```bash
# Clone the repository
git clone https://github.com/dhruvtpatel/2540_finalproj.git
cd 2540_finalproj

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Verification Pipeline

```bash
# Run the full verification pipeline
python verification/all_results.py

# View results
python verification/all_results.py --view-results
```

### Difficulty Analysis

```bash
# Generate difficulty scores for programs
python difficulty/classify_difficulty.py
```

## Example

Here's how SENTINEL transforms a simple Python function with a late assertion into one with an early, equivalent assertion:

### Original Program
```python
def process_data(x: int):
    # No early assertion here
    y = x * 2
    if y > 0:
        z = y
    else:
        z = -y
    assert z == 100  # Final assertion
```

### LLM-Generated Early Assertion
```python
def process_data(x: int):
    assert x == 50  # Early assertion added by LLM
    y = x * 2
    if y > 0:
        z = y
    else:
        z = -y
    assert z == 100  # Original final assertion
```

### Transformed Program for Verification
```python
def process_data_transformed(x: int):
    b_early = (x == 50)  # Capture early assertion as boolean
    y = x * 2
    if y > 0:
        z = y
    else:
        z = -y
    b_final = (z == 100)  # Capture final assertion as boolean
    
    # Assert that early & final assertions are equivalent
    assert b_early == b_final
```

The verification pipeline then checks that for all inputs, the early assertion (`x == 50`) is logically equivalent to the final assertion (`z == 100`).

## Paper

For a comprehensive understanding of our methodology, results, and implications, refer to our paper in `writeups/final_writeup.tex`. The paper includes:

- Formal definition of assertion equivalence
- Details on our multi-stage verification pipeline
- Analysis of program complexity vs. verification success
- Evaluation of failure explanation quality

## Authors

Dinesh Vasireddy, Soham Gupta, Dhruv Patel, Lavik Jain


## NOTE 

This is an AI-generated README.md file. Please refer to the `writeups/final_writeup.tex` for the actual paper.