from django.shortcuts import render ,redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# this orm layer

# Create your views here.
def index(request):
    return render(request,'index.html')

#all tweet listed on page
def tweet_list(request):
    tweets =Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

#create tweets
def tweet_create(request):
    #using form two ways --empty form | submit form |just render form
    if requset.method =="POST":
        form =TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet =form.save(commit=False) #not save in db
            tweet.user =request.user # adding user in form
            tweet.save() # now it save in db
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request ,'tweet_form.html',{'form':form})

#edit tweets

def tweet_edit(request ,tweet_id):
    tweet =get_object_or_404(Tweet ,pk =tweet_id ,user =request.user)
    if request.method =='POST':
        form =TweetForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.save =request.user
            tweet.save()
            return redirect('tweet_list')
       
    else:
        form =TweetForm(instance=tweet) # form having somthing prefill
    return render(request,'tweet_form.html',{'form':form})


def tweet_delete(request,tweet_id):
    tweet =get_object_or_404(Tweet,pk=tweet_id,user =request.user)
    if request.method =='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})
    