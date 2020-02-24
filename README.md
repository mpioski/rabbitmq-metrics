# RabbitMQ Metrics

Description
-----------
This project aims to collect metrics from RabbitMQ using your [API](https://rawcdn.githack.com/rabbitmq/rabbitmq-management/v3.8.2/priv/www/api/index.html).

Available Metrics
-----------------
* /api/healthchecks/node

    Checks that the rabbit application is running correctly.
    
* /api/queues

    A list of all queues and their details.
    
*  	/api/queues/*vhost*/*name*/get
    
    Get messages from a queue.