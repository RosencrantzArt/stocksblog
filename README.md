# Stockblog

 ![](<staticfiles/admin/img/gis/responsive site .png>)
Stockblog is a Django-based blog project that provides a platform for users to share and discover stock market analysis, investment tips, and strategies. It allows users to create accounts, post analysis, and comment on others' posts, with the ability to edit and delete their own comments. The blog emphasizes an easy-to-use, minimalistic design to enhance the reading experience for investors and market enthusiasts. 

## Features

- **User Accounts**: Users can register, log in and logout. 
- **Comments**: Users can leave comments on posts, and edit or delete their own comments.
- **Admin Control**: Admins have the ability to delete comments.
  
## Technologies

- **Django 4.x** - Web framework for building the application.
- **PostgreSQL** - Database system for managing user data and blog content.
- **Bootstrap 5** - Responsive front-end framework used for the website's layout and design.
- **Whitenoise** - Static file management for production.
- **Git & GitHub** - Version control for managing and collaborating on the project.
- **Heroku** - Cloud platform for deploying the application.
- **ChatGPT** - Most of the text and blogpost generated by chat gpt

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
    git clone https://github.com/RosencrantzArt/stocksblog.git
    ```

2. Create a new GitHub repository to host the project and set it as the remote origin:
    ```bash
    git remote set-url origin <https://stockblog-f1303a9b9ead.herokuapp.com/>
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
The homepage displays a list of the latest stock analysis posts, including a title and expcerpt. Users can click on a post to view its full content and leave comments.

![Alt text](staticfiles/admin/img/gis/fullfirstpage.png)

### User Accounts
Users can register, log in and logout. 

![Alt text](staticfiles/admin/img/gis/registrer.png)

![Alt text](staticfiles/admin/img/gis/login.png)

![Alt text](staticfiles/admin/img/gis/logout.png)

### Post Creation and Editing
Admin can write and update posts. 
![Alt text](staticfiles/admin/img/gis/admincreatepost.png)    

### Commenting
Users can leave comments on posts to interact with the author and other readers. Users can edit or delete their own comments. 
![Alt text](staticfiles/admin/img/gis/commentEditDelete.png)   

### Admin Control
Admins have the ability to delete comments, which helps in moderating the content and maintaining a respectful environment. Admin needs to aprove new comments and comments thats been edited before it shows on the page. 
![Alt text](staticfiles/admin/img/gis/waittoapprovecomment.png)

### Confirmation 
A confirmation message shows after eftery command
![Alt text](staticfiles/admin/img/gis/comfirmcommentdelete.png)
![Alt text](staticfiles/admin/img/gis/loginconfirm.png)

### About page 
![Alt text](staticfiles/admin/img/gis/aboutpage.png)

## Database Schema

The database schema for Stockblog consists of three main entities: Users, Posts, and Comments. Below is a detailed breakdown of the schema:

### Wireframe 
![Alt text](staticfiles/admin/img/gis/wireframe.png)

### Tables:

### 1. **User**
| Column      | Type         | Description                             |
|-------------|--------------|-----------------------------------------|
| id          | int (PK)     | Unique ID for the user.                 |
| name        | varchar      | The user's name.                        |
| email       | varchar      | The user's email address.               |
| password    | varchar      | The user's password (hashed).           |

- **Relationships**:
  - A **User** can create many **Posts** and **Comments**.

---

### 2. **Post**
| Column        | Type         | Description                                      |
|---------------|--------------|--------------------------------------------------|
| id            | int (PK)     | Unique ID for the post.                          |
| title         | varchar      | Title of the post.                              |
| content       | text         | Content of the post.                            |
| stock_symbols | varchar      | Stock symbols referenced in the post (if applicable). |
| created_at    | datetime     | Timestamp when the post was created.            |
| user_id       | int (FK)     | Foreign key linking to the user's ID who created the post. |

- **Relationships**:
  - A **Post** belongs to one **User** and can have many **Comments**.

---

### 3. **Comment**
| Column      | Type         | Description                                      |
|-------------|--------------|--------------------------------------------------|
| id          | int (PK)     | Unique ID for the comment.                       |
| content     | text         | Content of the comment.                         |
| created_at  | datetime     | Timestamp when the comment was created.         |
| user_id     | int (FK)     | Foreign key linking to the user's ID who created the comment. |
| post_id     | int (FK)     | Foreign key linking to the post's ID.           |

