import requests as url_requests
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book, Library


def book_list(request):
    user_library = Library.objects.filter(user=request.user)
    books_in_library = [book for book in user_library.values_list('book', flat=True)]
    search_term = request.GET.get('search', '')  # Replace this with the search term you want to use
    api_key = 'AIzaSyAzmUaULnPv1IhOorHDN36kbOR7FPU-Pmc'
    api_url = f'https://www.googleapis.com/books/v1/volumes?q={search_term}&key={api_key}'
    response = url_requests.get(api_url)
    data = response.json()

    if 'items' in data:
        books = data['items']
    else:
        books = []
    results = []
    for book in books:
        volume_info = book['volumeInfo']
        title = volume_info.get('title', [])
        authors = volume_info.get('authors', [])
        authors = ', '.join(authors)
        authors = authors.replace('[', '')
        authors = authors.replace(']', '')
        publisher = volume_info.get('publisher', '')
        published_date = volume_info.get('publishedDate', '')
        description = volume_info.get('description', '')
        num_pages = volume_info.get('pageCount', [])
        genre = volume_info.get('categories', [])
        genre = ', '.join(genre)
        genre = genre.replace('[', '')
        genre = genre.replace(']', '')
        image = volume_info.get('imageLinks', {}).get('smallThumbnail', 'media/default-book.jpg')

        if publisher == '':
            publisher = 'Unknown'
        if published_date == '':
            published_date = 'Unknown'
        if description == '':
            description = 'Unknown'
        if num_pages == '' or num_pages == '0' or num_pages == 0 or type(num_pages) == list:
            num_pages = 'Unknown'
        if genre == '':
            genre = 'Unknown'
        else:
            try:
                num_pages = int(num_pages)
            except:
                num_pages = 'Unknown'

        new_key = str(hash((title, tuple(authors), publisher, published_date)))
        all_books = list(Book.objects.all().values_list('key', flat=True))

        if new_key not in all_books:
            obj = Book(title=title,
                       author=authors,
                       publisher=publisher,
                       publication_date=published_date,
                       description=description,
                       key=new_key,
                       num_pages=num_pages,
                       genre=genre,
                       image=image, )
            obj.save()

        results.append({
            'title': title,
            'authors': authors,
            'publisher': publisher,
            'published_date': published_date,
            'description': description,
            'key': new_key,
            'image': image,
        })
    return render(request, 'feed/home.html', {'books': results, 'books_in_library': books_in_library})


# def book_detail(request, key):
#     book = Book.objects.get(key=key)
#     authorsString = "-".join(book.author)
#
#     return render(request,
#                   'feed/book_details.html',
#                   {
#                       'book': book,
#                       "authorsString": authorsString,
#                   })
#
@login_required
def add_to_library(request, book_id):
    try:
        book = get_object_or_404(Book, pk=book_id)
        print(book)
        user = request.user
        library = Library(user=user, book=book)
        library.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    except:
        return JsonResponse({'status': 'error'})
