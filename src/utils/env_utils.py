import os
from dotenv import load_dotenv

load_dotenv()

SAUCE_DEMO_BASEURL = os.getenv("SAUCE_DEMO_BASEURL", "https://www.saucedemo.com/")

SAUCE_DEMO_PASSWORD = os.getenv("SAUCE_DEMO_PASSWORD", "secret_sauce")
SAUCE_DEMO_INCORRECT_PASSWORD = os.getenv("SAUCE_DEMO_INCORRECT_PASSWORD", "secret_sauce_incorrect")

SAUCE_DEMO_STANDARD_USER = os.getenv("SAUCE_DEMO_STANDARD_USER", "standard_user")
SAUCE_DEMO_INCORRECT_USER = os.getenv("SAUCE_DEMO_INCORRECT_USER", "standard_user_incorrect")
SAUCE_DEMO_LOCKED_OUT_USER = os.getenv("SAUCE_DEMO_LOCKED_OUT_USER", "locked_out_user")
SAUCE_DEMO_PROBLEM_USER = os.getenv("SAUCE_DEMO_PROBLEM_USER", "problem_user")
SAUCE_DEMO_PERFORMACE_GLITCH_USER = os.getenv("SAUCE_DEMO_PERFORMACE_GLITCH_USER", "performance_glitch_user")
SAUCE_DEMO_ERROR_USER = os.getenv("SAUCE_DEMO_ERROR_USER", "error_user")
SAUCE_DEMO_VISUAL_USER = os.getenv("SAUCE_DEMO_VISUAL_USER", "visual_user")
