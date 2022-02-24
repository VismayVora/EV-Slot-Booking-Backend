from django.shortcuts import render
from.models import Order,Payment
from .serializers import OrderDetailsSerializer,PaymentDetailsSerializer
import razorpay, environ
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

env = environ.Env()
environ.Env.read_env()

# Create your views here.
class RazorPayOrder(GenericAPIView):

    serializer_class = OrderDetailsSerializer
    
    def post(self,request,*args,**kwargs):
        client = razorpay.Client(auth=(env("RAZOR_KEY_ID"), env("RAZOR_KEY_SECRET")))
        client.set_app_details({"title" : "FindMyPlug", "version" : "1.0.0"})
        amount = request.data['amount']
        id = request.data['id']
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_"+str(id) }
        payment = client.order.create(data=data)
        serializer = self.serializer_class(data=payment)
        serializer.is_valid(raise_exception = True)
        order = serializer.save()
        return Response(payment)

class PaymentDetailsView(GenericAPIView):

    serializer_class = PaymentDetailsSerializer

    def post(self,request,*args,**kwargs):
        razorpay_payment_id = request.data['razorpay_payment_id']
        razorpay_order_id = request.data['razorpay_order_id']
        razorpay_signature = request.data['razorpay_signature']
        client = razorpay.Client(auth = ('[key_id]', '[key_secret]'))
        trusted_order = Order.objects.filter(id=razorpay_order_id)
        if trusted_order:
            params_dict={
                'razorpay_order_id': razorpay_payment_id,
                'razorpay_payment_id': razorpay_order_id,
                'razorpay_signature': razorpay_signature
                }
            verification = client.utility.verify_payment_signature(params_dict)
            print(type(verification))
            print(verification)
        else:
            verification = False
        return Response(verification)
