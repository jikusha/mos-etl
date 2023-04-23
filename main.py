import mysql.connector
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='call_summary'
)
my_cursor = conn.cursor()
print(my_cursor)

telephone_id= [278817, 288023, 288123, 288027, 278834, 288017, 288034, 278826, 267765, 288189]

date = datetime(2023, 4, 1)

total_time = [300, 345, 321, 890, 456, 654, 121, None, 54, 23]

talk_time = [280, 300, 321, 690, 256, 600, 120, None, 54, 20]

hold_time = [20, 45, 0, 200, 200, 54, 1, None, 54, 3]

ts = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
l=[(278817, 'H84632', ts), (288023, 'H67865', ts), (288123, 'H78654', ts),
   (288027, 'C7N876', ts), (278834, 'C76543', ts), (288017, 'H83910', ts),
   (288034, 'D76321', ts), (278826, 'H70987', ts), (267765, 'K89765', ts), (288189, 'H12345', ts)]
# for k in telephone_id:
#     for i in range(10):
#         dates = (date + timedelta(days=i)).strftime("%Y-%m-%d")
#         for j in range(10):
#             values = [k]
#             values.append(dates)
#             values.append(j+1)
#             values.append(total_time[j])
#             values.append(talk_time[j])
#             values.append(hold_time[j])
#             values.append(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
#             l.append(tuple(values))


# query = """INSERT INTO call_agent_summary_dly
#             (telephone_id, date_time, call_seq_num, total_time, talk_time, hold_time, last_timestamp)
#             values(%s, %s, %s, %s, %s, %s, %s)"""
#
# my_cursor.executemany(query, l)

# query = """
#             INSERT INTO call_agent_mapping values(%s, %s, %s)
#         """

query = "select * from call_agent_mapping"
#
# my_cursor.executemany(query, l)

my_cursor.execute(query)
result = my_cursor.fetchall()
print(result)
# conn.commit()

# print(my_cursor.rowcount, " was inserted")