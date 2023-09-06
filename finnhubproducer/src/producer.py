from kafka3 import KafkaProducer
import websocket
import json
import time

producer = KafkaProducer(
    bootstrap_servers='kafka:29092',
    api_version=(2,6,0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')

)


data = []
counter = 0
api_key = 'cj8quspr01qjjsj7i4a0cj8quspr01qjjsj7i4ag'
def on_message(ws, message):
    global counter

    
    json_data = json.loads(message)
    data = json_data['data']
    type = json_data['type']
    for d in data:
        
        producer.send('stocks',key=b'Bitcoin Update',value=d)


    producer.flush()
    

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):

    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=cj8quspr01qjjsj7i4a0cj8quspr01qjjsj7i4ag",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
