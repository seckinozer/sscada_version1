from django.shortcuts import render
from opcua import Client, ua
from django.http import JsonResponse


from django.shortcuts import render
from opcua import Client

def index(request):
    
    client = Client("opc.tcp://192.168.1.83:4840")
    try:
        client.connect()
        node = client.get_node('ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestBool_1')  # Örnek bir node
        node_1 = client.get_node('ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestBool_2')
        node_2 = client.get_node('ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestReal')
        node_3 = client.get_node('ns=4; s=|var|CODESYS Control Win V3 x64.Application.GVL.xTestString')

        variable_value = node.get_value()
        variable_value_1 = node_1.get_value()
        variable_value_2 = node_2.get_value()
        variable_value_3 = node_3.get_value()
        client.disconnect()
    except Exception as e:
        variable_value = "Hata: OPC UA sunucusuna bağlanılamadı veya değişken okunamadı."
    
    context = {
        'variable_value': variable_value,
        'variable_value_1': variable_value_1,
        'variable_value_2': variable_value_2,
        'variable_value_3': variable_value_3,
        'node' : node,
        'node_1' : node_1,
        'node_2' : node_2,
        'node_3' : node_3
    }#
    return render(request, 'index.html', context)


def update_variable(request):
    if request.method == 'POST':
        variable_value = request.POST.get('variable_value', None)
        return JsonResponse({'success': True})  # Başarılı bir yanıt döndürün

    return JsonResponse({'success': False})  # POST isteği bekleniyor