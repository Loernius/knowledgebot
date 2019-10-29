from bot import Knowledgebot
import json
def main():
    with open('config/config.json', 'r') as f:
        config = json.load(f)

    discordbot = Knowledgebot()

    discordbot.run(config['token'])

if __name__ == "__main__":
    main()