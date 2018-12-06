# coding:utf-8

# argparse库功能肯能类似于getopt库，可以接受解析参数？？？



import argparse



parser = argparse.ArgumentParser(description='Options in Server')
parser.add_argument('-z', '--zk_host', default='127.0.0.1:2181', help='ZooKeeper server host `ip:port`')
parser.add_argument('-g', '--grpc_host', default='127.0.0.1:10001', help='Grpc server hosts `ip:port`')
parser.add_argument('-s', '--service_name', default='MyService', help='The service name current grpc server offers')
parser.add_argument('-t', '--thread', default=1, type=int, help='Number of running multi-threads.')


def serve():
    args = parser.parse_args()
    ZKHost.connect(args.zk_host)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.thread))