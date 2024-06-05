from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Ad
from .forms import ConsumerForm
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO
from .sendmail import send_email

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue())

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            consumer = form.save(commit=False)
            consumer.ad = ad  # 広告情報を保存
            consumer.save()
            send_notification_emails(form.cleaned_data, ad)  # adオブジェクトを渡す
            return redirect('thanks')  # フォーム送信後にリダイレクト
    else:
        form = ConsumerForm()
    return render(request, 'ads/ad_detail.html', {'ad': ad, 'form': form})

def user_form(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            send_notification_emails(form.cleaned_data)
            return redirect('thanks')  # フォーム送信後にリダイレクト
    else:
        form = ConsumerForm()
    return render(request, 'ads/user_form.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')

def send_notification_emails(data, ad):
    subject = 'New Form Submission'
    message = f"サービス利用者: {data['name']}\n電話番号: {data['phone_number']}\nEmail: {data['email']}"
    from_email = 'your_email@gmail.com'
    
    # 広告主と広告スペース提供者のメールアドレスを取得
    advertiser_email = ad.advertiser.email
    ad_space_provider_email = ad.ad_space_provider.email
    
    recipient_list = [
        'naokimatsubayashi@example.com',
        advertiser_email,
        ad_space_provider_email
    ]
    send_mail(subject, message, from_email, recipient_list)

def email_form(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['suzukigsxnaoki@example.com']  # 送信先のメールアドレス
        send_mail(subject, message, from_email, recipient_list)
        return redirect('email_sent')
    return render(request, 'ads/email_form.html')

def email_sent(request):
    return render(request, 'ads/email_sent.html')

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})