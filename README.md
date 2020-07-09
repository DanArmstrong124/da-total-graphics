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
- As an employee, I want to be able to access a dashboard through the navbar so that I can create or add new products.

I created a mobile design mockup and a desktop design mockup ofthe websites which can be found inside of the [WIREFRAMES]() folder.

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
- WIREFRAMES
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

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

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


In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

1. Previews
2. Running Locally
3. Setting Variables to Heroku
4. Setting up automatic deployments with GitHub
4. Hosting on Heroku with automatic repository pulls through github

## Credits

### Content
- Any content from other sites?
- Font Awesome

### Media
- PHOTOS created by myself

### Acknowledgements

- INSPO from codeinstitute