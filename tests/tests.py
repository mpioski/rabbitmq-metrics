import unittest

from source.rabbit.rabbit_metrics import RabbitMetrics
from source.utils import Format


class TestMetrics(unittest.TestCase):
    def setUp(self) -> None:
        self.rabbit = RabbitMetrics()
        self.format = Format()
        self.vhost = 'vhost_test'
        self.queue = 'queue_test'
        self.create_vhost()
        self.create_queue()

    def create_vhost(self):
        endpoint = self.format.join_args('vhosts', self.vhost)

        data = {"description": "test virtual host", "tags": "test"}
        with self.rabbit:
            self.rabbit.put_info(name=endpoint, data=data)

    def create_queue(self):
        endpoint = self.format.join_args('queues', self.vhost, self.queue)

        data = {"auto_delete": False, "durable": True}
        with self.rabbit:
            self.rabbit.put_info(name=endpoint, data=data)

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
        endpoint = self.format.join_args('queues', self.vhost, self.queue, 'get')

        data = {"count": 5, "ackmode": "ack_requeue_true", "encoding": "auto", "truncate": 50000}
        with self.rabbit:
            queue_message = self.rabbit.post_info(name=endpoint, data=data, json_type=False)

        print(queue_message)

    def test_delete_messages(self):
        endpoint = self.format.join_args('queues', self.vhost, self.queue, 'contents')

        data = {"count": 5, "ackmode": "ack_requeue_true", "encoding": "auto", "truncate": 50000}
        with self.rabbit:
            r = self.rabbit.delete_info(name=endpoint, data=data)

        print(r)

    def test_bindings(self):
        endpoint = self.format.join_args('queues', self.vhost, self.queue, 'bindings')

        with self.rabbit:
            bindings = self.rabbit.get_info(name=endpoint, json_type=True)

        print(bindings)


if __name__ == "__main__":
    t = TestMetrics()
    t.setUp()
    t.create_queue()
