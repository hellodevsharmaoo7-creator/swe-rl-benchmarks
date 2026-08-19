# SWE-RL-Benchmarks 🚀
> **Reinforcement Learning Evaluation Suites & Software Engineering Benchmarks for Code LLMs**

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Benchmark Version](https://img.shields.io/badge/SWE--Bench-Compatible-brightgreen.svg)]()

`swe-rl-benchmarks` is a production-grade framework for building, executing, and evaluating **Reinforcement Learning (RL) environments** designed to train and benchmark AI models on complex software engineering tasks.

Created to support AI training pipelines (e.g. micro1 RL environment creation), this repository provides reproducible sandboxes, automated reward calculation, bug injection harnesses, and golden reference solutions across real-world codebases.

---

## 🏛️ Architecture Overview

```
                                +---------------------------+
                                |    Code LLM / Agent       |
                                +-------------+-------------+
                                              |
                                              | 1. Generates Diff / Patch
                                              v
+------------------------+      +-------------+-------------+      +------------------------+
|  Problem Specification | ---> |    SWERLEnvironment       | ---> |    Docker Sandbox      |
|  (Bug/Feature Spec)    |      +-------------+-------------+      | (Isolated Test Runner) |
+------------------------+                    |                    +-----------+------------+
                                              | 2. Executes Tests              |
                                              | 3. Computes Reward             | 3. Test Outcome
                                              v                                v
                                +-------------+-------------+      +------------------------+
                                |    Reward Scalar Vector   | <--- | pytest / Performance   |
                                |  (Pass / Speed / Memory)  |      | Verification           |
                                +---------------------------+      +------------------------+
```

---

## 🛠️ Key Features

- **Reproducible RL Sandboxes**: Fully containerized environments using Docker to prevent environment drift during RL trajectory rollouts.
- **Reward Modeling Engine**: Computes composite scalar rewards based on:
  - **Correctness Reward ($R_{\text{pass}}$)**: Pass/Fail state of regression and unit test suites.
  - **Performance Optimization Reward ($R_{\text{perf}}$)**: Latency and memory footprint reduction.
  - **Code Quality Reward ($R_{\text{quality}}$)**: Static analysis, linting, and AST complexity diffs.
- **Golden Reference Solutions**: Human-verified reference patches (`.diff`) for ground-truth verification.
- **Multi-Task Categories**:
  - `async_deadlock`: Concurrency bugs, race conditions, and event loop blocking.
  - `memory_leak_optimization`: Profiling heap allocation and optimizing memory leaks.
  - `feature_refactor`: Modernizing legacy modules into clean architecture patterns.

---

## 📂 Repository Structure

```
swe-rl-benchmarks/
├── swe_harness/
│   ├── __init__.py
│   ├── environment.py         # Gymnasium-compatible RL environment wrapper
│   └── evaluator.py           # Automated patch evaluation engine
├── tasks/
│   └── task_01_async_deadlock/
│       ├── problem.md          # Task description & environment specifications
│       ├── buggy_code.py       # Codebase containing concurrency bug
│       ├── test_suite.py       # Test harness for defect verification
│       └── golden_patch.diff   # Verified reference patch
├── Dockerfile                  # Isolated execution environment
└── README.md
```

---

## 🚀 Quickstart

### 1. Installation
```bash
git clone https://github.com/hellodevsharmaoo7-creator/swe-rl-benchmarks.git
cd swe-rl-benchmarks
pip install -r requirements.txt
```

### 2. Running an RL Evaluation Step
```python
from swe_harness.environment import SWERLEnvironment

# Initialize environment for task 01
env = SWERLEnvironment(task_id="task_01_async_deadlock")
obs = env.reset()

# Apply LLM candidate patch
patch = '''--- a/buggy_code.py
+++ b/buggy_code.py
@@ -15,4 +15,4 @@ async def process_queue(self):
-            await self.lock.acquire()
+            async with self.lock:
'''
obs, reward, done, info = env.step(patch)
print(f"Reward: {reward} | Passed: {info['passed']}")
```

---

## 📜 License
Licensed under the [MIT License](LICENSE). Developed for AI Code Evaluation & RL Benchmark Training.
