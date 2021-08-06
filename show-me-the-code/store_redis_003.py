# coding=utf-8

import redis


def store_redis(file_path):
    # r = redis.StrictRedis(host="localhost", port=6379, password="123456")
    r = redis.StrictRedis(host="localhost", port=6379)
    with open(file_path, 'r') as f:
        result = f.readlines()
        # print(result)
    for line in result:
        code = line.strip()
        r.lpush("cupon_code", code)


if __name__ == "__main__":
    store_redis("编程练习/python练习/show-me-the-code/coupon.txt")
