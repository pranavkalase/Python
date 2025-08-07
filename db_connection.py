import psycopg2

conn = psycopg2.connect(database='Batch22',
                        user='postgres',
                        password='Admin@123',
                        host='localhost',
                        port='5432')
print('Database connected successfully')