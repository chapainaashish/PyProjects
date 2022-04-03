# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

# program to take search keyword and print the results as relevance
import time
from search_engine import search


user_list = ["python is programming language.", "python named after python snake.", "aashish is good",
             "life is beautiful", "everything is connected", "computer is a intelligent machine",
             "computer can be used in different applications", "git is used to push code",
             "we are anonymous, we donot forget, we donot forgive.", "some people think python isn't python"]
news = ["Riots broke out in cities across the Netherlands on Sunday, the third night in a row that police clashed with mobs of angry youths who set fires and threw rocks to protest COVID-19 restrictions.", "Oil off 7-week lows but under pressure as release of reserves eyed", "Kyle Rittenhouse says said that his case was not about the contentious issue of race — and that, in fact, he supports Black Lives Matter.", "For a few minutes in the fourth quarter, it looked like the Chargers were going to add another game to the long list of crushing defeats. The Steelers had mounted a furious comeback with a blocked punt, interception, and fourth-down stop — building a 37-34 le…", "Celebrities including Olivia Rodrigo, BTS and Chlöe are on the red carpet tonight for the American Music Awards in Los Angeles -- an annual event that not only celebrates promising new talent and established artists, but is a fashion spectacle.", "SUBSCRIBE TO OUR CHANNEL:https://www.youtube.com/user/CBSSportsHQ FOLLOW US ON:Facebook - https://www.facebook.com/CBSSports/Instagram - https://www.instagra...", "The released members of Christian Aid Ministries are safe, the Ohio-based church organization said Sunday, after they were kidnapped by a Haitan gang in October.", "Three suspects were arrested Saturday night after dozens ransacked a Nordstrom department store near San Francisco in what police are calling a \"smash-and-grab\" incident.", "The safe-haven U.S. dollar traded close to a 16-month high to the euro on Monday on growing anxiety over the impact of surging Covid-19 infections in Europe.",
        "Republican party’s José Antonio Kast set to win first round with 28% of the vote", "UPDATE | An hours-long standoff continues in southeast Portland Sunday night as police say they are working to negotiate a hostage situation at an apartment complex. The incident started around 3:30 p. m. in the 2400 block of Southeast 171st Avenue. Portland …", "The Centers for Disease Control and Prevention on Friday expanded availability of COVID-19 booster shots to all American adults, hoping to preserve vaccine protection against the fast-spreading delta variant.", "Rep. Alexandria Ocasio-Cortez said the stakes of passing the Build Back Better Act are \"really, really high.\"", "HPD is reporting the 1-year-old is expected to survive after being shot in the abdomen. There are no suspects in custody at this time.", "It is very likely the formula the Giants used for their success two weeks ago will not be the approach they take Monday night against the Buccaneers at Raymond James Stadium.", "The reality star and the \"Saturday Night Live\" castmember were all smiles as they walked hand-in-hand.", "\"Ghostbusters: Afterlife\" has unseated \"Eternals\" atop the domestic box office, while awards-buzzy tennis drama \"King Richard\" opened at No. 4.", "As a new wave of Covid infections spreads over Europe, resistance to public health measures is growing, and not just in Austria.", "A Wall Street Journal report says he met last week with executives and senior managers", "Peter Aykroyd, a former\xa0comedian and writer on \"Saturday Night Live\"\xa0and the brother of \"Ghostbusters\" star Dan Aykroyd, has died, \"SNL\" announced."]

user_search = str(input("\nEnter the keyword: ")).lower()
start_time = time.time()
sorted_list = search(user_search, news)

print(
    f"\n{len(sorted_list)} search results in {time.time() - start_time} second\n ")

if len(sorted_list) == 0:
    print("No search results found!\n")
    exit()

else:
    for item in sorted_list:
        print(f"\t\t{item[1].capitalize()}\n")
