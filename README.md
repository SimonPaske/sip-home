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
