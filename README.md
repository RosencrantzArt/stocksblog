# Stockblog

Stockblog is a Django-based blog project that provides a platform for users to share and discover stock market analysis, investment tips, and strategies. It allows users to create accounts, post analysis, and comment on others' posts, with the ability to edit and delete their own comments. The blog emphasizes an easy-to-use, minimalistic design to enhance the reading experience for investors and market enthusiasts.

## Features

- **User Accounts**: Users can register, log in, and manage their accounts.
- **Posts**: Users can create, update, and delete their own posts. Posts can include stock symbols and related analysis.
- **Comments**: Users can leave comments on posts, and edit or delete their own comments.
- **Admin Control**: Admins have the ability to delete comments.
  
## Technologies

- **Django 4.x** - Web framework for building the application.
- **PostgreSQL** - Database system for managing user data and blog content.
- **Bootstrap 5** - Responsive front-end framework used for the website's layout and design.
- **Whitenoise** - Static file management for production.
- **Git & GitHub** - Version control for managing and collaborating on the project.
- **Heroku** - Cloud platform for deploying the application.

## Installation

To get the project running locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/stockblog.git
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables:
    - Create a `.env` file in the project's root directory and add your environment variables:
    ```text
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@localhost:5432/dbname
    ```

5. Migrate the database:
    ```bash
    python manage.py migrate
    ```

6. Collect static files:
    ```bash
    python manage.py collectstatic
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

    Open your browser and go to `http://localhost:8000` to view the blog.

## Deployment

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/your-username/stockblog.git
    ```

2. Create a new GitHub repository to host the project and set it as the remote origin:
    ```bash
    git remote set-url origin <YOUR_GITHUB_REPO_URL>
    ```

3. Push the changes to your repository:
    ```bash
    git push
    ```

4. Sign up for [Heroku](https://signup.heroku.com/?utm_source=google&utm_medium=paid_search&utm_campaign=emea_heraw&utm_content=general-branded-search-rsa&utm_term=heroku%20deploy&utm_source_platform=GoogleAds&gad_source=1&gclid=CjwKCAjw3624BhBAEiwAkxgTOnW3NMOV1WnmmRl3waphvbeJMziUKDW38F0Dy3uLfBJLsjNUm-vZdxoCp9MQAvD_BwE) if you haven't already.
  
5. Create a new Heroku app through the Heroku dashboard.

6. Link your GitHub repository to Heroku and deploy the app.

7. Add environment variables on Heroku:
    - **SECRET_KEY**: Your secret key
    - **DATABASE_URL**: Your database URL (usually provided by Heroku PostgreSQL add-on)

8. After deployment, open the application in your browser.

## Functionality

### Homepage
The homepage displays a list of the latest stock analysis posts, including a title, excerpt, and a small image. Users can click on a post to view its full content and leave comments.

### User Accounts
Users can register, log in, and manage their accounts. They can post stock analysis and comment on posts. Users can edit and delete their own comments.

### Post Creation and Editing
Users can create new posts with detailed stock analysis, including text content and stock symbols. Posts can be updated or deleted by the user who created them.

### Commenting
Users can leave comments on posts to interact with the author and other readers. Users can edit or delete their own comments.

### Admin Control
Admins have the ability to delete comments, which helps in moderating the content and maintaining a respectful environment.

## Database Schema

The database schema for Stockblog consists of three main entities: Users, Posts, and Comments. Below is a detailed breakdown of the schema:

### Tables:

#### 1. User
| Column      | Type         | Description                |
|-------------|--------------|----------------------------|
| id          | int (PK)     | Unique ID for the user.    |
| name        | varchar      | The user's name.           |
| email       | varchar      | The user's email address.  |
| password    | varchar      | The user's password.       |

#### 2. Post
| Column      | Type         | Description                     |
|-------------|--------------|---------------------------------|
| id          | int (PK)     | Unique ID for the post.         |
| title       | varchar      | Title of the post.              |
| content     | text         | Content of the post.            |
| stock_symbols | varchar    | Stock symbols referenced in the post. |
| created_at  | datetime     | Timestamp when the post was created. |
| user_id     | int (FK)     | Foreign key linking to the user's ID. |

#### 3. Comment
| Column      | Type         | Description                     |
|-------------|--------------|---------------------------------|
| id          | int (PK)     | Unique ID for the comment.      |
| content     | text         | Content of the comment.         |
| created_at  | datetime     | Timestamp when the comment was created. |
| user_id     | int (FK)     | Foreign key linking to the user's ID. |
| post_id     | int (FK)     | Foreign key linking to the post's ID. |

### Relationships:
- **User**: A user can create many posts and comments.
- **Post**: A post belongs to one user and can have many comments.
- **Comment**: A comment belongs to one user and is linked to a specific post.

## Improvements and Future Features

- **User Portfolios**: Users will be able to create and track their stock investments within their portfolio.
- **Interactive Charts**: Implement interactive charts for displaying stock performance and analysis.
- **Market News Integration**: Integrate real-time stock news feeds to keep users up-to-date on market trends.

## Design Overview

### Colors

The color scheme of Stockblog is inspired by a professional and modern look that suits the world of stock market analysis. Below are the selected colors and their usage:

| **Color Code** | **Usage**                     | **Description**                                |
|-----------------|-------------------------------|------------------------------------------------|
| `#8D8C3E`      | Buttons, highlights           | A goldish yellow tone for buttons and key actions. |
| `#B4C3CF`      | Background, sections          | A soft blue-gray tone for backgrounds and main sections. |
| `#6C6F5C`      | Footer, accents               | A muted olive-green used for footer and other secondary accents. |
| `#FFFFFF`      | Card backgrounds, text        | Neutral white, balancing the other colors.    |

### Typography
The font used throughout the project is:

- **'Roboto', sans-serif**: A clean and modern font that enhances the readability and professional look of the blog.

### Design Rationale
The design focuses on clarity and usability, with a modern and professional layout that suits stock market discussions. The selected colors help create a calm, professional look while maintaining readability and highlighting important elements like buttons and links.

## CRUD Functionality

### 1. Create
- **Description**: Users can create new posts and comments through an intuitive interface.
- **How it works**:
  - Posts: Users can write text content and include stock symbols.
  - Comments: Users can leave comments on posts.

### 2. Read
- **Description**: Users can view posts and comments.
- **How it works**: 
  - All posts are displayed on the homepage.
  - Clicking a post shows its full content, along with comments.

### 3. Update
- **Description**: Users can edit their own posts and comments.
- **How it works**: 
  - Users can modify the content of their posts and comments.

### 4. Delete
- **Description**: Users can delete their own posts and comments.
- **How it works**:
  - Users can remove their comments and posts.
  - Admins can delete comments if necessary.

## License

MIT License

## Contact

For questions or feedback, please contact me via [your email address or GitHub profile].
