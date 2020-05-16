def consume_from_queue(queue_name):
    """
    Opens a connection to the specified queue and consumes data from it
    Runs every 1 minute
    Returns a list of data, depending on the queue it consumed from
    """
    import pika
    import os
    import logging
    import time

    data = []

    params = pika.URLParameters(os.environ.get('CLOUDAMQP_URL'))
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    start_time = time.time()

    # a hacky way to force this function to exit in 55 seconds
    # it will consume all incoming messages in 55 seconds
    # use 55 seconds since this function is run in 1 minute intervals
    while time.time() - start_time < 55:
        method_frame, properties, body = channel.basic_get(queue_name)

        # check that the message from the queue is not empty
        if method_frame is not None:
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)

            # the message is a byte string which needs to be decoded
            data.append(body.decode('utf-8'))

    # Cancel the consumer and return any pending messages
    # Check how many messages were requeued
    requeued_messages = channel.cancel()
    logging.info(f'Requeued {requeued_messages} messages')

    # Close the channel and the connection
    channel.close()
    connection.close()

    return data