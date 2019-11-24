import json, logging
from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from play.models import Play


def hello(request):
    return HttpResponse("提交成功，敬请期待")


from django.shortcuts import render


def index(re):
    # return HttpResponse("hello word")
    if re.method == 'POST':
        u = re.POST['username']
        p = re.POST['password']
        a = re.POST['address']
        longitude, latitude = '', ''
        print(u, p)
        print(a)
        try:
            import requests
            url = "http://api.map.baidu.com/cloudgc/v1?ak=l4z5qZ9rtFSMAP9xLzo2Zw2GEAtDlNn6&address=上海市{}".format(a)
            r = requests.get(url)
            print(r.url)
            if r.status_code == 200:
                addr_info = json.loads(r.content).get("result")[0]
                longitude, latitude = addr_info['location'].get('lng'), addr_info['location'].get('lat')
        except Exception as e:
            print("error")
            logging.error(e)
            pass
        play = Play.objects.filter(name=u).first()
        if play:
            play.lan = longitude
            play.len = latitude
            play.address = a
            play.save()
        else:
            play = Play(name=u, sex=p, lan=longitude, len=latitude, address=a)
            play.save()
        logging.error(play)
        return HttpResponseRedirect("/")
    else:
        return render(re, 'index.html')


def demo(request):
    plays = Play.objects.all()
    l = list()
    for p in plays:
        l.append({"name": p.name, "lan": p.lan, "len": p.len})
    return HttpResponse(json.dumps(l))


def map(request):
    return render(request, 'map.html')
