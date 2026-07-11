from client import CartMarginROISimulatorClient
client = CartMarginROISimulatorClient()
print(client.simulate_margins([{"price": 10}], 5.0))