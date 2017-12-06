#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Post
from  .myCrawler import spider

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{'posts' : posts})

def post_shop_list(request):
    products = []
    posts = spider("게토레이")

    for key, value in posts.items():
        product = value.split(',')
        #product = [href,name,price,img_src]
        print(product)
        product_entry = {
            'key': key,
            'name': product[1],
            'href': product[0],
            'price': str(product[2]).replace(".",","),
            'img' : product[-1]
        }
        products.append(product_entry)

    return render(request, 'blog/post_list.html',{'products' : products})




