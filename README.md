**THIS PROJECT IS NOW ARCHIVED AND MOVED TO [OUR GITLAB REPOSITORY](https://gitlab.com/TheHammerBot/TheHammer)**

# The Hammer
An open source general purpose [Discord](https://discordapp.com/) Bot

## Development Team
Category            | People
------------------- | --------------------------
Lead Developer      | JustMaffie#5001 ([@JustMaffie](https://github.com/JustMaffie))
Developer           | CircuitRCAY#3038 ([@CircuitCodes](https://github.com/CircuitCodes))
Contributor         | Tom#4405 ([@Douile](https://github.com/Douile))

## Installation
1. `git clone https://github.com/TheHammerBot/TheHammer && cd TheHammer`
1. `cp config.example.json config.json`
1. Edit `config.json`
1. `sudo python3.6 -m pip install -r requirements.txt`
1. `sudo sh ./run.sh`

## Fortnite Command
To be able to use the Fortnite command you must set the `fortnite_api_key` setting in the `config.json`, you can create one at [fortnitetracker.com/site-api](https://fortnitetracker.com/site-api)

### Production
In case you run a production instance of this bot on `Linux`, you are recommended to install `UVLoop`, this will severely speed up your bot.

## Licence

```
    The Hammer
    Copyright (C) 2018 Jori van Ee (JustMaffie)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
```

### Info.json
The `info.json` file is for information about the bot, this should only be changed by project maintainers.
