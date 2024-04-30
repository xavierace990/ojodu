from django.shortcuts import render,HttpResponse ,redirect,get_object_or_404
from .models import FeedBack 
from .models import First
from .models import Teaching_sermon
from datetime import datetime
from django.contrib import messages
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import FileResponse
import os
import io
import zipfile
from PIL import Image,ImageDraw

from datetime import datetime, timedelta
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





# Create your views here.
def index(request):
     # Retrieve the latest blog posts
    posts = Teaching_sermon.objects.all()[:2]  # Assuming you want to display the latest 2 posts

    context = {
        'posts': posts  # Pass the posts queryset to the template
    }

    return render(request, 'index.html', context)




def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        obj = FeedBack(name=name, phone=phone, email=email, feedback=feedback)
        obj.save()
        print(f"the name is {name}, phone is {phone}, email is {email}, feedback is {feedback}")
        return redirect('success')  # Redirect to the success page upon successful submission

    return render(request, 'feedback.html')


def first(request):
    if request.method == "POST":
        namee = request.POST.get("name")
        emaill = request.POST.get("email")
        phonee = request.POST.get("phone")
        visit_datee = request.POST.get("visit_date")
        how_heardd = request.POST.get("how_heard")
        commentss = request.POST.get("comments")

        print(f"Debugging: Name - {namee}")
        print(f"Debugging: Email - {emaill}")
        print(f"Debugging: Phone - {phonee}")
        print(f"Debugging: Visit_date - {visit_datee}")
        print(f"Debugging: How_heard - {how_heardd}")
        print(f"Debugging: Comments - {commentss}")

        # Create and save the object
        obj = First(name=namee, email=emaill, phone=phonee, visit_date=visit_datee, how_heard=how_heardd, comments=commentss)
        obj.save()

        return redirect('success')  # Redirect to the success page upon successful submission

    return render(request, 'first.html')

def teaching_details(request, pk):
    post = get_object_or_404(Teaching_sermon, pk=pk)
    return render(request, 'teaching_details.html', {'post': post})
    

def bulletins(request):
   
    return render(request,'bulletins.html')



def ourministries(request):
    return render(request, 'ourministries.html')

def about(request):
    return render(request, 'about.html')

def preacher(request):
    return render(request, 'preacher.html')

def teaching(request):
    return render(request, 'teaching.html')

def success(request):
    return render(request, 'success.html')
def livestream(request):
    return render(request,'livestream.html')
'''
@login_required(login_url='user_login')
def bulletin(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Redirect authenticated users to another view or home page
        return redirect('bulletin')  # Change 'some_other_view' to the desired URL or view name

    # Redirect non-authenticated users to the login page
    return redirect('user_login')

    # Your other conditions or logic for the bulletin view
    # This code will not be reached if redirections are triggered

  

    return render(request, 'bulletin.html')
'''



def donate(request):
    return render(request, 'donate.html')

def teaching_sermon(request):
    # Retrieve all posts
    posts = Teaching_sermon.objects.order_by('-published_date')

    # Set the number of posts per page
    posts_per_page = 9

    # Paginate the posts
    paginator = Paginator(posts, posts_per_page)

    # Get the current page number from the URL parameters
    page_number = request.GET.get('page')

    try:
        # Get the posts for the requested page
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'teaching_sermon.html', {'posts': paginated_posts})

'''
def teaching_sermon(request):
    posts = Teaching_sermons.objects.all()
    return render(request, 'teaching_sermon.html', {'posts': posts})
'''



def heaven_and_hell(request):
    return render(request, 'heaven_and_hell.html')

def social_vices(request):
    return render(request, 'social_vices.html')

def joy_of_the_lord(request):
    return render(request, 'joy_of_the_lord.html')

def couples_cooperation(request):
    return render(request, 'couples_cooperation.html')

def first_timer(request):
    return render(request, 'first_timer.html')

'''
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect to a success page or wherever you want
                return redirect('bulletin')
            
            # Increase the login attempt count
            attempts = request.session.get('login_attempts', 0) + 1
            request.session['login_attempts'] = attempts

            if attempts >= 4:
                # Lock the account for 3 minutes after 4 failed attempts
                request.session['login_locked'] = datetime.now() + timedelta(minutes=3)
                del request.session['login_attempts']
                
                locked_until = request.session.get('login_locked')
                if locked_until and datetime.now() < locked_until:
                    return render(request, 'login_locked.html', {'locked_until': locked_until})
            
            else:
                # Handle invalid login credentials
                error_message = "Invalid login credentials. Please try again."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
'''






def january(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["january.png","january2.png"]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="january.zip"'

    return response

def february(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="february.zip"'

    return response


def march(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["march.png","march2.png"]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="march.zip"'

    return response


def april(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["april.png","april-1.png"]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="april.zip"'

    return response


def may(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="may.zip"'

    return response


def june(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="june.zip"'

    return response


def july(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="july.zip"'

    return response 

def august(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="august.zip"'

    return response 

def september(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="september.zip"'

    return response

def october(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="october.zip"'

    return response

def november(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="november.zip"'

    return response

def december(request):
    # List of image file paths to include in the ZIP file
    image_filenames = ["",""]

    # Create an in-memory ZIP file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for image_filename in image_filenames:
            # Construct the full path to the image file
            image_path = os.path.join(settings.STATIC_ROOT,"img",  image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Save each image to the ZIP file
                zip_file.write(image_path, os.path.basename(image_path))
            else:
                print(f"Image file not found: {image_path}")

    # Rewind the ZIP buffer
    zip_buffer.seek(0)

    # Create a response with the ZIP file
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="December.zip"'

    return response



def jan(request):
    return render(request, 'january.html')

def feb(request):
    return render(request, 'february.html')

def mar(request):
    return render(request, 'march.html')
    
def apr(request):
    return render(request, 'april.html')

def may_b(request):
    return render(request, 'may.html')

def jun(request):
    return render(request, 'june.html')

def jul(request):
    return render(request, 'july.html')

def aug(request):
    return render(request, 'august.html')

def sep(request):
    return render(request, 'september.html')

def oct(request):
    return render(request, 'october.html')

def nov(request):
    return render(request, 'november.html')

def dec(request):
    return render(request, 'december.html')

