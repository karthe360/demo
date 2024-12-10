from fastapi import FastAPI
from pydantic import BaseModel
from producer import produce_message

app = FastAPI()

# Define the data model for the message
class Message(BaseModel):
    key: str
    value: str

@app.post("/send_message/")
async def send_message(message: Message):
    # Send the message to Kafka
    topic = 'my_topic'
    produce_message(topic, message.dict())
    return {"message": "Message sent to Kafka", "data": message}



# pip install fastapi uvicorn confluent-kafka
