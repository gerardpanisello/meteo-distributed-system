import random
import meteo_utils
import time
import grpc
import lb_server_pb2
import lb_server_pb2_grpc

stub = []
channel = grpc.insecure_channel('localhost:50051')
stub.append(lb_server_pb2_grpc.Server_serviceStub(channel))
channel = grpc.insecure_channel('localhost:50052')
stub.append(lb_server_pb2_grpc.Server_serviceStub(channel))


class LB_service:

    def __init__(self):
        self.actual = 0
        
    def sendHumidity(self, humidity):
    	print(humidity)
    	stub[self.actual].SendHumidity(humidity)
    	if self.actual <=-1:
    		self.actual = 1
    	self.actual = self.actual-1
    	return 'Done'
    	
    def sendPollution(self, pollution):
    	print(pollution)
    	stub[self.actual].SendPollution(pollution)
    	if self.actual <=-1:
    		self.actual = 1
    	self.actual = self.actual-1
    	return 'Done'



lb_service = LB_service()
