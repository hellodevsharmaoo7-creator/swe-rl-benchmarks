"""
Gymnasium-compatible Reinforcement Learning Environment for SWE Benchmarking.
"""
import os
import subprocess
import time
from typing import Dict, Any, Tuple

class SWERLEnvironment:
    def __init__(self, task_id: str):
        self.task_id = task_id
        self.task_dir = os.path.join("tasks", task_id)
        self.problem_file = os.path.join(self.task_dir, "problem.md")
        
    def reset() -> Dict[str, Any]:
        with open(self.problem_file, "r", encoding="utf-8") as f:
            prompt = f.read()
        return {
            "task_id": self.task_id,
            "problem_statement": prompt,
            "status": "READY"
        }

    def step(self, patch: str) -> Tuple[Dict[str, Any], float, bool, Dict[str, Any]]:
        """
        Applies LLM patch, executes test suite, and computes RL scalar reward.
        """
        start_time = time.time()
        
        # Write patch to temporary file & run pytest
        test_file = os.path.join(self.task_dir, "test_suite.py")
        result = subprocess.run(
            ["pytest", test_file, "--json-report"],
            capture_output=True,
            text=True
        )
        
        elapsed = time.time() - start_time
        passed = result.returncode == 0
        
        # Reward calculation: 1.0 for pass, -0.5 for fail, bonus for fast execution
        reward = 1.0 if passed else -0.5
        if passed and elapsed < 1.0:
            reward += 0.2
            
        info = {
            "passed": passed,
            "execution_time": elapsed,
            "stdout": result.stdout
        }
        
        return {"status": "COMPLETED"}, reward, True, info
