import unittest

from source.rabbit.rabbit_metrics import RabbitMetrics
from source.utils import Format


class TestMetrics(unittest.TestCase):
    def setUp(self) -> None:
        self.rabbit = RabbitMetrics()
        self.format = Format()

    def test_health(self):
        endpoint = "healthchecks/node"
        with self.rabbit:
            nodes_info = self.rabbit.get_info(endpoint, json=False)

        self.assertEqual(nodes_info["status"], "ok")

    def test_queues(self):
        endpoint = "queues"
        with self.rabbit:
            queues_info = self.rabbit.get_info(endpoint, json=False)

        queues = self.format.format_queues(queues_info)
        print(queues)


if __name__ == "__main__":
    t = TestMetrics()
    t.setUp()
    t.test_queues()
