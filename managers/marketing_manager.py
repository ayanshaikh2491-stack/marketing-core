from agents.research_agent import run as research
from agents.strategy_agent import run as strategy
from agents.content_agent import run as content
from agents.reel_agent import run as reel
from agents.script_agent import run as script
from agents.hashtag_agent import run as hashtag
from agents.audience_agent import run as audience
from agents.psychology_agent import run as psychology

def handle_marketing(task):

    output = ""

    output += research(task) + "\n\n"
    output += strategy(task) + "\n\n"
    output += audience(task) + "\n\n"
    output += psychology(task) + "\n\n"
    output += content(task) + "\n\n"
    output += reel(task) + "\n\n"
    output += script(task) + "\n\n"
    output += hashtag(task) + "\n\n"

    return output
