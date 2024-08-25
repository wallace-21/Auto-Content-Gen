<h1>Social Media AI System</h1>

<h2>Overview</h2>
<p>
The Social Media AI System is a Flask-based web application that allows you to manage articles, generate summaries using OpenAI's API, and post these summaries to various social media platforms including Facebook, X (formerly Twitter), LinkedIn, and Instagram.
</p>

<h2>Features</h2>
<ul>
<li><strong>CRUD Operations</strong>: Create, Read, Update, and Delete articles.</li>
<li><strong>Summary Generation</strong>: Automatically generate summaries of articles using OpenAI's API.</li>
<li><strong>Social Media Integration</strong>: Post generated summaries to Facebook, X, LinkedIn, and Instagram.</li>
<li><strong>Database</strong>: Uses SQLite for storing article information.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
<li><strong>Flask</strong>: Web framework for Python.</li>
<li><strong>SQLAlchemy</strong>: SQL toolkit and Object-Relational Mapping (ORM) library.</li>
<li><strong>OpenAI API</strong>: For generating article summaries.</li>
<li><strong>Requests</strong>: For making HTTP requests to social media APIs.</li>
<li><strong>python-dotenv</strong>: For managing environment variables.</li>
</ul>

<li><strong>Install Dependencies:</strong></li>
<pre><code>pip install -r requirements.txt</code></pre>

<li><strong>Create a `.env` File:</strong> Copy `.env.example` to `.env` and fill in the required values:</li>
<pre><code>DATABASE_URL=your_database_url_here
OPENAI_API_KEY=your_openai_api_key_here
FACEBOOK_ACCESS_TOKEN=your_facebook_access_token_here
FACEBOOK_PAGE_ID=your_facebook_page_id_here
TWITTER_API_KEY=your_twitter_api_key_here
TWITTER_API_SECRET=your_twitter_api_secret_here
TWITTER_ACCESS_TOKEN=your_twitter_access_token_here
TWITTER_ACCESS_SECRET=your_twitter_access_secret_here
LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token_here
INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token_here
INSTAGRAM_USER_ID=your_instagram_user_id_here</code></pre>
<h2>Installation</h2>
<ol>
<li><strong>Clone the Repository:</strong></li>
<pre><code>git clone https://github.com/wallace-21/Auto-Content-Gen.git
cd your-repository</code></pre>
</ol>
