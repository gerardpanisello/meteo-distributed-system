import grpc
from concurrent import futures
import time

import lb_server_pb2
import lb_server_pb2_grpc

from lb_service import lb_service



class LB_serviceServicer(lb_server_pb2_grpc.LB_serviceServicer):
    def SendHumidity(self, Humidity, context):
        lb_service.sendHumidity(Humidity)
        response = lb_server_pb2.BooleanResponse(success=True)
        #response = lb_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response
        
    def SendPollution(self, Pollution, context):
        lb_service.sendPollution(Pollution)
        response = lb_server_pb2.BooleanResponse(success=True)
        #response = lb_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response
        
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
lb_server_pb2_grpc.add_LB_serviceServicer_to_server(LB_serviceServicer(), server)

print("LB executant-se")
server.add_insecure_port('0.0.0.0:50050')
server.start()

try:
  while True:
    time.sleep(86400)
except KeyboardInterrupt:
  server.stop(0)
