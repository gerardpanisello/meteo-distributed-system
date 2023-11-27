import grpc
import meteo_utils
import datetime
import time
import lb_server_pb2
import lb_server_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50050')

# create a stub (client)
stub = lb_server_pb2_grpc.LB_serviceStub(channel)



# create a valid request message
while True:
    a=meteo_utils.MeteoDataDetector()
    air=a.analyze_air()
    t=time.time()
    temps=datetime.datetime.fromtimestamp(t)
    temperature=air["temperature"]
    humidity=air["humidity"]
    print(humidity)
    print(temps)
    Humidity=lb_server_pb2.Humidity(temperature=temperature, humidity=humidity, timestamp=t)
    stub.SendHumidity(Humidity)
    time.sleep(3)
    
