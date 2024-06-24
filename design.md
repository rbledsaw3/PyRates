### PyRates! Design Document

#### Overview
"PyRates!" is a terminal-based, text-driven game inspired by "Sid Meier's Pirates!" set during the golden age of piracy. Players will navigate the Caribbean, engage in naval battles, trade goods, undertake quests, manage their crew, and hunt for treasure, all through text commands and narrative descriptions.

#### Game Mechanics

1. **Sailing and Navigation**
   - **Description**: Players navigate their ship across a map of the Caribbean using text commands. They can encounter other ships, ports, and random events.
   - **Key Commands**: `sail north`, `sail south`, `sail east`, `sail west`, `check map`, `sail Porto Bello`, `make landfall`

2. **Naval Combat**
   - **Description**: Players engage enemy ships in text-based naval battles, choosing actions such as firing cannons, maneuvering, or boarding.
   - **Key Commands**:
     - **Carpenter**: `repair hull`, `repair sails`, `repair mast`
     - **Helmsman**: `evade`, `retreat`, `ram`, `board`, `maneuver`
     - **Gunner**: `switch ammo [chain/grape/ball]`, `fire`

3. **Sword Fighting**
   - **Description**: During boardings or personal duels, players engage in text-based sword fights, choosing attack and defense moves.
   - **Key Commands**: `attack high`, `attack mid`, `attack low`, `defend high`, `defend mid`, `defend low`

4. **Trading and Economics**
   - **Description**: Players can buy and sell goods at different ports, taking advantage of price differences to make a profit.
   - **Key Commands**: `buy [item] [quantity]`, `sell [item] [quantity]`, `check prices`

5. **Quests and Missions**
   - **Description**: Players undertake quests such as rescuing captives, finding lost cities, and capturing notorious pirates, each described through text.
   - **Key Commands**: `accept quest`, `check quests`, `complete quest`

6. **Crew Management**
   - **Description**: Players recruit and manage their crew, ensuring high morale to avoid mutinies.
   - **Key Commands**: `recruit crew`, `check morale`, `discipline crew`

7. **Romance and Reputation**
   - **Description**: Players can court governors' daughters and build a reputation, which affects their standing in different ports.
   - **Key Commands**: `court [name]`, `check reputation`

8. **Treasure Hunting**
   - **Description**: Players search for buried treasure using maps and clues, described through text-based puzzles.
   - **Key Commands**: `search treasure`, `use map`, `dig`

9. **Port Interactions**
   - **Description**: Players interact with various ports to trade, gather information, and recruit crew.
   - **Key Commands**: `visit port`, `gather information`, `recruit crew`

#### File and Folder Structure

```
/pyrates_game
│
├── /data               # Data files such as maps, item databases, etc.
│   └── quests.json     # Example data file for quests
│
├── /src                # Source code
│   ├── __init__.py
│   ├── main.py         # Main game entry point
│   ├── config.py       # Game configuration settings
│   │
│   ├── /game           # Game mechanics
│   │   ├── __init__.py
│   │   ├── sailing.py
│   │   ├── combat.py
│   │   ├── trading.py
│   │   ├── quests.py
│   │   ├── crew.py
│   │   ├── reputation.py
│   │   ├── treasure.py
│   │   └── port.py
│   │
│   ├── /models         # Game data models
│   │   ├── __init__.py
│   │   ├── ship.py
│   │   ├── character.py
│   │   ├── item.py
│   │   └── map.py
│   │
│   └── /utils          # Utility functions and helpers
│       ├── __init__.py
│       ├── helpers.py
│       └── math_utils.py
│
└── README.md
```

#### Class Responsibilities

**game/sailing.py**
```python
class Navigator:
    def __init__(self, map):
        self.map = map
        self.position = (0, 0)
        self.speed = 5
    
    def navigate(self, direction):
        # Logic to update ship position based on direction and speed
        pass
```

**game/combat.py**
```python
class NavalCombat:
    def __init__(self, player_ship, enemy_ship):
        self.player_ship = player_ship
        self.enemy_ship = enemy_ship
    
    def engage(self):
        # Logic for naval combat
        pass

    def issue_carpenter_command(self, command):
        # Logic to process carpenter command
        pass

    def issue_helmsman_command(self, command):
        # Logic to process helmsman command
        pass

    def issue_gunner_command(self, command):
        # Logic to process gunner command
        pass

class SwordFight:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
    
    def duel(self):
        # Logic for sword fighting
        pass
```

**game/trading.py**
```python
class Trader:
    def __init__(self, inventory):
        self.inventory = inventory
        self.prices = {}
    
    def buy(self, item, quantity):
        # Logic to handle buying items
        pass
    
    def sell(self, item, quantity):
        # Logic to handle selling items
        pass
```

**game/quests.py**
```python
class QuestManager:
    def __init__(self):
        self.quests = []
    
    def accept_quest(self, quest):
        # Logic to accept a quest
        pass
    
    def check_quests(self):
        # Logic to list current quests
        pass
    
    def complete_quest(self, quest):
        # Logic to complete a quest
        pass
```

**game/crew.py**
```python
class CrewManager:
    def __init__(self):
        self.crew = []
        self.morale = 100
    
    def recruit_crew(self, number):
        # Logic to recruit crew members
        pass
    
    def check_morale(self):
        # Logic to check crew morale
        pass
    
    def discipline_crew(self):
        # Logic to discipline crew
        pass
```

**game/reputation.py**
```python
class ReputationManager:
    def __init__(self):
        self.reputation = {}
    
    def court(self, name):
        # Logic to court a character
        pass
    
    def check_reputation(self):
        # Logic to check reputation
        pass
```

**game/treasure.py**
```python
class TreasureHunter:
    def __init__(self):
        self.maps = []
    
    def search_treasure(self):
        # Logic to search for treasure
        pass
    
    def use_map(self, map):
        # Logic to use a treasure map
        pass
    
    def dig(self):
        # Logic to dig for treasure
        pass
```

**game/port.py**
```python
class PortManager:
    def __init__(self):
        self.ports = []
    
    def visit_port(self, port_name):
        # Logic to visit a port
        pass
    
    def gather_information(self):
        # Logic to gather information
        pass
    
    def recruit_crew(self):
        # Logic to recruit crew in a port
        pass
```

### Summary
"PyRates!" will be a rich, text-based simulation of pirate life, capturing the essence of adventure, strategy, and exploration. This design document outlines the key mechanics, class structure, and folder organization to guide the development process.
