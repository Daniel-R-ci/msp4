# Config variables / Settings

These are the variables stored in env.py for development, and in config variables in Hero Deployment. They have identical values, unless otherwise stated.

## Settings used in both env.py and Heroku Config Variables

- DATABASE_URL, containing path and key to PostgreSQL database
- DEBUG, set to True in env.py and "" in config variable, translating to value False. This ensures Debug is always set to True respectively False in development versus deployed version.
- DJANGO_SECRET_KEY, containing the Django Secret Key
- AWS_ACCES_KEY_ID and AWS_SECRET_ACCESS_KEY, to handle AWS requests
- STRIPE_PUBLISHALBE_KEY, CLIENT_SECRET and STRIPE_WH_SECRET for STRIPE payments

## Settings used only as Heroku Config Variables

- DEPLOYED, with value TRUE. A check if DEPLOYED exists in settings.py tells Django wether to chose deployment or development settings (email and static folder)
- EMAIL_HOST_PASS and EMAIL_HOST_USER, to handle sending emails. In development settings, emails are printed to terminal.