import random
import meteo_utils
import time
import grpc


class Server_service:

    def __init__(self):
        self.actual = 0
        
    def sendHumidity(self, humidity):
    	print(humidity)
    	
    	return 'Done'
    	
    def sendPollution(self, pollution):
    	print(pollution)
    	
    	return 'Done'




server_service = Server_service()
