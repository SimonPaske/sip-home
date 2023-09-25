# **Photography E-Commerce Website**

Welcome to the Photography E-Commerce Website! This platform is designed to provide users with a seamless experience for browsing, purchasing, and interacting with a collection of stunning photo prints. Whether you're a photography enthusiast or simply looking to adorn your space with beautiful visuals, this website has something for everyone.

you can find website --> [here](https://sip-home-a6dbdb394c52.herokuapp.com)

---

## The-Strategy

## Site Goals

### 1. E-commerce Platform
- **Product Listing**: Display products with details such as name, image, category, description, and price.
- **User Registration**: Allow users to register for accounts.
- **Shopping Cart**: Enable users to add and remove items from their shopping cart.
- **Checkout**: Facilitate the checkout process for users to make payments.
- **Order Management**: Manage customer orders, including order creation, tracking, and payment processing.
- **Product Reviews**: Allow users to leave reviews and ratings for products.

### 2. User Management
- **User Registration**: Allow users to create accounts.
- **User Authentication**: Authenticate users during login.
- **User Profiles**: Enable users to edit their profiles.

### 3. Content Management
- **Product Management**: Allow administrators to add and update product details.

### 4. Payment Processing
- **Secure Payments**: Support secure payment processing, including interaction with the Stripe payment gateway.

### 5. Customer Interaction
- **Contact Form**: Provide a means for customers to contact the site through a contact form.

### 6. Responsive Design
- **User-Friendly Experience**: Ensure the site is responsive and accessible on various devices to improve the user experience.

### 7. Documentation
- **Product Reviews**: Document and display product reviews and ratings.

---

### Agile Planning

This project followed an agile development approach, with work organized into three sprints spread evenly over a four-week period.

Each project task was defined as a **User Story** and categorized into priority levels:

- **Must have**
- **Should have**
- **Could have**

![issues](docs/images/agile/agile_issues.png)

These stories were then assigned to specific **Milestones** and given complexity-based **story points**. The primary focus was on completing the **Must have** stories first, followed by the **Should haves**, and, if time allowed, the **Could haves**. This sequencing ensured that essential project requirements were addressed upfront, providing a comprehensive foundation before adding desirable features.
<br>

![milestones](docs/images/agile/agile_milestones.png)

A **Kanban board** was established using **GitHub Projects**, accessible [here](link to the Kanban board), where more detailed information about project tasks can be found through project cards. Notably, all stories, except those related to docs, were accompanied by well-defined **acceptance criteria**. These criteria served as clear guidelines for determining when a story could be considered complete.


Certainly, here are the various user stories and tasks written in Markdown format:
### User Stories and Tasks

#### Managing Orders (Site Administrator)
- **Description**: As a site administrator, I can manage and process customer orders so that I can change the status of orders.
- **Objective**: Efficiently handle and update order statuses as needed.

#### Reviewing Comments (Site Administrator)
- **Description**: As a site administrator, I can review and moderate comments so that I can filter out objectionable comments.
- **Objective**: Maintain a positive and respectful community by monitoring and managing comments.

#### Managing Photo Prints (Site Administrator)
- **Description**: As a site administrator, I can manage the collection of photo prints so that they are available for sale.
- **Objective**: Ensure that the photo print collection is up-to-date and ready for purchase.

#### User Profile Management (User)
- **Description**: As a user, I can manage my profile information so that I can update my details when necessary.
- **Objective**: Provide users with the ability to maintain accurate and current profile information.

#### Placing an Order (Buyer)
- **Description**: As a buyer, I can place my order and receive a confirmation so that I know my purchase was successful.
- **Objective**: Enable a smooth and reassuring purchase process for buyers.

#### Proceeding to Checkout (Customer)
- **Description**: As a customer, I can proceed to the checkout process so that I can provide shipping and payment details.
- **Objective**: Allow customers to complete the purchase transaction securely.

#### Managing Cart (Shopper)
- **Description**: As a shopper, I can view the contents of my cart, adjust quantities, and remove items so that I can finalize my purchase.
- **Objective**: Provide shoppers with control over their shopping cart contents.

#### Review Photos (User)
- **Description**: As a user, I can leave a review on photos so that I can share my thoughts about the quality.
- **Objective**: Encourage user engagement and feedback on photo prints.

#### Adding to Cart (Shopper)
- **Description**: As a shopper, I can add selected photo prints to my cart so that I can review and purchase them later.
- **Objective**: Allow shoppers to save items for future purchase consideration.

#### Browsing Photos (User)
- **Description**: As a user, I can view a collection of photo prints so that I can choose the ones I like.
- **Objective**: Enable users to explore and select from the available photo prints.

#### User Registration (New Customer)
- **Description**: As a new customer, I can create an account on the website so that I can start shopping, liking, and commenting.
- **Objective**: Facilitate the onboarding process for new customers, enabling them to engage with the site.

These user stories and tasks outline various actions and objectives for both site administrators and users, contributing to the functionality and usability of the website.

---

# Features

# Website Features and Elements

## Navigation Bar

![navbar](docs/images/screenshots/desktop/navbar.jpg)

- **Logo**: A website logo with the text "SiP Ecom" that links to the home page.
- **Menu**: A responsive navigation menu with links to different sections of the website.
  - "Store": Takes users to the store page to browse products.
  - "Edit Profile" (for authenticated users): Allows authenticated users to edit their profiles.
  - "Contact": Provides access to the contact page.
- **User Information** (for authenticated users):
  - Displays a welcome message with the username.
  - "Logout" button to log out of the user's account.
  - "Login / Sign Up" button for non-authenticated users.
- **Shopping Cart Icon**: Displays the number of items in the user's cart and links to the cart page.



## Home Page
- Displays a carousel with product images that users can interact with.
- Provides a grid of product listings with images, names, prices, and "View Details" and "Add to Cart" buttons.
- Responsive design for various screen sizes.

## Store Page
- Lists products with images, names, prices, and "View Details" and "Add to Cart" buttons.
- Allows users to view product details by clicking on a product.
- Responsive design for product listings.

## Product Detail Page
- Displays product details including name, description, price, and an image.
- Allows users to add the product to their cart.
- Shows product reviews and ratings.
- Provides a button to leave a review (for authenticated users).

## User Profile and Edit Profile
- Allows users to view and edit their profile information (for authenticated users).
- User can edit their name and email.
- Displays success messages upon profile updates.

## Cart Page
- Shows a list of items in the user's cart with names, quantities, and total prices.
- Allows users to update item quantities or remove items.
- Provides a "Proceed to Checkout" button.

## Checkout Page
- Displays a payment form for users to enter shipping and payment information.
- Supports secure payment processing.
- Shows order summary and total.
- Confirms successful payment with an order confirmation or success page.

## Contact Page
- Provides a form for users to submit messages with fields for name, email, and message.
- Validates user input and sends messages successfully.
- Responsive design for the contact form.

## Footer
- Displays social media icons with links (Facebook, Twitter, Google, Instagram, LinkedIn, GitHub).
- Includes a copyright notice with a link to the website creator's portfolio.

## Additional Functionality
- Lightbox feature for product images.
- Star rating system for product reviews.
- Ability to leave product reviews and view existing ones.
- User registration and login functionality.
- "Forgot Password" functionality.
- Custom lightbox for enlarging images.

These features and elements create a comprehensive e-commerce website with essential user interface components and functionality for users to browse, shop, and interact with products and reviews.

---
# User Experience on Website

## Home Page
Upon landing on the website, users are greeted with an intuitive and visually appealing interface. The home page provides a seamless and responsive design, ensuring that it looks great on both desktop and mobile devices. 

The main elements on the home page include:

- **Navigation Menu:** A clear and easy-to-navigate menu at the top of the page allows users to explore different sections of the website, including the store, user profile, and more.

- **Product Listings:** Users are presented with a grid of products, each with an image, name, and price. This layout makes it convenient for users to quickly browse through available products.

- **Cart Indicator:** For logged-in users, a cart indicator displays the number of items in their cart, providing a visual reminder of their shopping status.

## Store Page
When users click on the "Store" link, they are taken to the store page where they can view a wider range of products. Here, they can:

- **View Product Details:** By clicking on a product, users can access detailed information, including product images, descriptions, and pricing.

- **Add to Cart:** Users can easily add products to their shopping cart, and the cart indicator updates automatically, giving them real-time feedback on their selections.

## User Profile and Edit Profile
The "User Profile" link allows registered users to access and update their profile information. Here, they can:

- **Edit Profile:** Users can modify their name and email address through a user-friendly form. Upon saving changes, a success message confirms the update.

## Cart Page
Users can access their shopping cart by clicking on the cart icon or selecting "Cart" from the navigation menu. In the cart, they can:

- **Review Cart Contents:** Users can see a detailed list of the items they've added, including product names, quantities, and total prices.

- **Update Cart:** Users can adjust item quantities or remove items entirely.

- **Proceed to Checkout:** When ready to complete their purchase, users can proceed to the checkout page.

## Checkout Page
The checkout page provides a smooth and secure experience for users to finalize their purchase. Here, users can:

- **Enter Shipping Information:** If applicable, users can input their shipping address.

- **Payment:** Users can securely enter their payment information. The integration with Stripe ensures a secure transaction process.

## Product Reviews
For each product, users have the option to leave reviews and ratings. This feature adds transparency and trust to the shopping experience.

## Registration and Login
For new users, the website offers a straightforward registration process. Once registered, users can log in using their credentials. The website provides informative feedback for successful login and registration.

## Contact Page
The "Contact" page offers an easy way for users to get in touch with the website administrators. Users can provide their name, email, and message, making it simple to seek assistance or provide feedback.

## Overall Experience
The website provides a seamless and enjoyable user experience, from browsing products to completing purchases. It prioritizes user convenience, clear navigation, and a responsive design. Additionally, user feedback is integrated into the shopping experience through product reviews and the contact page, enhancing user engagement and satisfaction.

---

## User Interaction

- **Reviewing Comments**: As a site administrator, you have the power to review and moderate comments to maintain a positive and engaging environment.
- **Reviewing Photos**: Express your opinions about the quality and aesthetic of the photos by leaving detailed reviews.

## Shopping Experience

- **Browsing Photos**: Discover a diverse collection of photo prints and explore a range of themes and styles.
- **Adding to Cart**: Shoppers can add their favorite photo prints to the cart, allowing them to review and purchase their chosen items at a later time.
- **Managing Cart**: View the contents of your cart, adjust quantities, and remove items as needed, ensuring a smooth checkout process.
- **Placing an Order**: Buyers can easily place orders and receive confirmations, assuring that their purchase was successful.
- **Proceeding to Checkout**: Customers can proceed to the checkout process, where they can input shipping and payment details to finalize their purchase.

## Admin Management

- **Managing Orders**: As a site administrator, you can efficiently manage and process customer orders, including changing the status of orders as necessary.
- **Reviewing and Moderating**: Admins have the ability to review and moderate reviews, ensuring that objectionable content is filtered out.
- **Managing Photo Prints**: Admins curate the collection of photo prints available for sale, ensuring a high-quality selection.

## User Accounts

- **User Profile Management**: Users can easily manage their profile information, allowing them to update details whenever required.
- **User Registration**: New customers can create accounts on the website, granting them the ability to start shopping and leave reviews.

---

## Deployment

The project was stored on GitHub and deployed on Heroku. Before deployment make sure that a requirements.txt file is created using the command `pip3 freeze > requirements.txt`.
To deploy the project, the following steps were taken:

1. Log in to [ElephantSQL.com](https://www.elephantsql.com/) to access your dashboard
![new instance](docs/images/deployment/elephantSQL.png)

1. Set up your plan and select region.
![select plan and region](docs/images/deployment/elephantSQL1.png)

1. Select a data center near you
![select region](docs/images/deployment/elephantSQL2.png)

1. Then click “Review”
![review](docs/images/deployment/elephantSQL3.png)

1. Click “Create Instance”
![create instance](docs/images/deployment/elephantSQL4.png)

1. Click on the instance you just created
![select instance](docs/images/deployment/elephantSQL5.png)

1. In the URL section, click the copy icon to copy the database URL.
![copy](docs/images/deployment/elephantSQL6.png)

1. Create a file called **env.py**.
   1. In your **env.py** file add the following line of code  **import os**
   2. First, add a blank line, then set a DATABASE_URL variable, with the value you just copied from ElephantSQL as follows and then create a SECRET_KEY variable:
![database url](docs/images/deployment/database_url.png)
![secret key](docs/images/deployment/secret_key.png)

1. Create a Procfile. In the Procfile, add the following line of code with your app name:
`web: gunicorn appname.wsgi`

1. Migrate you models to the database using the command `python3 manage.py migrate`.
2. Add, commit, and push the changes to GitHub.
3. Connect the GitHub repository to the Heroku app.
4. Create a new app on Heroku.
![new app](docs/images/deployment/heroku1.png)

1. Give your app a name and select the region closest to you. When you’re done, click “Create app” to confirm
![app name](docs/images/deployment/heroku2.png)

1. Click on Heroku dashboard open the Settings tab
    ![settings](docs/images/deployment/heroku3.png)

2. Set the following config vars in Heroku:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - DATABASE_URL
    - EMAIL_HOST_PASS
    - EMAIL_HOST_USER
    - SECRET_KEY
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - STRIPE_WH_SECRET
    - USE_AWS
    - DISABLE_COLLECTSTATIC
    ![config vars](docs/images/deployment/heroku4.png)

3. In the Heroku dashboard, click on the “Deploy” tab, then scroll down to “Deployment method” and select GitHub.
![deployment](docs/images/deployment/heroku5.png)

1. In the “Connect to GitHub” section, make sure your GitHub profile is displayed, then add your repository name and click “Search”.
![connect](docs/images/deployment/heroku6.png)

20. Once your repo is found, click “Connect” to complete the connection.
![search](docs/images/deployment/heroku7.png)

21. In the “Automatic deploys” section, click “Enable Automatic Deploys” to deploy the app to Heroku every time you push to GitHub.
![enable automatic](docs/images/deployment/heroku8.png)

22. In the “Manual deploy” section, select the master branch then click “Deploy Branch”.
![deploy](docs/images/deployment/heroku9.png)

23. Once the build is complete, click “View” to launch your new app.
![view](docs/images/deployment/heroku10.png)

---

# Manual Testing Checklist - SiP Home E-Commerce Website

## Home Page

- [ ] Verify that the home page loads correctly without errors.
- [ ] Check that the navigation menu is visible and functional.
- [ ] Ensure that the product listings are displayed correctly with images, names, and prices.
- [ ] Test the responsiveness of the home page by resizing the browser window.
- [ ] Verify that the cart indicator (if logged in) shows the correct number of items.

## Store Page

- [ ] Click on a product to view its details, and verify that the product page loads correctly.
- [ ] Check that the product images, descriptions, and prices are displayed accurately.
- [ ] Attempt to add a product to the cart and confirm that the cart updates accordingly.
- [ ] Test the "Add to Cart" button to ensure it functions as expected.

## User Profile and Edit Profile

- [ ] Access the user profile page and verify that it displays the user's information.
- [ ] Edit the user's profile by modifying the name and email address and confirm that changes are saved successfully.
- [ ] Ensure that appropriate success messages are displayed after profile edits.

## Cart Page

- [ ] Click on the cart icon or select "Cart" from the menu to access the cart page.
- [ ] Verify that the cart displays a list of items with their names, quantities, and total prices.
- [ ] Test the functionality to update item quantities and remove items from the cart.
- [ ] Confirm that the "Proceed to Checkout" button takes users to the checkout page.

## Checkout Page

- [ ] Access the checkout page and check for the presence of a secure payment form.
- [ ] Enter valid shipping information (if applicable) and verify that it is processed correctly.
- [ ] Test the payment process by entering valid payment information.
- [ ] Confirm that a successful payment results in an order confirmation or success page.
- [ ] Test the behavior when entering invalid payment information.

## Product Reviews

- [ ] Navigate to a product page and check if users can leave product reviews.
- [ ] Leave a review and rating for a product to ensure the process is straightforward.
- [ ] Confirm that submitted reviews and ratings are displayed correctly on the product page.

## Registration and Login

- [ ] Register a new user account and verify that the registration process is successful.
- [ ] Log in using the newly created account and ensure that the login process works as expected.
- [ ] Test the "Forgot Password" functionality if available.

## Contact Page

- [ ] Access the contact page and verify that it displays the required fields for name, email, and message.
- [ ] Submit a message through the contact form and confirm that it is sent successfully.
- [ ] Test the contact form with incomplete or incorrect information to check for validation.

## Overall Experience

- [ ] Perform cross-browser testing (e.g., Chrome, Firefox, Safari) to ensure compatibility.
- [ ] Test the website's responsiveness on various devices (e.g., desktop, tablet, mobile).
- [ ] Verify that error messages are displayed when necessary (e.g., login failures, invalid form submissions).
- [ ] Check for broken links or images throughout the website.
- [ ] Test the website's performance by loading pages with a reasonable amount of data.
- [ ] Confirm that the website's design is consistent and visually appealing.

This manual testing checklist can serve as a starting point for ensuring the functionality, usability, and reliability of your e-commerce website. You may customize it further to match the specific features and requirements of your website.

## Technologies

### Frameworks, Libraries, and Programs Used

- **Django**: The project uses Django as the web framework.
- **PostgreSQL**: The project uses PostgreSQL as the database.
- **Heroku**: The project is deployed on Heroku.
- **AWS S3**: The project uses AWS S3 to store static and media files.
- **Stripe**: The project uses Stripe to handle payments.
- **Bootstrap**: The project uses Bootstrap for styling.
- **jQuery**: The project uses jQuery for interactivity.
- **Font Awesome**: The project uses Font Awesome for icons.
- **Google Fonts**: The project uses Google Fonts for typography.
- **Git**: The project uses Git for version control.
- **GitHub**: The project uses GitHub for version control.
- **GitPod**: The project uses GitPod as the IDE.
- **Justinmind**: The project uses Justinmind for wireframing.
- **Gunicorn**: The project uses Gunicorn as the WSGI HTTP Server.
- **PIP**: The project uses PIP as the package manager.
- **PIPENV**: The project uses PIPENV for virtual environment.
- **Boto3**: The project uses Boto3 to connect to AWS services.
- **Django Allauth**: The project uses Django Allauth for user authentication.
- **Django Crispy Forms**: The project uses Django Crispy Forms for styling forms.
- **Django Countries**: The project uses Django Countries to provide country choices.
- **Django Storages**: The project uses Django Storages to connect to AWS S3.
- **Pillow**: The project uses Pillow to handle images.
- **Psycopg2**: The project uses Psycopg2 to connect to PostgreSQL.
- **Whitenoise**: The project uses Whitenoise to serve static files.
- **W3C Markup Validator**: The project uses W3C Markup Validator to validate HTML code.
- **W3C CSS Validator**: The project uses W3C CSS Validator to validate CSS code.
- **JSHint**: The project uses JSHint to validate JavaScript code.
- **PEP8**: The project uses PEP8 to validate Python code.
- **Chrome DevTools**: The project uses Chrome DevTools for testing and debugging.
- **VSCode**: The project uses VSCode as the code editor.
- **ElephantSQL**: The project uses ElephantSQL as the PostgreSQL database provider.
- **Cloudinary**: The project uses Cloudinary to store images.
- **Django Debug Toolbar**: The project uses Django Debug Toolbar to debug the project.
- **SQLAlchemy**: The project uses SQLAlchemy to connect to PostgreSQL.

---

### Languages Used:

- **HTML**: The project uses HTML to structure the content.
- **CSS**: The project uses CSS to style the content.
- **JavaScript**: The project uses JavaScript to add interactivity.
- **Python**: The project uses Python to handle the backend functionality.
- **Markdown**: The project uses Markdown to write the README.md file.
- **JSON**: The project uses JSON to store data.
- **SQL**: The project uses SQL to query the database.
-
