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
            nodes_info = self.rabbit.get_info(endpoint, json_type=False)

        self.assertEqual(nodes_info["status"], "ok")

    def test_queues(self):
        endpoint = "queues"
        with self.rabbit:
            queues_info = self.rabbit.get_info(endpoint, json_type=False)

        queues = self.format.format_queues(queues_info)
        print(queues)

    def test_get_queue_messages(self):
        vhost = 'vhost'
        queue = 'queue'
        endpoint = self.format.join_args('queues', vhost, queue, 'get')

        data = {"count": 5, "ackmode": "ack_requeue_true", "encoding": "auto", "truncate": 50000}
        with self.rabbit:
            queue_message = self.rabbit.post_info(name=endpoint, data=data, json_type=False)

        print(queue_message)


if __name__ == "__main__":
    t = TestMetrics()
    t.setUp()
    t.test_get_queue_messages()
