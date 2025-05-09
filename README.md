Hosted Website Link: https://green-genius-wine.vercel.app

Final Write-Up:

Project Title: Green Genius

Team Members:
Utsav Kataria
Adnan Kabir
Juhi Parikh

Description of final project idea (Overview):

Green Genius is a personalized sustainability tracker and goal‑setting platform built with Flask. The app helps users live more environmentally conscious lives by combining user‑generated eco‑goals, habit tracking, and AI‑powered advice. Users can register, log in, and interact with a built‑in AI assistant to ask open‑ended questions about sustainable living. They can log daily eco‑friendly actions (e.g., biking to work), track their progress over time, and set custom sustainability goals with optional target dates. The dashboard presents visual insights such as category breakdowns and weekly progress charts, making eco‑conscious living both actionable and motivating.

Description of functionality only available to logged-in users:
Submitting sustainability questions to the AI assistant
Logging eco‑friendly actions for progress tracking
Creating, editing, and saving personal sustainability goals
Viewing the personalized dashboard (saved goals, recent actions, charts)
Saving AI‑generated suggestions for later review

Forms:
RegistrationForm: Collects username, email, password, and password confirmation for new user signup.
LoginForm: Accepts email and password to authenticate and start a user session.
AIQuestionForm: Provides a textarea for users to submit open‑ended sustainability questions to the AI assistant.
EcoActionForm: Lets users log an eco‑friendly action with a description and category dropdown (energy, waste, transport, food, water, other).
GoalForm: Allows users to set a sustainability goal with title, description, and optional target completion date.

Routes / Blueprints:
auth (/auth):
/register (GET/POST) — User signup
/login (GET/POST) — User authentication
/logout (GET) — End session
ai (/ai):
/ask (GET/POST) — Render AI question form and submit prompt to OpenAI
/history (GET) — List past questions and responses
/view/<suggestion_id> (GET) — View a specific AI suggestion
/save/<suggestion_id> (GET) — Mark a suggestion as saved
tracker (/tracker):
/log-action (GET/POST) — Log a new eco‑action
/actions-history (GET) — View full history of actions
/set-goal (GET/POST) — Create a new sustainability goal
/update-goal/<goal_id>/<status> (GET) — Change goal status (in progress, completed, abandoned)
dashboard (/dashboard):
/home (GET) — Show the user’s dashboard with stats, charts, recent actions, active goals, and saved tips

Database (What will be stored/retrieved from MongoDB):
users: _id, username, email, password_hash, created_at
eco_actions: user_id, action_text, category, timestamp
sustainability_goals: user_id, title, description, status, created_at, target_date
ai_suggestions: user_id, question, response, timestamp, saved

APIs:

We integrated GROQ’s hosted endpoint using the requests Python library to power our AI assistant, Green Genius. When users submit sustainability-related questions through the app, we send their prompt to the LLaMA 4 Scout 17B model via a POST request to the GROQ API. The model generates tailored, real-time advice, which we store in MongoDB alongside the user’s ID and timestamp.

This integration enhances the user experience by offering personalized, context-aware tips that go beyond static content. It fosters ongoing engagement, supports goal progress, and adds a sense of interactivity.

Added Styling (Extra Credit):
Consistent visual design using custom CSS components to maintain a cohesive look across login, dashboard, AI response, goal tracking, and history pages
Custom color-coded badges for eco-action categories to enhance quick visual identification of sustainability topics.
Responsive card layouts and flexbox styling for the dashboard — especially the statistics and chart sections — to minimize scrolling and maximize content visibility
Proper spacing and padding around form elements and content blocks to reduce visual clutter and improve readability.
Accessible hover effects and button styling
Charts and dashboard cards for a smooth user experience
