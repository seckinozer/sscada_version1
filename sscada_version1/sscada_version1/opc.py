from opcua import Client

# OPC UA sunucusunun adresi ve bağlantı noktası
opc_server_url = "opc.tcp://192.168.1.114:4840"

def get_plc_data():
    # Bağlantıyı kur
    client = Client(opc_server_url)
    client.connect()

    # Okumak istediğiniz node'ların adreslerini belirtin
    node_addresses = [
        'ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestBool_1' # Örnek bir node
        'ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestBool_2'
        'ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestReal'
        'ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestString'
        # Daha fazla node adresi ekleyebilirsiniz
    ]

    plc_data = {}

    # Belirtilen node'ları oku ve değerlerini bir sözlüğe kaydet
    for node_address in node_addresses:
        node = client.get_node(node_address)
        value = node.get_value()
        plc_data[node_address] = value

    # Bağlantıyı kapat
    client.disconnect()

    return plc_data