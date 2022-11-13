from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# @login_required(login_url='signin')



from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='6ef0ac691097460daa7e4599bd75151d')

def dashboard(request): 
    top_headlines = newsapi.get_top_headlines(
                                        category= 'general', 
                                         language='en',
                                    )

    titles = [] 
    descriptions = [] 
    img_urls = [] 
    redirects = [] 

    title_arr = []
    url_arr = []
    descrip_arr = []
    redirect_arr = []

    title_arr = []
    for i in range(len(top_headlines['articles'])): 
        title_arr.append(top_headlines['articles'][i]['title'])
        url_arr.append(top_headlines['articles'][i]["urlToImage"])
        descrip_arr.append(top_headlines['articles'][i]["description"])
        redirect_arr.append(top_headlines['articles'][i]["url"])

 
    context = {
        "titles" : title_arr, 
        "img_urls" : url_arr, 
        "descriptions" : descrip_arr, 
        "redirects" : redirect_arr, 
    }
    return render(request, 'new/general.html', context)

@login_required(login_url='signin')
def business(request): 
    top_headlines = newsapi.get_top_headlines(
                                        category= 'business', 
                                         language='en',
                                    )

    titles = [] 
    descriptions = [] 
    img_urls = [] 
    redirects = [] 

    title_arr = []
    url_arr = []
    descrip_arr = []
    redirect_arr = []

    title_arr = []
    for i in range(len(top_headlines['articles'])): 
        title_arr.append(top_headlines['articles'][i]['title'])
        url_arr.append(top_headlines['articles'][i]["urlToImage"])
        descrip_arr.append(top_headlines['articles'][i]["description"])
        redirect_arr.append(top_headlines['articles'][i]["url"])

    
    context = {
        "titles" : title_arr, 
        "img_urls" : url_arr, 
        "descriptions" : descrip_arr, 
        "redirects" : redirect_arr, 
    }
    return render(request, 'new/business.html', context)
    
@login_required(login_url='signin')
def entertainment(request): 
    top_headlines = newsapi.get_top_headlines(
                                        category= 'entertainment', 
                                         language='en',
                                    )

    titles = [] 
    descriptions = [] 
    img_urls = [] 
    redirects = [] 

    title_arr = []
    url_arr = []
    descrip_arr = []
    redirect_arr = []

    title_arr = []
    for i in range(len(top_headlines['articles'])): 
        title_arr.append(top_headlines['articles'][i]['title'])
        url_arr.append(top_headlines['articles'][i]["urlToImage"])
        descrip_arr.append(top_headlines['articles'][i]["description"])
        redirect_arr.append(top_headlines['articles'][i]["url"])

    
    context = {
        "titles" : title_arr, 
        "img_urls" : url_arr, 
        "descriptions" : descrip_arr, 
        "redirects" : redirect_arr, 
    }
    return render(request, 'new/entertainment.html', context)

@login_required(login_url='signin')
def health(request): 
    top_headlines = newsapi.get_top_headlines(
                                        category= 'health', 
                                         language='en',
                                    )

    titles = [] 
    descriptions = [] 
    img_urls = [] 
    redirects = [] 

    title_arr = []
    url_arr = []
    descrip_arr = []
    redirect_arr = []

    title_arr = []
    for i in range(len(top_headlines['articles'])): 
        title_arr.append(top_headlines['articles'][i]['title'])
        url_arr.append(top_headlines['articles'][i]["urlToImage"])
        descrip_arr.append(top_headlines['articles'][i]["description"])
        redirect_arr.append(top_headlines['articles'][i]["url"])

    context = {
        "titles" : title_arr, 
        "img_urls" : url_arr, 
        "descriptions" : descrip_arr, 
        "redirects" : redirect_arr, 
    }
    return render(request, 'new/health.html', context)
@login_required(login_url='signin')
def sports(request): 
    top_headlines = newsapi.get_top_headlines(
                                        category= 'sports', 
                                         language='en',
                                    )

    titles = [] 
    descriptions = [] 
    img_urls = [] 
    redirects = [] 

    title_arr = []
    url_arr = []
    descrip_arr = []
    redirect_arr = []

    title_arr = []
    for i in range(len(top_headlines['articles'])): 
        title_arr.append(top_headlines['articles'][i]['title'])
        url_arr.append(top_headlines['articles'][i]["urlToImage"])
        descrip_arr.append(top_headlines['articles'][i]["description"])
        redirect_arr.append(top_headlines['articles'][i]["url"])

    
    context = {
        "titles" : title_arr, 
        "img_urls" : url_arr, 
        "descriptions" : descrip_arr, 
        "redirects" : redirect_arr, 
    }
    return render(request, 'new/sports.html', context)
@login_required(login_url='signin')
def technology(request): 
    top_headlines = newsapi.get_top_headlines(
                                        category= 'technology', 
                                         language='en',
                                    )

    titles = [] 
    descriptions = [] 
    img_urls = [] 
    redirects = [] 

    title_arr = []
    url_arr = []
    descrip_arr = []
    redirect_arr = []

    title_arr = []
    for i in range(len(top_headlines['articles'])): 
        title_arr.append(top_headlines['articles'][i]['title'])
        url_arr.append(top_headlines['articles'][i]["urlToImage"])
        descrip_arr.append(top_headlines['articles'][i]["description"])
        redirect_arr.append(top_headlines['articles'][i]["url"])

    
    context = {
        "titles" : title_arr, 
        "img_urls" : url_arr, 
        "descriptions" : descrip_arr, 
        "redirects" : redirect_arr, 
    }
    return render(request, 'new/technology.html', context)
@login_required(login_url='signin')
def science(request): 
    top_headlines = newsapi.get_top_headlines(
                                        category= 'science', 
                                         language='en',
                                    )

    titles = [] 
    descriptions = [] 
    img_urls = [] 
    redirects = [] 

    title_arr = []
    url_arr = []
    descrip_arr = []
    redirect_arr = []

    title_arr = []
    for i in range(len(top_headlines['articles'])): 
        title_arr.append(top_headlines['articles'][i]['title'])
        url_arr.append(top_headlines['articles'][i]["urlToImage"])
        descrip_arr.append(top_headlines['articles'][i]["description"])
        redirect_arr.append(top_headlines['articles'][i]["url"])

    
    context = { 
        "titles" : title_arr, 
        "img_urls" : url_arr, 
        "descriptions" : descrip_arr, 
        "redirects" : redirect_arr, 
    }
    return render(request, 'new/science.html', context)

@login_required(login_url='signin')
def profile(request): 
    return render(request, 'profile.html')