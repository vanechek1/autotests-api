import grpc

import user_service_pb2
import user_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051') # создаем подключение к незащищенному каналу
stub = user_service_pb2_grpc.UserServiceStub(channel) # заглушка для выполнения запроса к gRPC-сервису

response = stub.GetUser(user_service_pb2.GetUserRequest(username='Alice'))
print(response)