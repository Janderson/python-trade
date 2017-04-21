""" A Simple Order Routing Mechanism """
from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import Connection
import ib.ext.EWrapper as wrapper



def error_handler(msg):
	print("Server Error:", msg)




def server_handler(msg):
	print("Server Msg:", msg.typeName, "-", msg)




def create_contract(symbol, sec_type, exch, prim_exch, curr):
	contract = Contract()
	contract.m_symbol = symbol
	contract.m_secType = sec_type
	contract.m_exchange = exch
	contract.m_primaryExch = prim_exch
	contract.m_currency = curr
	return contract




def create_order(order_type, quantity, action):
	order = Order()
	order.m_orderType = order_type
	order.m_totalQuantity = quantity
	order.m_action = action
	return order


contract = Contract()
contract.symbol = "FISV"
contract.secType = "OPT"
contract.exchange = "SMART"
contract.currency = "USD"


class TestWrapper(wrapper.EWrapper):
	def historicalData(self, reqId: TickerId, date: str, open: float, high: float, low: float, close: float, volume: int, barCount: int, WAP: float, hasGaps: int):
		super().historicalData(reqId, date, open, high, low, close, volume, barCount, WAP, hasGaps)
		print("HistoricalData. ", reqId, " Date:", date, "Open:", open,"High:", high, "Low:", low, "Close:", close, "Volume:", volume, barCount, "WAP:", WAP, "HasGaps:", hasGaps)

	def historicalDataEnd(self, reqId: int, start: str, end: str):
		super().historicalDataEnd(reqId, start, end)
		print("HistoricalDataEnd ", reqId, "from", start, "to", end)

if __name__ == "__main__":
	client_id = 1001
	order_id = 1
	port = 7496
	tws_conn = None
	try:
		# Establish connection to TWS.
		tws_conn = Connection.create(port=port,clientId=client_id)
		tws_conn.connect()
		tws_conn.register(error_handler, 'Error')
		tws_conn.registerAll(server_handler)
		aapl_contract = create_contract('EUR.USD','STK','SMART','SMART','USD')
		aapl_order = create_order('MKT', 12000, 'BUY')
		tws_conn.placeOrder(order_id, aapl_contract, aapl_order)
	finally:
		if tws_conn is not None:
			tws_conn.disconnect()
