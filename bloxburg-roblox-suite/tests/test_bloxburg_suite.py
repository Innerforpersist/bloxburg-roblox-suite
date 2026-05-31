import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bloxburg_automation import BloxburgBot
from src.job_manager import JobManager

class TestBloxburgBot(unittest.TestCase):

    def setUp(self):
        self.bot = BloxburgBot(username="TestPlayer")

    def test_start_stop(self):
        self.bot.start()
        self.assertTrue(self.bot.running)
        self.bot.stop()
        self.assertFalse(self.bot.running)

    def test_perform_task_when_not_running(self):
        self.bot.perform_task("Build Wall")  # should not crash

    def test_set_job(self):
        self.bot.set_job("Pizza Delivery")
        self.assertEqual(self.bot._current_job, "Pizza Delivery")

    def test_get_status(self):
        status = self.bot.get_status()
        self.assertIn("username", status)
        self.assertIn("running", status)

class TestJobManager(unittest.TestCase):

    def setUp(self):
        self.jm = JobManager()

    def test_list_jobs(self):
        jobs = self.jm.list_jobs()
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0)

    def test_add_and_remove_job(self):
        test_job = "Test Job"
        self.jm.add_job(test_job)
        self.assertIn(test_job, self.jm.list_jobs())
        self.jm.remove_job(test_job)
        self.assertNotIn(test_job, self.jm.list_jobs())

    def test_get_job_valid(self):
        job = self.jm.get_job(0)
        self.assertIsNotNone(job)

    def test_get_job_invalid(self):
        job = self.jm.get_job(999)
        self.assertIsNone(job)

if __name__ == "__main__":
    unittest.main()