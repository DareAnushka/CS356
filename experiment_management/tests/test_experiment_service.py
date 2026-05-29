import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from storage import experiment_store


class TestExperimentStore(unittest.TestCase):

    def setUp(self):
        experiment_store.experiments.clear()
        experiment_store.experiment_id = 1

    def test_save_experiment_assigns_id(self):

        experiment = {
            "user_id": "user1",
            "name": "Test Experiment",
            "status": "new",
            "project_type_id": 1,
            "sequences": [],
        }


        saved = experiment_store.save_experiment(experiment)

        self.assertEqual(saved["id"], 1)
        self.assertIn(saved, experiment_store.experiments)
        self.assertEqual(experiment_store.experiment_id, 2)

    def test_get_all_by_user_filters_results(self):

        experiment_store.save_experiment({
            "user_id": "user1",
            "name": "Experiment A",
            "status": "new",
            "project_type_id": 1,
            "sequences": [],
        })

        experiment_store.save_experiment({
            "user_id": "user2",
            "name": "Experiment B",
            "status": "new",
            "project_type_id": 1,
            "sequences": [],
        })

        experiment_store.save_experiment({
            "user_id": "user1",
            "name": "Experiment C",
            "status": "completed",
            "project_type_id": 2,
            "sequences": [],
        })

        results = experiment_store.get_all_by_user("user1")

        self.assertEqual(len(results), 2)
        
        for experiment in results:
            self.assertEqual(experiment["user_id"], "user1")


if __name__ == "__main__":
    unittest.main()
