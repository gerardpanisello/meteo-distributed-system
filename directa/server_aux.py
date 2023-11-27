import argparse
import grpc
import redis
from concurrent import futures
import time

# importa las clases generadas
import lb_server_pb2
import lb_server_pb2_grpc

# importa el servicio del servidor
from server_service import server_service
redis_client = redis.Redis(host='localhost', port=6379, db=0)
redis_client.flushdb()

# crea una clase para definir las funciones del servidor
class Server_serviceServicer(lb_server_pb2_grpc.Server_serviceServicer):
    def SendHumidity(self, Humidity, context):
        hum = str(Humidity)
        redis_client.hmset('servidor_1', {'' :hum})
        server_service.sendHumidity(Humidity)
        response = lb_server_pb2.BooleanResponse(success=True)
        return response

    def SendPollution(self, Pollution, context):
        pol = str(Pollution)
        redis_client.hmset('servidor_2', {'' :pol})
        server_service.sendPollution(Pollution)
        response = lb_server_pb2.BooleanResponse(success=True)
        return response

def start_server(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lb_server_pb2_grpc.add_Server_serviceServicer_to_server(Server_serviceServicer(), server)
    server.add_insecure_port('0.0.0.0:' + str(port))
    server.start()
    print('Server started. Listening on port', port)
            
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=50051, help='Port number')
    args = parser.parse_args()

    port = args.port

    start_server(port)

