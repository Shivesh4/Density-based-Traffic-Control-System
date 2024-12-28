# import boto3
# import matplotlib.pyplot as plt
# from datetime import datetime

# # Define the AWS credentials and region
# aws_access_key_id = "ASIAZS7UMHQP2SKUNMYX"
# aws_secret_access_key = "7uRAUsZCwAz7pdRY4sNQtjUwvR+KcCFIcwvb6AzG"
# aws_region = "us-east-1"
# aws_session_token = "FwoGZXIvYXdzEJ///////////wEaDHjH/YdAWUT4OTt12SK6AaPrxI/9gu7BX2ItG4PAjF/CC47Miq0EcY3NjsUu+s72m0wzSKGiPzJts5IIcLc8f3w/8kUoJwd0Z95Fe1LMKava1/IRq4bciLeZTYmXoPGrv+3RD6bMyE8KasICtiuD5l71qyPwt/4XgX3vkVGfILMTHloTPABSf8lRXXCi9UUzDaAvLTZHTdHM1dl1WwTyE3FXJjOF50kycNJXh/DBjFQHaruYDKiTtEhIgGRu15Y/InuWb3E24JQ7fSiPm+SjBjItQSs+KRuYcxDO+rA69MJ33e800tuRjdmyxZb3qWBMWx+7oTAufMXLImdrr0l+"
# # Define the DynamoDB table name
# table_name = "new_traffic_data"

# # Create a DynamoDB client
# dynamodb = boto3.client('dynamodb', region_name=aws_region, aws_access_key_id=aws_access_key_id,
#                         aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)

# # Define the desired day for which you want to retrieve and plot the data
# desired_day = "2023-05-02"

# # Define the projection expression to retrieve only the desired fields
# projection_expression = "#ts, road1, road2, road3, road4"

# # Define the filter expression to retrieve data for the desired day
# expression_attribute_names = {"#ts": "Timestamp"}

# # Scan the DynamoDB table to retrieve the data for the desired day
# response = dynamodb.scan(
#     TableName=table_name,
#     ProjectionExpression=projection_expression,
#     ExpressionAttributeNames=expression_attribute_names
# )


# # Print the response from DynamoDB
# print("DynamoDB Response:", response)

# # Extract the relevant fields from the retrieved data
# timestamps = []
# road1_values = []
# road2_values = []
# road3_values = []
# road4_values = []

# for item in response['Items']:
#     timestamp_str = item['Timestamp']['S']
#     timestamp = datetime.strptime(timestamp_str[:-1], '%Y-%m-%d %H:%M:%S')
#     timestamps.append(timestamp)
#     road1_values.append(float(item['road1']['N']))
#     road2_values.append(float(item['road2']['N']))
#     road3_values.append(float(item['road3']['N']))
#     road4_values.append(float(item['road4']['N']))

# # Print the retrieved values
# print("Timestamps:", timestamps)
# print("Road 1 Values:", road1_values)
# print("Road 2 Values:", road2_values)
# print("Road 3 Values:", road3_values)
# print("Road 4 Values:", road4_values)

import boto3
import matplotlib.pyplot as plt
from datetime import datetime

# Define the AWS credentials and region
aws_access_key_id = "ASIAZS7UMHQPWL2RITML"
aws_secret_access_key = "4LX4daWy7pitnPWHMlAAZbPRIpE/9CydDb0Pg5Lk"
aws_region = "us-east-1"
aws_session_token = "FwoGZXIvYXdzEBQaDIz2U4ggLOjAvAtczSK6Ae54BTPLBA7AXytUM9pajXqcd7x7C/YuShgUBjhtUsehHBZbi4z7lB9v09u4XPgJSwHB8r8X4Koj8zIdZ3NkzH4hGyOtU6CIzBlqlcukiuoJmubRrM3O79w79AYPJTTfbfiPXA6MKhPuI23bXh3R83QIWaP+x7OS+u1WP8lwXeUhakEr78oBeiqGsMFHmmOzQobck4srhIX58zSPhUExBhUJpiALTFW4zl2z4iMjuUjuStdxFfjCWquQOyjlgP6jBjIthaCwBuR9H+Pu+w/rQUKmax/+XMetjOzr/6oXOCenkSDE2rXeSBCbWaoDrS2K"
# Define the DynamoDB table name
table_name = "new_traffic_data"

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb', region_name=aws_region, aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)

# Define the desired day for which you want to retrieve and plot the data
desired_day = "2023-05-18"

# Define the projection expression to retrieve only the desired fields
projection_expression = "#ts, road1, road2, road3, road4"

# Define the filter expression to retrieve data for the desired day
expression_attribute_names = {"#ts": "Timestamp"}

# Scan the DynamoDB table to retrieve the data for the desired day
response = dynamodb.scan(
    TableName=table_name,
    ProjectionExpression=projection_expression,
    ExpressionAttributeNames=expression_attribute_names
)

# Extract the relevant fields from the retrieved data
timestamps = []
road1_values = []
road2_values = []
road3_values = []
road4_values = []

for item in response['Items']:
    timestamp_str = item['Timestamp']['S']
    timestamp = datetime.strptime(timestamp_str[:-1], '%Y-%m-%d %H:%M:%S')
    timestamps.append(timestamp)
    road1_values.append(float(item['road1']['N']))
    road2_values.append(float(item['road2']['N']))
    road3_values.append(float(item['road3']['N']))
    road4_values.append(float(item['road4']['N']))

data = zip(timestamps, road1_values, road2_values, road3_values, road4_values)
sorted_data = sorted(data, key=lambda x: x[0])

timestamps, road1_values, road2_values, road3_values, road4_values = zip(*sorted_data)

# Plot the values
plt.plot(timestamps, road1_values, label='Road 1')
plt.plot(timestamps, road2_values, label='Road 2')
plt.plot(timestamps, road3_values, label='Road 3')
plt.plot(timestamps, road4_values, label='Road 4')

plt.xlabel('Timestamp')
plt.ylabel('Traffic Value')
plt.title('Traffic Data for {}'.format(desired_day))
plt.xticks(rotation=45)
plt.legend()
plt.show()