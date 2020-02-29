import redis

# redis连接
conn = redis.Redis(host='106.15.39.103', port=6379, password='')
conn.set('a1', 'hello', ex=500)
val = conn.get('a1')
print(val)

pool = redis.ConnectionPool(host='106.15.39.103', port=6379, password='', max_connections=1024)
conn = redis.Redis(connection_pool=pool)
