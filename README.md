# DA TOTAL GRAPHICS

DA TOTAL GRAPHICS is an online store that sells logo graphics, a customer can search for a design using the keywords they desire, if it matches a result will be shown. The customer can create an account, fill up their basket and make a purchase.

## Travis CI Build Status:
[![Build Status](https://travis-ci.org/DanArmstrong124/da-total-graphics.svg?branch=master)](https://travis-ci.org/DanArmstrong124/da-total-graphics)
 
## UX
 
- As a customer, I want to be able to find a product on the website so that I can purchase what I need.
- As a customer, I want to be able to find my basket with ease so that I can see what I am purchasing.
- As a customer, I want to be able to purchase my items so I can fulfill my needs.
- As a customer, I want to be able to create an account so that I can complete purchases.
- As a customer, I want to be able to contact the company so that I can ask enquiries.
- As a customer, I want to be able to find out more on the company so I can see their background.
- As a customer, I want to be able to search for a product by name so that I can narrow down the product results.
- As a customer, I want to be able to access and use the site from my mobile device so that I can make purchases from remote locations.
- As an admin user, I want to be able to access a dashboard through the navbar so that I can create or add new products.

I created a mobile design mockup and a desktop design mockup ofthe websites which can be found inside of the [WIREFRAMES](wireframes) folder.

## Features
 
### Existing Features

- Accounts
- - Create account - Users can create an account
- - Sign in - Users can sign in
- - Sign out - Users can sign out
- - Reset Password - Users can reset their passwords
- - Profile page - Users can view a basic profile page
- - Email verify - Users can sign in with email
- - Purchase verify - Users cannot make a purchase without an account

- Admin Panel
- - Products - View, Add, Edit, Remove
- - Users - View, Add, Edit, Remove
- - Orders - View, Add, Edit, Remove

- Products
- - View the products
- - Add the products to a basket
- - Search Bar - Search for products via name

- Checkout
- - Products - View products in cart
- - Card info - input card information for purchase
- - Checkout form - Input all information needed for purchase

- Cart
- - View all products added to cart
- - Adjust the amount of items in the cart

- Templates
- - Contact Page
- - About Page
- - Accounts
- - Cart
- - Checkout
- - Products
- - Reset Password
- - Base - The base template that extends to all other templates.

- Home
- - Contains the contact page and about page

- Live Chat
- - Allows the user to contact the admins live or leave a message.

- Contact Form
- - Allows the user to send an email after filling in a contact form.

- Favicon
- - Shows my DanCodes logo in the tab.

- Navigation
- - Allows the user to go between pages.
- - Allows the user to see the amount of items in their cart.
- - Responsive for the user to be able to use the website on their phone.

- Footer
- - Claims copyright on the site.

### Features Left to Implement
- FIX Reset Password
- Update Tests
- CSS Customisation (ADDITIONAL)
- README

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML)
    - The project uses **HTML** for the front end development.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - The project uses **CSS** for the front end development.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Python](https://www.python.org/)
    - I use **Python** for my backend applications.

- [Django](https://www.djangoproject.com/)
    - I use **Django** to create applications and projects within my code.

- [SQLITE3](https://www.sqlite.org/index.html)
    - I use **SQLITE3** as a fall-back local database if my S3 AWS fails.

- [S3 AWS](https://aws.amazon.com/s3/)
    - I use **S3 AWS** for an online database.

- [Bootstrap](https://getbootstrap.com/)
    - I use **Bootstrap** for custom css and js modules.

- [Stripe](https://stripe.com/gb)
    - I use **Stripe** as the payment gateway for the site.

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - I use **Jinja** for my templates, extensions and inner html if and for loops.

- [Heroku](https://heroku.com/)
    - I use **Heroku** to deploy my live site to the public.

- [Balsamiq](https://balsamiq.com/?gclid=Cj0KCQjwgJv4BRCrARIsAB17JI6pxTY3CSMFjqhBK9Mc7vNZZrBpNjI2EjkcVEL7T5bndyNLgDS6r98aAo4hEALw_wcB)
    - I use **Balsamiq** to create my mobile and desktop wireframes.

- [GitHub](https://github.com/)
    - I use **GitHub** to deploy my code into a repository.

- [GitPod](https://gitpod.io/)
    - I use **GitPod** as my IDE to develop my project and show local previews of my site.

- [Formspree](https://formspree.io/)
    - I use **Formspree** for email integration.

- [LiveChatInc](https://livechatinc.com/)
    - I use **LiveChatInc** for live chat integration.

- [PyPi](https://pypi.org/)
    - I use **PyPi** to install the packages required for this project into [requirements.txt](requirements.txt)

- [Travis](https://travis-ci.org/)
    - I use **Travis** as an automated builds test to ensure that my builds pass before deployment.

## Testing


### User Tests

1. Create an account form:
    1. Go to "Register"
    2. Hit submit to see if you get a verified message.
    3. Fill in form and submit to see if you get a verified message.

Tested by friends and family - Results: All Positive

2. Sign out:
    1. Go to "Sign out"
    2. Verify that you can now see Register and Sign in.

Tested by friends and family - Results: All Positive
# FAILED
3. Reset password:
    1. Go to 'Login'
    2. Press 'Forgotten password'
    3. Enter email
# FAILED

4. Sign in:
    1. Go to "Login"
    2. Press Login with empty values, verify an error message.
    3. Fill in your details, press enter and verify you are signed in.

Tested by friends and family - Results: All Positive

5. View profile:
    1. Go to "Profile"
    2. Verify that it is your username and your last login.

Tested by friends and family - Results: All Positive

6. View products:
    1. Go to "All Products"
    2. Verify you can see the products.

Tested by friends and family - Results: All Positive

7. Search for a product:
    1. Use the search bar found in the navigation bar.
    2. Search for a keyword such as "Sport".
    3. Verify you can see the product singled out.

Tested by friends and family - Results: All Positive

8. Add to basket:
    1. Go to "All Products"
    2. Select the quantity bar of a product.
    3. Enter an amount and press add to cart.
    4. Verify in nav bar you have a badge with a number of products next to your cart.

Tested by friends and family - Results: All Positive

9. Adjust cart:
    1. Go to "Cart"
    2. Select your product quantity.
    3. Adjust the product quantity up and press button.
    4. Verify quantity has been adjusted.

Tested by friends and family - Results: All Positive

12. Checkout Form:
    1. Go to "Checkout" through "Cart"
    2. Leave forms empty and submit. Verify that you have error messages.
    3. Fill in forms with Stripe Default( 4242424242424242 & 111) choose a date for expiry number and submit.
    4. Verify the purchase message.

Tested by friends and family - Results: All Positive

13. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.
    5. Press go back to original site.

Tested by friends and family - Results: All Positive

14. Live chat:
    1. Press live chat button.
    2. Attempt to leave a message.

Tested by friends and family - Results: All Positive

15. Add Products:
    1. Sign into admin account.
    2. Go to admin dashboard in navbar.
    3. Go to products.
    4. Add a product.
    5. Fill in form.
    6. Press view site.
    7. Verify the product has been added.

16. Remove Products:
    1. Sign into admin account.
    2. Go to admin dashboard in navbar.
    3. Go to products.
    4. Select a product.
    5. Select delete.
    6. Press view site.
    7. Verify the product has been removed.

17. Edit Products:
    1. Sign into admin account.
    2. Go to admin dashboard in navbar.
    3. Go to products.
    4. Select a product.
    5. Change details in product form.
    6. Press save.
    7. Press view site.
    8. Verify the product has been adjusted.

### Automated Build Tests

I used [Travis](https://travis-ci.org/) to test my builds prior to deployments.

1. I set up Travis towards the top of the README.md to show that my builds are still passing through each git push.
2. I set up Travis in a custom .travis.yml which will install all the python requirements and will test through my applications in each git push.

All of my Travis tests are passing as seen in this README.md

### Bugs & Fixes

1. My environmental variables could not be called during live previews/deployments.
    - I started my fix of this bug by spending time looking through my code, and adjusting the variable keywords.
    - I then examined my code in settings.py, of which I could not find any import of the environmental variables.
    - I added 'import env' into the code and pushed my code to github.
    - Once it worked, I setup my S3 AWS and Heroku before collecting static via 'python3 manage.py collectstatic'.
    - After the static files were sent to S3 AWS, I commented out my 'import env' before publishing my site.

## Deployment

- I started my deployment process through gitpods previews, I would preview my code every git push to ensure that it was all running smoothly.

- I started to then run my application using 'python3 manage.py runserver $IP:$PORT' this ran my application and allowed me to view my site in a browser tab.

- I made the application public to allow my friends and family to test my website whilst I had it running.

- I set up a heroku application and set all of my environmental variables into the config variables on heroku.

- I connected my heroku application to my github repository, allowing me to enable automatic deployments through each git push.

- I started hosting my website on heroku after ensuring all my databases were setup correctly.

- Once I could view my live site on heroku, my deployment process was finished, I now force a deployment through heroku, or I push to github and wait for it to run its course.

## Credits

### Content
- My icons behind certain buttons/text can be found via [FontAwesome](https://fontawesome.com/).

### Media
- I created all of my images for the site through [Canva](https://www.canva.com/).

### Acknowledgements
- I received inspiration for this site through the Code Institute Milestone Project Examples.