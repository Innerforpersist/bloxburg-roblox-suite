import json
import os
from typing import List, Optional

JOBS_DB = "jobs_database.json"

class JobManager:
    """Manages available jobs for Bloxburg players."""

    def __init__(self):
        self.jobs: List[str] = []
        self._load_jobs()

    def _load_jobs(self):
        """Load jobs from local JSON file."""
        if os.path.exists(JOBS_DB):
            with open(JOBS_DB, "r") as f:
                data = json.load(f)
                self.jobs = data.get("jobs", [])
        else:
            self.jobs = [
                "Pizza Delivery",
                "Cashier",
                "Mechanic",
                "Miner",
                "Lumberjack"
            ]
            self._save_jobs()

    def _save_jobs(self):
        """Save jobs to local JSON file."""
        with open(JOBS_DB, "w") as f:
            json.dump({"jobs": self.jobs}, f, indent=2)

    def list_jobs(self) -> List[str]:
        """Return all available jobs."""
        return self.jobs

    def add_job(self, job_name: str):
        """Add a new job to the list."""
        if job_name not in self.jobs:
            self.jobs.append(job_name)
            self._save_jobs()
            return True
        return False

    def remove_job(self, job_name: str) -> bool:
        """Remove a job from the list."""
        if job_name in self.jobs:
            self.jobs.remove(job_name)
            self._save_jobs()
            return True
        return False

    def get_job(self, index: int) -> Optional[str]:
        """Get job by index."""
        try:
            return self.jobs[index]
        except IndexError:
            return None