- **Relationships**:
  - A **Comment** belongs to one **User** and is linked to a specific **Post**.
  - A **User** can edit or delete their own comments, based on matching the `user_id` in the **Comment** table with the current logged-in user.

---

### Key Points:
- **User** can create an account, comment on posts, and edit or delete their own comments.
- **Post** belongs to a **User** and can have many **Comments**.
- **Comment** belongs to a **User** and is associated with a **Post**.

### Additional Considerations:
- **Access Control**: Ensure that users can only edit or delete their own comments by comparing the logged-in user's ID with the `user_id` in the **Comment** table.
- **Indexes**: It is recommended to create indexes on `user_id` and `post_id` in the **Comment** table to optimize queries that filter by user or post.


## Improvements and Future Features

- **User Posts**: Users will be able to create their own posts, including adding content and stock symbols.
- **Comment Replies**: Users will be able to reply to comments made on posts, enabling threaded discussions.
- **Filter sections**: Users will be able to sort blog posts
- **Delete account**: Users will be able to delete own account
- **Overall Design**: Use design on all pages and make It more modern and suiteble for a site about stocks. 

## Design Overview

### Colors

The color scheme of Stockblog is inspired by a professional and modern look that suits the world of stock market analysis. Below are the selected colors and their usage:

| **Color Code** | **Usage**                     | **Description**                                |
|-----------------|-------------------------------|------------------------------------------------|
| `#8D8C3E`      | Buttons, highlights           | A goldish yellow tone for buttons and key actions. |
| `#B4C3CF`      | Background, sections          | A soft blue-gray tone for backgrounds and main sections. |
| `#6C6F5C`      | Color for frame headline      | A dark beige used for frame headline in posts. |
| `#13252F`      | Footer, accents, text         | A dark blue-green used for footer and text.  |


![Alt text](staticfiles/admin/img/gis/colorscheme.png)

### Typography
The font used throughout the project is:

- **'Roboto', sans-serif**: A clean and modern font that enhances the readability and professional look of the blog.

### Design Rationale
The design is simple and user-friendly, aiming for clarity and ease of navigation. The layout is clean and functional, with a focus on delivering stock market content effectively. The color scheme is subtle and professional, ensuring good readability while drawing attention to key elements like buttons and links.

## CRUD Functionality

### 1. Create
- **Description**: Users can create account and add comments through an intuitive interface.
- **How it works**:
  - Posts: Users can click on posts and view the whole post.
  - Comments: Users can leave comments on posts.

### 2. Read
- **Description**: Users can view posts and comments.
- **How it works**: 
  - All posts are displayed on the homepage.
  - Clicking a post shows its full content, along with comments.

### 3. Update
- **Description**: Users can edit their own comments.
- **How it works**: 
  - Users can modify the content of their comments.

### 4. Delete
- **Description**: Users can delete their own comments.
- **How it works**:
  - Users can remove their comments. 
  - Admins can delete comments if necessary.


# Testing Report for StocksBlog

## Devices Tested
- **Samsung Galaxy Z Flip 6** (Mobile)
- **iPhone 13** (Mobile)

### Browsers Tested:
- Chrome (latest version)
- Safari (latest version on iPhone 13)


## Features Tested
1. **Homepage**
   - Navigation links: All links are functional and navigate correctly to their respective pages.
   - Blog posts display correctly with text and timestamps.
   - Pagination: The pagination works correctly, leading to the next page of blog posts.
   - Responsiveness: The site adapts to different screen sizes correctly, maintaining usability on both mobile and desktop views.
   - Navbar collapses correctly on mobile devices.

2. **Mobile Testing**
   - **Samsung Galaxy Z Flip 6** (Mobile): The layout adjusts properly for smaller screens. All elements are accessible.
   - **iPhone 13**: Same as above, responsive design works well across various screen sizes.

3. **Interactivity**
   - Navbar toggle works correctly on mobile devices.
   - Links open correctly when clicked.
   - "Home", "About", "Regisrer", "Login" and "Logout" links navigate to the correct destinations.
   - JavaScript-based features such as the collapsible navbar and Bootstrap components function as expected.

