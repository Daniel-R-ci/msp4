# Config variables

These variables are stored in env.py for development, and in config variables in Hero Deployment.

- DATABASE_URL, containing path and key to PostgreSQL database
- DEBUG, set to True in env.py and "" in config variable, translating to value False. This ensures Debug is always set to True respectively False in development and deployed version.
- DJANGO_SECRET_KEY, containing the Django Secret Key