import logging
logger = logging.getLogger(__name__)
logger.debug("Loaded " + __name__)

import sys
import time
import json

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition


def dict_to_binary(the_dict):
	# str = json.dumps(the_dict)
	binary = ' '.join(format(ord(letter), 'b') for letter in the_dict)
	return binary

def binary_to_dict(the_binary):
	jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
	# d = json.loads(jsn)  
	return jsn

	
class KafkaConnector(object):
	Type = "KafkaConnector"
	def __init__(self, Behaviour, producer_topic=None, consumer_topic=None, consumer_topic2=None, kafka_broker="localhost:9092", sync_consumer=True):
	# def __init__(self, Behaviour):
		super(KafkaConnector, self).__init__()

		self.behavior = Behaviour
		self.producer_topic = producer_topic
		self.consumer_topic = consumer_topic
		self.consumer_topic2 = consumer_topic2
		self.sync_consumer = sync_consumer
		self.kafka_api_version = (2, 12, 2)

		if(producer_topic):
			self.producer = KafkaProducer(bootstrap_servers=kafka_broker, max_request_size=20000000)
		else:
			self.producer = None
		
		if(consumer_topic):
			self.consumer = KafkaConsumer(consumer_topic, bootstrap_servers=kafka_broker)
			self.consumer.poll()
		else:
			self.consumer = None

		if(consumer_topic2):
			self.consumer2 = KafkaConsumer(consumer_topic2, bootstrap_servers=kafka_broker)
			self.consumer2.poll()
		else:
			self.consumer2 = None


	def run(self):
		while True:
			if(self.consumer): # Check at least primary consumer is present
				logger.info("Consumed | {} | Topic : {}".format(self.behavior.__class__.__name__, self.consumer_topic))
				msg = next(self.consumer)
				msg_params = { "_offset":msg.offset, "_timestamp":msg.timestamp, "_partition": msg.partition, "_topic":msg.topic }
				msg = json.loads(binary_to_dict(msg.value))

			if(self.consumer2): #chech for two consumers		
				try:
					if(self.sync_consumer):
						msg2 = json.loads(binary_to_dict(next(self.consumer2).value))
						assert msg2["_id"] == msg["source_id"]
					else:
						msg2_raw = self.consumer2.poll(max_records=1)

						if msg2_raw:
							msg2 = json.loads(binary_to_dict(msg2_raw.values()[0][0].value))
							
						else:
							msg2 = None
				except AssertionError:

					logger.info("Syncing Partition...")

					_partition = TopicPartition(topic=msg["_CameraTopic"], partition=msg["_CameraPartition"]) 
					_offset = msg["_CameraOffset"]

					logger.debug("Partition : " + str(_partition))

					self.consumer2.seek(_partition,_offset)
					msg2 = json.loads(binary_to_dict(next(self.consumer2).value))

				output = self.behavior.run(msg, msg2, msg_params)
			elif(self.consumer): # One consumer only
				output = self.behavior.run(msg, msg_params)
			else: # Not even primary consumer present, producer only behaviour
				output = self.behavior.run()

			if(self.producer):
				logger.info("Produced | {} | Topic : {}".format(self.behavior.__class__.__name__, self.producer_topic))
				# output = self.behavior.run()
				if(output):
					self.producer.send(topic=self.producer_topic, value=dict_to_binary(json.dumps(output)))