4. **SEO and Metadata**
   - Title tags and meta descriptions are present and correct.
   - Structured data (if applicable) is validated for SEO.
   - Favicon and Apple touch icon display correctly on all devices.

**Validation** 

- CSS validation  
  ![Alt text](staticfiles/admin/img/gis/cssvalidation.png)

- Html validation
 
  ![Alt text](staticfiles/admin/img/gis/htmlvalidation.png)

- Lighthouse 
  Mobile
  ![Alt text](staticfiles/admin/img/gis/mobilelighthouse.png)

  Desktop 
  ![Alt text](staticfiles/admin/img/gis/desktoplighthouse.png)

## Known Bugs
1. **Webmanifest File Failure**:  
   The webmanifest file (`/static/images/site.webmanifest`) fails to load properly on some devices, which may affect the display of the site icon when the site is added to the home screen on Android devices. This does not affect the core functionality of the blog but may be a problem for users who add the site to their home screen for offline use.

2. **Minor UI Glitch on Mobile**:
   On mobile devices, some text elements slightly overlap on the blog post cards in the main feed. This does not impact the content readability but should be addressed for a smoother user experience.

---

## Bugs That Do Not Affect Functionality
1. **Trailing Slash on Void Elements**: 
   Some self-closing tags, such as `<hr />`, still include trailing slashes. This does not cause any functionality issues on modern browsers but could lead to validation warnings. The site renders correctly across all browsers and devices.

2. **Font Loading on First Load**:  
   Occasionally, on the first load of the site (especially on slower networks), fonts may load slightly delayed, causing a flash of unstyled text (FOUT). This does not affect functionality but may impact the user experience on slower connections.

---

## Summary
The site is fully functional and responsive across tested devices, including the **Samsung Galaxy Z Flip 6** and **iPhone 13**. The core features such as navigation, blog post rendering, pagination, and interactivity work as expected. There are a few known bugs, such as the webmanifest failing to load, but these do not affect the blog’s core functionality.

### Next Steps:
- Resolve the webmanifest loading issue to ensure better home screen experience for Android users.
- Address the minor UI glitches on mobile devices for a more polished mobile experience.
- Fix html code, It works, but it's not fully semantic

## Learnings and Mistakes

### What I Learned

1. **The Importance of Planning**  
   I didn’t initially plan the project step-by-step on a Kanban board, which led to a lack of structure in the development process. If I had planned more thoroughly, I could have avoided time-consuming backtracking.

2. **Simple Design is Key**  
   Trying to implement too many features in the design initially was overwhelming. I learned that it’s better to start simple and iterate later.

3. **Use of Bootstrap**  
   The use of **Bootstrap** significantly sped up the responsive design process, but I had to customize it to better fit the theme of my blog.

### Mistakes I Made

1. **Skipping the Paper Prototype**  
   In hindsight, designing the layout on paper before jumping into code would have helped me better understand the user flow on different devices. I later drew basic models of the site for **mobile** and **tablet** (iPad) views, which helped clarify the user experience and planning my prodject. 

2. **Lack of Error Handling in Forms**  
   I did not plan for robust error handling in the forms (user registration and commenting), which led to occasional frustration when users encountered vague errors.

3. **Underestimating complexity and time**  
   I started out to follow a turorial on YT, a prodject that was more complex than I unserstood. After a session with my mentor I diside to start over and follow the LMS as mush as possible. 


## Acknowledgements

I would like to express my sincere gratitude to everyone who has helped and supported me throughout the development of this project. Your guidance, encouragement, and constructive feedback have been invaluable. Special thanks to [insert names or groups here] for their unwavering support and for offering their time, expertise, and inspiration.

This project wouldn't have been possible without your contributions, and I am incredibly grateful for all the learning and growth I've experienced along the way.

Thanks to Malin5p for sharing her PP4 and board. 
Thanks to Swedish slack comunity for support and help.
Thanks to Tutor support. 
Thanks to mentor Rory to make me understand It was better to start over and keep It simple. 

## Contact

For questions or feedback, please contact me via anrosencrantz79@icloud.com
