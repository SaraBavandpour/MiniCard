from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import SaveSerializer, ReceiveSerializer, SaveSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from myapp.test import USDToIRRView

@csrf_exempt
@api_view(['POST'])
def snippet_create(request):
    if request.method == 'POST':
        serializer = SaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def receive_user_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        card_number = data.get('CardNumber') 
        amount1 = data.get('amount') 
        #print(type(card_number))
        if card_number:
            try:
                user = Users.objects.get(CardNumber=card_number)
                inventory = user.inventory  
                #print('inn',inventory)
                Fname = user.FullName
                if amount1 < inventory or amount1 == inventory:
                    inventory1 = inventory - amount1
                    #inventory.save
                    instance = Users.objects.get(CardNumber=card_number)
                    data = {'inventory': inventory1}
                    #print(data, instance)
                    
                    serializer = SaveSerializer(instance,data=data)
                    #print(serializer)
                    usd_to_irr_view = USDToIRRView()
                    rate = usd_to_irr_view.get_usd_to_irr()
                    D_R = inventory1 / rate
                    def fibonacci_recursive(n):
                        if n <= 0:
                            return 0
                        elif n == 1:
                            return 1
                        else:
                            return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

                    
                    n = D_R
                    result = fibonacci_recursive(n)
                    #print(f"فیبوناچی {n}: {result}")

                    if serializer.is_valid():
                        serializer.save()
                    
                    
                    else:
                        print(serializer.errors)
                        
                    
                    return JsonResponse({'inventory': n, 'Full name' : Fname}, status=200)
                else:
                    
                   return JsonResponse({'error': 'Insufficient inventory', 'Full name' : Fname}, status=400)

            except Users.DoesNotExist:
                return JsonResponse({'error': 'CardNumber not found'}, status=400)
        return JsonResponse({'error': 'CardNumber is required', 'Full name' : Fname}, status=400)

            
       
@api_view(['GET'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Users.objects.all()
        serializer = SaveSerializer(snippets, many=True)
        return Response(serializer.data)

